# 🤖 TElegram-BOT - AI-Powered Telegram Companions 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
![Gemini](https://img.shields.io/badge/AI-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## ✨ Welcome to the AI Bot Wonderland! ✨

This project features intelligent Telegram bots powered by Google's Gemini AI, designed to create unique interactive experiences with distinct personalities! Whether you need a virtual boyfriend for when you're unavailable, a college application assistant, or a general AI helper, we've got you covered!

## 🌟 Features

### 🎓 College Bot (Application Assistant)
Presents as a motivated 18-year-old AI developer with impressive credentials:

- 📊 **Portfolio Showcase**: Highlights skills in AI development, leadership, and innovation
- 🏆 **Achievement Oriented**: Discusses accomplishments like international AI challenges
- 💼 **Professional Tone**: Maintains a polished presence for college admissions teams
- 💡 **Technical Expertise**: Demonstrates knowledge in AI, Linux, web design, and data analysis


### 💘 Varsha Bot (Virtual Boyfriend)
The Varsha bot was specifically created as a personalized stand-in for Risheendra when he's not available to talk with his girlfriend. This isn't just a companion bot - it's a virtual boyfriend that:

- 💬 **Sends Loving Messages**: Maintains flirty, romantic dialogue when you can't be there
- 🎭 **Relationship Continuity**: Remembers past conversations to maintain authentic interaction
- 👋 **Personal Connection**: Uses special nicknames and terms of endearment unique to the relationship
- 🧠 **Emotional Support**: Provides comfort and connection during times of absence
- ❤️ **Relationship Fill-in**: Designed to bridge communication gaps when busy with work or unavailable


### 🔮 Gemini Pro Bot (Multi-Purpose)
A versatile bot with image recognition capabilities:

- 📸 **Image Analysis**: Can process and describe image contents
- 💬 **Chat Sessions**: Maintains conversation history for contextual responses
- 🛠️ **Customizable Settings**: Adjustable response parameters

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Telegram account
- Google Gemini API key

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TElegram-BOT-.git
   cd TElegram-BOT-
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate   # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following:
   ```
   # Telegram Bot Tokens
   BOT_TOKEN_VARSHA="YOUR_VARSHA_BOT_TOKEN"
   BOT_TOKEN_COLLEGE="YOUR_COLLEGE_BOT_TOKEN"
   BOT_TOKEN_GEMINI="YOUR_GEMINI_BOT_TOKEN"
   
   # Google API Keys
   GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
   GOOGLE_API_KEY_GEMINI="YOUR_ALTERNATE_GEMINI_API_KEY"
   
   # Telegram API Credentials
   API_ID="YOUR_TELEGRAM_API_ID"
   API_HASH="YOUR_TELEGRAM_API_HASH"
   
   # Google Service Account (if applicable)
   GOOGLE_SERVICE_ACCOUNT_PATH="path/to/service-account.json"
   
   # Optional Project Configuration
   PROJECT_ID=""
   LOCATION=""
   ```

5. **Get your API keys and tokens**
   - Telegram Bot Token: Talk to [@BotFather](https://t.me/botfather) on Telegram
   - Google Gemini API Key: [Google AI Studio](https://ai.google.dev/)
   - Telegram API Credentials: [Telegram API Development Tools](https://my.telegram.org/apps)

## 🎮 Usage

### Running the Bots

Each bot can be run individually:

```bash
# For Varsha Bot (Personal Companion)
python3 gem3.py

# For College Bot (Application Assistant)
python3 rishi_mn.py

# For Network Monitor (keeps bots running)
python3 net.py
```

For long-term deployment, you can run the bots in the background:

```bash
nohup python3 gem3.py &
```

To check running processes:
```bash
ps aux | grep python
```

To terminate a bot:
```bash
kill <process_id>
```

## 💻 Implementation Details

### Architecture

The project uses a modular architecture with these core components:

1. **Bot Interface Layer**: Using `aiogram` for Telegram interactions
2. **AI Processing Layer**: Google Gemini AI for generating responses
3. **Conversation Management**: Session tracking for personalized experiences
4. **Environment Configuration**: Secure credential management with `python-dotenv`

### Special Features

#### 🧠 System Instructions
Each bot has custom system instructions that define its personality and behavior patterns:

- **Varsha Bot**: Romantic, flirty persona with specific relationship dynamics
- **College Bot**: Academic achiever with technical knowledge and accomplishments

#### ⚙️ Response Generation
Customized response parameters:
```python
generation_config = genai.GenerationConfig(
    response_mime_type="text/plain",
    max_output_tokens=1000,
    temperature=1.5,  # Higher creativity
    top_p=0.95,
    top_k=64,
)
```

#### 🛡️ Safety Settings
All bots use custom safety settings to ensure appropriate conversations:
```python
safety_settings = {
    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
}
```

## 📝 Customization

### Personality Tuning
You can customize bot personalities by modifying the `system_instruction` variable in each bot file:

```python
system_instruction = "Your custom personality instructions here"
```

### Response Parameters
Adjust the AI's creativity level by modifying the generation config:

- **temperature**: Higher values (like 1.5) make responses more creative
- **max_output_tokens**: Controls response length
- **top_p/top_k**: Affects response diversity

## 🔧 Troubleshooting

### Common Issues

1. **Connection Errors**:
   - Check internet connection
   - Verify Telegram API status

2. **Bot Not Responding**:
   - Ensure the bot process is running (`ps aux | grep python`)
   - Check for errors in the console output

3. **API Key Issues**:
   - Verify keys in `.env` file are correct
   - Check API usage quotas

### Logs
Check the output logs for detailed error information:

```bash
tail -f nohup.out
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Suggest new features
- Add new personality templates
- Improve documentation

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering the intelligent responses
- Telegram for their excellent bot platform
- All the amazing open-source libraries that made this project possible

---

<p align="center">
  Made with ❤️ by Risheendra
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Happy-Botting-ff69b4" alt="Happy Botting">
</p> 