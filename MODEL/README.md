# Nova AI - Intelligent Chatbot with Voice Support

A modern, interactive AI chatbot built with Streamlit that supports both text and voice interactions. Powered by Groq's Llama model and OpenAI Whisper for speech recognition.

## 🤖 Features

- **Text Chat**: Interactive text-based conversations with Nova AI
- **Voice Input**: Record and transcribe audio messages using microphone input
- **Modern UI**: Clean, dark-themed interface with smooth animations
- **Real-time Responses**: Streaming text responses with typing animation
- **ASR Integration**: Automatic Speech Recognition using OpenAI Whisper
- **Audio Processing**: Support for multiple audio formats (WAV, MP3, FLAC, OGG, M4A)

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))
- Microphone access (optional, for voice input)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MODEL
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file or set the environment variable:
   ```bash
   export GROQ_API_KEY="your-groq-api-key-here"
   ```
   
   On Windows (PowerShell):
   ```powershell
   $env:GROQ_API_KEY="your-groq-api-key-here"
   ```

## 🎯 Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

### Using the Inference Script

For processing audio files directly:

```bash
python inference.py --audio path/to/your/audio.wav
```

## 📁 Project Structure

```
MODEL/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration constants
├── inference.py           # Audio file processing script
├── requirement.txt        # Python dependencies
├── model/
│   ├── groq_model.py     # Groq API integration
│   ├── asr_model.py      # Speech recognition model
│   └── text_model.py     # Text generation utilities
└── utils/
    ├── audio_utils.py     # Audio processing utilities
    └── prompt_engine.py   # Prompt building functions
```

## ⚙️ Configuration

Edit `config.py` to customize:

- `ASR_MODEL_NAME`: Speech recognition model (default: "openai/whisper-small")
- `TEXT_MODEL_NAME`: Text generation model
- `MAX_RESPONSE_TOKENS`: Maximum response length
- `SUPPORTED_AUDIO_TYPES`: Supported audio file formats

## 🔧 Technologies Used

- **Streamlit**: Web application framework
- **Groq API**: Fast LLM inference (Llama 4 Maverick 17B)
- **Transformers**: Hugging Face models for ASR
- **Librosa**: Audio processing
- **SoundFile**: Audio file I/O
- **Audio Recorder Streamlit**: Microphone input widget

## 📝 Features in Detail

### Text Chat
- Clean, bubble-free chat interface
- Real-time message streaming
- HTML sanitization for security
- Conversation history management

### Voice Input
- One-click audio recording
- Automatic transcription
- Support for multiple audio formats
- Audio normalization and processing

### Model Configuration
- Uses Groq's `meta-llama/llama-4-maverick-17b-128e-instruct` model
- Temperature: 0.7 for balanced responses
- Max tokens: 300 for concise replies
- Plain-text output enforcement

## 🛠️ Development

### Adding New Features

1. **Audio Processing**: Extend `utils/audio_utils.py` for custom audio handling
2. **Model Integration**: Modify `model/groq_model.py` to use different models
3. **UI Customization**: Edit CSS in `app.py` for styling changes

### Troubleshooting

**Issue**: Microphone not working
- Ensure `audio-recorder-streamlit` is installed
- Check browser permissions for microphone access

**Issue**: API errors
- Verify `GROQ_API_KEY` is set correctly
- Check your Groq API quota

**Issue**: Model loading errors
- Ensure all dependencies are installed
- Check internet connection for model downloads

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on the GitHub repository.

---

**Made with ❤️ using Streamlit and Groq**

