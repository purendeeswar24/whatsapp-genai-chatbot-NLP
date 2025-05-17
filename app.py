from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging
import asyncio
from collections import deque

app = Flask(__name__)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")  # Advanced model

# Session store with limited history
user_sessions = {}

# Predefined student questions and answers
STUDENT_FAQS = {
    "exam schedule": "The semester exams are scheduled for December 2025. Check your college portal for the detailed timetable.",
    "exam preparation": "Focus on past papers, create a study schedule, and revise key concepts. Group study can help too!",
    "scholarship": "Apply for scholarships like NSP, PMSS, or state-specific schemes via the National Scholarship Portal or your college office.",
    "career guidance": "Explore internships on Internshala or LinkedIn. Attend campus placement drives and consider upskilling in AI or data science.",
    "timetable": "The weekly timetable is available on the college website or notice board. Contact your department for updates.",
    "attendance": "Maintain at least 75% attendance as per university rules. Check your attendance on the student portal.",
    "fee deadline": "The fee payment deadline for this semester is November 30, 2025. Pay online via the college website.",
    "internship": "Look for internships on Internshala, LetsIntern, or through college placement cells. Start with small projects to build your resume.",
    "placement": "Campus placements start in January 2026. Prepare your resume and practice aptitude tests now.",
    "study tips": "Break your study sessions into 25-minute Pomodoro chunks, take short breaks, and summarize notes daily."
}

# System prompt for Gemini fallback
SYSTEM_PROMPT = (
    "You are a helpful WhatsApp chatbot for Indian students, providing concise, accurate, and friendly answers. "
    "Focus on academic, career, and college-related queries. Keep responses under 100 words."
)

async def generate_response(prompt: str, user_number: str) -> str:
    """Generate a response using Gemini with session context and 30-second timeout."""
    try:
        # Get session history (limited to 5 messages)
        history = user_sessions.get(user_number, deque(maxlen=5))
        full_prompt = f"{SYSTEM_PROMPT}\n" + "\n".join(history) + f"\nUser: {prompt}\nBot:"

        # Run Gemini API call with 30-second timeout
        response = await asyncio.wait_for(
            asyncio.to_thread(model.generate_content, full_prompt),
            timeout=30.0
        )
        reply = response.text.strip()
        if not reply:
            reply = "Sorry, I couldn't generate a response. Please try again."
        return reply
    except asyncio.TimeoutError:
        logger.error(f"Timeout (30s) for user {user_number}: {prompt}")
        return "Server is busy, please try again later."
    except Exception as e:
        logger.error(f"Error generating response for {user_number}: {str(e)}")
        return "Oops, something went wrong. Please try again."

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip().lower()
    user_number = request.values.get("From", "")
    logger.info(f"Received message from {user_number}: {incoming_msg}")

    # Check for exit intent
    if incoming_msg in ["bye", "exit", "quit"]:
        farewell = "It was great helping you! All the best for your studies! 👋"
        user_sessions.pop(user_number, None)

        twilio_resp = MessagingResponse()
        twilio_resp.message(farewell)
        return str(twilio_resp)

    # Initialize session if not exists
    if user_number not in user_sessions:
        user_sessions[user_number] = deque(maxlen=5)

    # Check for predefined student FAQs
    reply = None
    for question, answer in STUDENT_FAQS.items():
        if question in incoming_msg:
            reply = answer
            break

    # Fallback to Gemini if no predefined answer
    if not reply:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            reply = loop.run_until_complete(generate_response(incoming_msg, user_number))
        finally:
            loop.close()

    # Update session history
    user_sessions[user_number].append(f"User: {incoming_msg}\nBot: {reply}")

    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)