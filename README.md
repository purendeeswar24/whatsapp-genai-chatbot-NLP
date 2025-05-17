<div align="center">
  <h1>🚀 WhatsApp AI Chatbot</h1>
  <p>✨ A Smart, Real-Time Conversational AI Powered by <b>Google Gemini</b> & <b>Twilio</b> ✨</p>
  <p>Transform WhatsApp into a dynamic platform for customer support, personal assistance, or education with this customizable chatbot built on Python and Flask!</p>
  <a href="https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio"><img src="https://img.shields.io/github/stars/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio/blob/main/LICENSE"><img src="https://img.shields.io/github/license/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio" alt="License"></a>
</div>

---

## 🌟 Why This Chatbot?

This **WhatsApp AI Chatbot** brings intelligent, real-time conversations to your fingertips! Powered by **Google Gemini** for cutting-edge generative AI and **Twilio** for seamless WhatsApp integration, this project is perfect for:

- 🛒 **Customer Support**: Automate responses and enhance user experience.
- 🤝 **Personal Assistants**: Schedule, remind, or answer queries.
- 📚 **Education**: Provide instant answers for students and learners.
- 💡 **Custom Use Cases**: Tailor it to your unique needs!

---

## ✨ Key Features

- ⚡ **Real-Time Conversations**: Instant, smart replies on WhatsApp.
- 🧠 **AI-Powered**: Leverages Google Gemini for intelligent responses.
- 📲 **Twilio Integration**: Seamless WhatsApp messaging API.
- 🗣️ **Session-Aware**: Maintains context for natural conversations (optional).
- 🌍 **Easy Deployment**: Run locally with ngrok or deploy to a production server.
- 🔧 **Highly Customizable**: Adapt prompts and logic for any use case.

---

## 🛠️ Tech Stack

| Component       | Technology                            |
|-----------------|---------------------------------------|
| **Language**    | 🐍 Python                             |
| **Framework**   | ⚙️ Flask                              |
| **AI Engine**   | 🌟 Google Gemini API                  |
| **Messaging**   | 📱 Twilio WhatsApp API                |
| **Deployment**  | 🚀 ngrok / Production Server          |
| **Tools**       | 🛠️ Git, Postman, VS Code             |

---

## 🚀 Getting Started

Follow these steps to set up and run your WhatsApp AI Chatbot locally or deploy it to a server.

### 📋 Prerequisites

- 🐍 Python 3.8+
- 🔑 Google Gemini API Key ([Get it here](https://cloud.google.com/gemini))
- 📲 Twilio Account & WhatsApp API Credentials ([Sign up here](https://www.twilio.com))
- 🌐 ngrok (for local testing) or a server for production

### 🛠️ Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/purendeeswar24/WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio.git
   cd WhatsApp-AI-Chatbot-Conversational-AI-using-Google-Gemini-Twilio
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   Create a `.env` file in the project root and add:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   ```

4. **Run the Flask App Locally**  
   ```bash
   python app.py
   ```

5. **Expose Your Local Server with ngrok**  
   ```bash
   ngrok http 5000
   ```
   Copy the ngrok URL (e.g., `https://your-ngrok-url.ngrok.io`) and configure it as the webhook in your Twilio WhatsApp sandbox.

6. **Test the Chatbot**  
   Send a message to your Twilio WhatsApp number and watch the AI respond! 🎉

---

## 🌐 Deployment

For production, deploy the Flask app to a cloud platform like **Heroku**, **AWS**, or **Google Cloud**. Update the Twilio webhook with your production URL.

---

## 🛠️ Customization

- **Prompt Engineering**: Modify the prompts in `app.py` to tailor the AI’s tone and responses.
- **Session Management**: Enable session-aware conversations by storing chat history (see `session.py`).
- **Use Cases**: Extend functionality for e-commerce, FAQs, or niche applications.

---

## 🤝 Contributing

We’d love your contributions! 💡  
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m 'Add awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **Google Gemini**: For powering the AI brain.
- **Twilio**: For seamless WhatsApp integration.
- **Flask**: For making web development a breeze.
- **You**: For exploring this project! 🚀

---

<div align="center">
  <p>Built with ❤️ by <a href="https://github.com/purendeeswar24">Purendeeswar</a></p>
  <p>Star the repo 🌟 and share your feedback!</p>
</div>
