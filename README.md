# 🧠 gemiTask - AI-Powered Terminal Task Manager

A free, open-source, terminal-based task management tool powered by Google's Gemini AI. Break down complex tasks into actionable steps, get smart suggestions, and stay productive - all from your terminal.

## ✨ Features

- 🤖 AI-powered task breakdown using Google's Gemini
- 📝 Natural language task input
- ⏱️ Smart time estimates and deadlines
- 📋 Subtask management
- 🔄 Task dependencies
- ⭐ Priority levels
- 🎯 Smart task suggestions
- 💾 Local JSON storage

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemiTask.git
   cd gemiTask
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API key**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy your API key

4. **Configure gemiTask**
   - Copy `config.json.example` to `config.json`
   - Add your Gemini API key to `config.json`

## 🛠️ Usage

### Add a new task
```bash
python main.py add "Build a landing page for product launch"
```

### List all tasks
```bash
python main.py list
```

### Show completed tasks
```bash
python main.py list --done
```

### Mark a task as done
```bash
python main.py done 1
```

### Get task breakdown
```bash
python main.py breakdown 1
```

### Get next task suggestion
```bash
python main.py suggest
```

## 📁 Project Structure

```
gemiTask/
├── main.py          # CLI interface
├── gemini.py        # Gemini API integration
├── storage.py       # JSON storage
├── task.py          # Task model
├── config.json      # API configuration
└── requirements.txt # Dependencies
```

## 🔧 Configuration

Edit `config.json` to customize your setup:
```json
{
  "gemini_api_key": "your-api-key-here"
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering the task analysis
- The open-source community for inspiration and tools 