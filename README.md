# CUA-V1

<div align="center">

**The Future of GUI Automation**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/SaadDev-01/CUA-V1)
[![Development Status](https://img.shields.io/badge/Status-Active%20Development-yellow)](https://github.com/SaadDev-01/CUA-V1)

**AI-Powered GUI Automation for Everyone**

Transform any GUI task into automated AI-driven actions with state-of-the-art multimodal LLMs.

[Documentation](#-documentation) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Contributing](#-contributing)

</div>

---

## Overview

CUA-V1 is an advanced AI agent that automates graphical user interface tasks using multimodal Large Language Models. By combining visual understanding with autonomous action execution, CUA-V1 can navigate applications, websites, and desktop environments with human-like intelligence.

### Key Differentiators

- **Vision-First Architecture**: Leverages multimodal LLMs to see and understand GUI elements in real-time
- **Multi-Agent System**: Sophisticated architecture with specialized agents for planning, grounding, reflection, and code execution
- **Provider Agnostic**: Support for 10+ LLM providers including OpenAI, Anthropic, Google, and local models via Ollama
- **Privacy-First**: Run entirely locally with open-source models—no data leaves your machine
- **Cross-Platform**: Native support for Windows, macOS, and Linux
- **Open Source**: Apache 2.0 licensed—free to use, modify, and distribute

---

## Quick Start

Get CUA-V1 running in under 5 minutes.

### Using Local Models (Recommended)

```bash
# Install Ollama
# Visit https://ollama.com/download

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

### Using Cloud Models

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model YOUR_MODEL_NAME \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key YOUR_API_KEY \
    --ground_model YOUR_MODEL_NAME \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Your task here"
```

---

## Installation

### Prerequisites

- Python 3.9 or higher
- For local models: [Ollama](https://ollama.com/download)

### Install from Source

```bash
git clone https://github.com/SaadDev-01/CUA-V1.git
cd CUA-V1
pip install -r requirements.txt
pip install -e .
```

### Verify Installation

```bash
python -m gui_agents.cua_v1.cli_app --help
```

---

## Architecture

CUA-V1 employs a sophisticated multi-agent architecture designed for complex GUI automation tasks.

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

**Agent Responsibilities:**
- **Worker Agent**: Task planning and action execution
- **Grounding Agent**: Precise UI element localization
- **Reflection Agent**: Action review and optimization
- **Code Agent**: Python/Bash code execution for complex tasks

---

## Supported Providers

### Cloud Providers

- **OpenAI**: GPT series models
- **Anthropic**: Claude series models
- **Google**: Gemini series models
- **xAI**: Grok models
- **Mistral**: Mistral models
- **OpenRouter**: Access to 500+ models
- **Azure OpenAI**: Enterprise deployments
- **HuggingFace**: Open model inference
- **vLLM**: Self-hosted models
- **Parasail**: High-performance inference

### Local Models (via Ollama)

- **Llama**: Meta's open models
- **Mistral**: Coding-optimized models
- **Phi**: Microsoft's lightweight models
- **Qwen**: Multilingual models
- **Gemma**: Google's open models
- **DeepSeek**: Open-source reasoning models

See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for detailed model recommendations.

---

## Usage

### Command-Line Interface

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

### Key Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--provider` | LLM provider | No (default: openai) |
| `--model` | Model name | No |
| `--ground_provider` | Grounding model provider | Yes |
| `--ground_url` | Grounding API URL | Yes |
| `--ground_model` | Grounding model name | Yes |
| `--grounding_width` | Screenshot width | Yes |
| `--grounding_height` | Screenshot height | Yes |
| `--task` | Task description | No |
| `--enable_reflection` | Enable reflection agent | No |
| `--enable_local_env` | Enable code execution | No |

---

## Development Status

CUA-V1 is in active development with a growing contributor community.

### Current Capabilities

- ✅ Multi-provider LLM support
- ✅ Local model execution via Ollama
- ✅ Cross-platform GUI automation
- ✅ Multi-agent architecture
- ✅ CLI interface
- ✅ Reflection system
- ✅ Code execution

### In Progress

- 🔄 Performance optimization
- 🔄 Documentation expansion
- 🔄 Test coverage
- 🔄 Error handling improvements

---

## Roadmap

We're building the future of GUI automation. Join us.

### Planned Features

- [ ] Web browser-specific optimizations
- [ ] Visual task recording and replay
- [ ] Custom model fine-tuning
- [ ] Docker deployment
- [ ] Web dashboard
- [ ] Multi-monitor support
- [ ] Task scheduling

### Contributing

**We need your help to build the future of GUI automation.**

CUA-V1 is an open-source project and we welcome contributions from developers of all skill levels. You can contribute by:

- **Improving existing features** - Optimize performance, fix bugs, enhance functionality
- **Adding new features** - Implement items from the roadmap or propose new ideas
- **Correcting issues** - Fix reported bugs and address edge cases
- **Adding upcoming features** - Help build planned features from the roadmap

**How to get started:**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
2. Check the [Roadmap](#-roadmap) for planned features
3. Open an issue to discuss your approach
4. Submit a pull request with your changes

**No contribution is too small.** Whether it's fixing a typo, improving documentation, or implementing a major feature, we appreciate all help.

---

## Documentation

- [OLLAMA_SETUP.md](OLLAMA_SETUP.md) - Local model setup guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community standards

---

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

---

## Acknowledgments

Built upon advanced multimodal LLM research. Inspired by the need for accessible GUI automation. Powered by community contributions.

---

<div align="center">

**[⭐ Star us on GitHub](https://github.com/SaadDev-01/CUA-V1)**

Made with ❤️ by [SaadDev-01](https://github.com/SaadDev-01)

</div>
