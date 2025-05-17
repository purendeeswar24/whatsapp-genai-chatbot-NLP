from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch

# Initialize Flask
app = Flask(__name__)

# Load BlenderBot model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Optional: keep short conversation history per user
user_sessions = {}

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip().lower()
    user_number = request.values.get("From", "")

    # Check if the user wants to end the chat
    if incoming_msg in ["bye", "exit", "quit"]:
        farewell = "It was great chatting with you! Have a wonderful day 👋"
        user_sessions.pop(user_number, None)  # Clear session if exists

        twilio_resp = MessagingResponse()
        twilio_resp.message(farewell)
        return str(twilio_resp)

    # Otherwise, continue the chat
    history = user_sessions.get(user_number, "")
    inputs = tokenizer([history + " " + incoming_msg], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Save updated history
    user_sessions[user_number] = incoming_msg + " " + response

    twilio_resp = MessagingResponse()
    twilio_resp.message(response)
    return str(twilio_resp)