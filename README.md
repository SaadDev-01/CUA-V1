# CUA-V1 🚀

<div align="center">

**AI-Powered GUI Automation Agent**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/SaadDev-01/CUA-V1)

**Transform any GUI task into automated AI-driven actions**

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## ✨ Features

CUA-V1 is a cutting-edge AI agent that automates GUI tasks using multimodal Large Language Models. It sees your screen, understands what to do, and executes actions autonomously.

### 🎯 Core Capabilities

- **👁️ Visual Understanding**: Uses vision-capable LLMs to see and understand GUI elements
- **🤖 Autonomous Actions**: Automatically clicks, types, and navigates to complete tasks
- **🌐 Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **🔌 Multiple Providers**: Support for OpenAI, Anthropic, Ollama (local models), and more
- **💻 Code Execution**: Built-in Python/Bash code execution for complex tasks
- **🎯 Precise Grounding**: Dual-model architecture for accurate UI element targeting
- **🧠 Reflection System**: Self-improving agent that reviews and optimizes actions
- **🔒 Privacy-First**: Use local models with Ollama for complete privacy

### 🏆 Why CUA-V1?

- **Free to Use**: Run with local models (Ollama) - no API costs
- **Easy Setup**: Get started in 5 minutes with simple commands
- **Flexible**: Switch between cloud and local models instantly
- **Powerful**: Handles complex multi-step tasks autonomously
- **Open Source**: Fully customizable and extensible

---

## 🚀 Quick Start

### Option 1: Using Ollama (Free, Local, Privacy-Focused)

```bash
# Install Ollama from https://ollama.com/download
# Download a model
ollama pull llama3.2

# Run CUA-V1
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Open Chrome and search for AI automation"
```

### Option 2: Using OpenAI (Cloud-Based)

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key YOUR_API_KEY \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Your task here"
```

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- For local models: [Ollama](https://ollama.com/download)

### Install CUA-V1

```bash
# Clone the repository
git clone https://github.com/SaadDev-01/CUA-V1.git
cd CUA-V1

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Install Ollama (Optional, for Local Models)

See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for detailed instructions.

---

## 💡 Usage

### Basic Command Structure

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider PROVIDER \
    --model MODEL_NAME \
    --ground_provider GROUNDING_PROVIDER \
    --ground_url GROUNDING_URL \
    --ground_model GROUNDING_MODEL \
    --grounding_width WIDTH \
    --grounding_height HEIGHT \
    --task "YOUR_TASK"
```

### Command-Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `--provider` | LLM provider (openai, anthropic, ollama, etc.) | No (default: openai) |
| `--model` | Model name (e.g., gpt-4o, llama3.2) | No (default: gpt-4o) |
| `--model_url` | Custom API endpoint URL | No |
| `--model_api_key` | API key for the model | No |
| `--ground_provider` | Grounding model provider | **Yes** |
| `--ground_url` | Grounding model API URL | **Yes** |
| `--ground_api_key` | Grounding model API key | No |
| `--ground_model` | Grounding model name | **Yes** |
| `--grounding_width` | Screenshot width | **Yes** |
| `--grounding_height` | Screenshot height | **Yes** |
| `--task` | Task description | No |
| `--enable_reflection` | Enable reflection agent | No |
| `--enable_local_env` | Enable local code execution | No |

---

## 📚 Examples

### Web Automation

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Open GitHub, search for CUA-V1 repository, and star it"
```

### Desktop Application Automation

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Open Notepad, type 'Hello from CUA-V1', and save the file"
```

### With Reflection Enabled

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key YOUR_API_KEY \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_reflection \
    --task "Complex multi-step task"
```

---

## 🧠 Supported Models

### Cloud Models

- **OpenAI**: GPT-4o, GPT-4.1, GPT-4 Turbo
- **Anthropic**: Claude 4 Sonnet, Claude 4 Opus
- **Google**: Gemini 2.0 Pro
- **OpenRouter**: Access to 200+ models
- **Azure OpenAI**: Enterprise Azure deployments

