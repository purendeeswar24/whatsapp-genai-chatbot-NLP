<div align="center">
  <h1> WhatsApp AI Chatbot</h1>
  <p> A Smart, Real-Time Conversational AI Powered by <b>Google Gemini</b> & <b>Twilio</b> </p>
  <p>Transform WhatsApp into a dynamic platform for customer support, personal assistance, or education with this customizable chatbot built on Python and Flask!</p>
  <a href="https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio"><img src="https://img.shields.io/github/stars/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio/blob/main/LICENSE"><img src="https://img.shields.io/github/license/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio" alt="License"></a>
</div>

---

WhatsApp AI Chatbot
A robust conversational AI chatbot integrated with Google Gemini and Twilio, enabling intelligent, real-time interactions on WhatsApp. Built with Python and Flask, this project is designed for applications such as customer support, personal assistance, and appointment scheduling, offering a customizable and scalable solution.
Overview
This WhatsApp AI Chatbot leverages Google Gemini's advanced natural language processing capabilities and Twilio's WhatsApp API to deliver seamless, context-aware conversations. Deployed using Flask and ngrok, it provides a user-friendly interface within WhatsApp, eliminating the need for additional software. The chatbot supports casual interactions and practical use cases like appointment booking, making it a versatile tool for businesses and individuals.
Key Features

Real-time conversational AI on WhatsApp
Intelligent, context-aware responses powered by Google Gemini
Seamless integration with Twilio WhatsApp API
Optional session-aware conversations for contextual dialogue
Lightweight Flask backend for easy deployment
Customizable prompts for diverse use cases

Tech Stack



Component
Technology



Language
Python


Framework
Flask


AI Engine
Google Gemini API


Messaging
Twilio WhatsApp API


Deployment
ngrok / Production Server


Tools
Git, Postman, VS Code


Getting Started
Prerequisites

Python 3.8 or higher
Google Gemini API Key (available at https://cloud.google.com/gemini)
Twilio Account and WhatsApp API Credentials (sign up at https://www.twilio.com)
ngrok for local testing or a server for production

Installation

Clone the Repository
git clone https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio.git
cd WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio


Install Dependencies
pip install -r requirements.txt


Set Up Environment VariablesCreate a .env file in the project root and add:
GEMINI_API_KEY=your_gemini_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number


Run the Flask Application Locally
python app.py


Expose the Local Server with ngrok
ngrok http 5000

Copy the ngrok URL (e.g., https://your-ngrok-url.ngrok.io) and configure it as the webhook in your Twilio WhatsApp sandbox.

Test the ChatbotSend a message to your Twilio WhatsApp number to interact with the AI-powered chatbot.


Deployment
For production, deploy the Flask application to a cloud platform such as Heroku, AWS, or Google Cloud. Update the Twilio webhook with your production URL to ensure continuous operation.
Customization

Modify prompts in app.py to adjust the AI's tone and response style.
Enable session-aware conversations by implementing chat history storage (see session.py).
Extend functionality for specific use cases like e-commerce, customer support, or educational services.

Contributing
Contributions are welcome. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Google Gemini for advanced conversational AI capabilities
Twilio for reliable WhatsApp API integration
Flask for a lightweight and flexible web framework
Contributors and users for their support and feedback

Summary of Workflow
The chatbot operates through a streamlined workflow:

A user sends a message via WhatsApp to a Twilio-registered 번호.
Twilio captures the message and forwards it as an HTTPS POST request to the Flask application's webhook endpoint.
During development, ngrok exposes the local Flask server to the internet, providing a public URL for Twilio.
The Flask application processes the incoming message, extracts content, and sends it to the Google Gemini API for response generation.
Gemini, authenticated via a secure API key stored in a .env file, generates a context-aware response.
The Flask application formats the response for WhatsApp compatibility and sends it back to Twilio.
Twilio delivers the response to the user, completing the interaction cycle.

This architecture ensures real-time, intelligent conversations with minimal latency, leveraging modular components for scalability and ease of maintenance.
Main Advantages

Accessibility: Operates within WhatsApp, a platform with over 2 billion users, requiring no additional software or learning curve.
Intelligent Responses: Powered by Google Gemini, the chatbot delivers coherent, context-aware, and human-like replies, enhancing user engagement.
Scalability: The modular design allows easy updates, such as swapping AI models or deploying to cloud platforms, to handle large user bases.
Cost-Effective Development: Utilizes free-tier Gemini API access and ngrok for local testing, reducing initial costs.
Versatility: Supports diverse use cases, from casual conversations to appointment scheduling, with customizable prompts and logic.
Security: Environment variables and secure webhook communication ensure sensitive data protection.
Real-Time Interaction: Twilio's robust API and Gemini's low-latency processing enable instant responses, mimicking human conversation flow.

Built by Purendeeswar. Feedback and contributions are appreciated.