### Local Models (via Ollama)

- **Llama 3.3**: Best balance of speed and intelligence
- **Llama 3.2**: Lightweight, efficient for general use
- **Mistral**: Excellent for coding tasks
- **Phi-4**: Lightweight, fast for older computers
- **Qwen 2.5**: Strong multilingual capabilities

See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for model recommendations and requirements.

---

## 🏗️ Architecture

CUA-V1 uses a sophisticated multi-agent architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    CUA-V1 Agent                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐      ┌──────────────┐                 │
│  │   Worker     │◄────►│  Grounding   │                 │
│  │   Agent      │      │    Agent     │                 │
│  └──────────────┘      └──────────────┘                 │
│         │                       │                       │
│         ▼                       ▼                       │
│  ┌──────────────┐      ┌──────────────┐                 │
│  │  Reflection  │      │   Code       │                 │
│  │   Agent      │      │   Agent      │                 │
│  └──────────────┘      └──────────────┘                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- **Worker Agent**: Plans and executes actions
- **Grounding Agent**: Precisely locates UI elements on screen
- **Reflection Agent**: Reviews and improves actions
- **Code Agent**: Executes Python/Bash code for complex tasks

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Star the repository** ⭐
2. **Fork the repository**
3. **Create a feature branch**: `git checkout -b feature/amazing-feature`
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/CUA-V1.git
cd CUA-V1

# Install in development mode
pip install -e .

# Note: Tests are not yet implemented in this version
```

---

## 📖 Documentation

- [OLLAMA_SETUP.md](OLLAMA_SETUP.md) - Setup guide for local models
- [Examples](#-examples) - Usage examples
- [Architecture](#-architecture) - System design overview

---

## 🐛 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'gui_agents'"**
```bash
cd CUA-V1
pip install -e .
```

**"Connection refused" with Ollama**
- Ensure Ollama is running (check system tray/taskbar)
- Verify Ollama is installed correctly
- Try restarting Ollama

**Slow performance**
- Use a smaller model (try `phi4` instead of `llama3.3`)
- Close other applications to free up RAM
- Check system requirements in OLLAMA_SETUP.md

For more troubleshooting, see [OLLAMA_SETUP.md](OLLAMA_SETUP.md).

---

## 📊 Performance

| Model | Speed | Accuracy | RAM Required | Best For |
|-------|-------|----------|--------------|----------|
| Phi-4 | ⚡⚡⚡ | ⭐⭐⭐ | 4GB | Quick tasks, older computers |
| Llama 3.2 | ⚡⚡ | ⭐⭐⭐⭐ | 4GB | General use, balanced |
| Llama 3.3 | ⚡ | ⭐⭐⭐⭐⭐ | 8GB | Complex tasks |
| GPT-4o | ⚡⚡ | ⭐⭐⭐⭐⭐ | N/A | Best accuracy (cloud) |

---

## 🗺️ Roadmap

- [ ] Web browser-specific optimizations
- [ ] Mobile app automation support
- [ ] Visual task recording and replay
- [ ] Custom model fine-tuning guide
- [ ] Docker container for easy deployment
- [ ] Web dashboard for task management
- [ ] Multi-monitor support
- [ ] Task scheduling and automation

---

## 📝 License

This project is licensed under the Apache License 2.0 - see the [license](https://opensource.org/licenses/Apache-2.0) for details.

---

## 🙏 Acknowledgments

- Built upon advanced multimodal LLM research
- Inspired by the need for accessible GUI automation
- Community feedback and contributions

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/SaadDev-01/CUA-V1/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SaadDev-01/CUA-V1/discussions)
- **Email**: For business inquiries

---

<div align="center">

**⭐ If you find CUA-V1 useful, please star the repository! ⭐**

Made with ❤️ by [SaadDev-01](https://github.com/SaadDev-01)

</div>
