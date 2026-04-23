# CUA-V1 Software Specification Document

**Version:** 1.0.0  
**Date:** April 23, 2026  
**Status:** Active Development  
**License:** Apache 2.0

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Overview](#2-system-overview)
3. [Features & Capabilities](#3-features--capabilities)
4. [Architecture](#4-architecture)
5. [Component Details](#5-component-details)
6. [API Reference](#6-api-reference)
7. [Installation & Setup](#7-installation--setup)
8. [Usage Guide](#8-usage-guide)
9. [Configuration](#9-configuration)
10. [Development Guide](#10-development-guide)
11. [Roadmap & Future Enhancements](#11-roadmap--future-enhancements)
12. [Appendices](#12-appendices)

---

## 1. Executive Summary

### 1.1 Purpose

CUA-V1 (Computer User Agent - Version 1) is an advanced AI-powered GUI automation system that enables autonomous task execution on desktop environments. The system uses multimodal Large Language Models (LLMs) to understand visual interfaces and execute actions with human-like intelligence.

### 1.2 Target Audience

- **End Users:** Individuals seeking to automate repetitive GUI tasks
- **Developers:** Engineers building automation solutions or extending the system
- **Researchers:** AI/ML researchers studying agent-based systems
- **Enterprise:** Organizations requiring desktop automation solutions

### 1.3 Key Value Propositions

- **Privacy-First:** Run entirely locally with open-source models
- **Provider Agnostic:** Support for 10+ LLM providers
- **Cross-Platform:** Native Windows, macOS, and Linux support
- **Open Source:** Apache 2.0 licensed for full customization
- **Multi-Agent Architecture:** Sophisticated agent collaboration for complex tasks

---

## 2. System Overview

### 2.1 System Definition

CUA-V1 is a multi-agent system that automates GUI interactions through:
1. **Visual Understanding:** Analyzing screenshots to understand UI state
2. **Task Planning:** Decomposing high-level instructions into actionable steps
3. **Action Execution:** Performing clicks, typing, scrolling, and other UI actions
4. **Self-Correction:** Reviewing and optimizing actions for better performance

### 2.2 Core Components

```
┌─────────────────────────────────────────────────────────┐
│                    CUA-V1 System                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐      ┌──────────────┐                │
│  │   Worker     │◄────►│  Grounding   │                │
│  │   Agent      │      │    Agent     │                │
│  └──────────────┘      └──────────────┘                │
│         │                       │                       │
│         ▼                       ▼                       │
│  ┌──────────────┐      ┌──────────────┐                │
│  │  Reflection  │      │   Code       │                │
│  │   Agent      │      │   Agent      │                │
│  └──────────────┘      └──────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 2.3 Supported Platforms

- **Windows:** Windows 10/11 with pywinauto integration
- **macOS:** macOS 10.15+ with pyobjc integration
- **Linux:** Ubuntu 20.04+, Debian, and major distributions

### 2.4 Technology Stack

- **Language:** Python 3.9+
- **Core Dependencies:**
  - OpenAI/Anthropic/Google APIs for LLM access
  - pyautogui for UI automation
  - Pillow for image processing
  - backoff for retry logic
- **Local Models:** Ollama for privacy-focused execution

---

## 3. Features & Capabilities

### 3.1 Implemented Features

#### 3.1.1 Multi-Provider LLM Support

**Status:** ✅ Fully Implemented

The system supports 10+ LLM providers:

| Provider | Type | Status | Authentication |
|----------|------|--------|----------------|
| OpenAI | Cloud | ✅ Active | API Key |
| Anthropic | Cloud | ✅ Active | API Key |
| Google (Gemini) | Cloud | ✅ Active | API Key |
| xAI (Grok) | Cloud | ✅ Active | API Key |
| Mistral | Cloud | ✅ Active | API Key |
| OpenRouter | Aggregation | ✅ Active | API Key |
| Azure OpenAI | Enterprise | ✅ Active | API Key + Endpoint |
| HuggingFace | Cloud | ✅ Active | Token |
| vLLM | Self-hosted | ✅ Active | API Key |
| Parasail | Inference | ✅ Active | API Key |
| Ollama | Local | ✅ Active | None Required |

**How It Works:**
- Each provider implements the `LMMEngine` base class
- Unified interface through `LMMAgent` class
- Automatic retry with exponential backoff
- Rate limiting support
- Environment variable support for API keys

#### 3.1.2 Multi-Agent Architecture

**Status:** ✅ Fully Implemented

The system uses four specialized agents:

1. **Worker Agent**
   - **Purpose:** Task planning and execution orchestration
   - **Capabilities:**
     - Decomposes high-level instructions into steps
     - Manages action sequence execution
     - Maintains trajectory history
     - Integrates with grounding agent for UI interaction
   - **Implementation:** `gui_agents/cua_v1/agents/worker.py`

2. **Grounding Agent**
   - **Purpose:** Visual understanding and UI element localization
   - **Capabilities:**
     - Analyzes screenshots using OCR and vision models
     - Generates precise coordinates for UI elements
     - Executes UI actions (click, type, scroll, drag)
     - Identifies interactive elements (buttons, inputs, links)
   - **Implementation:** `gui_agents/cua_v1/agents/grounding.py`

3. **Reflection Agent**
   - **Purpose:** Action review and optimization
   - **Capabilities:**
     - Reviews executed actions for correctness
     - Suggests improvements when actions fail
     - Provides alternative approaches
     - Validates action outcomes
   - **Implementation:** Integrated in `worker.py`

4. **Code Agent**
   - **Purpose:** Programmatic task execution
   - **Capabilities:**
     - Generates Python code for complex operations
     - Executes Bash commands
     - Handles file operations
     - Runs in isolated environment
   - **Implementation:** `gui_agents/cua_v1/agents/code_agent.py`

**How It Works:**
```
User Task → Worker Agent (Planning)
                ↓
    Grounding Agent (Visual Analysis)
                ↓
    Action Execution (via pyautogui)
                ↓
    Reflection Agent (Review)
                ↓
    Next Action / Completion
```

#### 3.1.3 CLI Interface

**Status:** ✅ Fully Implemented

Command-line interface for running automation tasks:

**Features:**
- Argument parsing for all configuration options
- Signal handling (pause/resume with Ctrl+C)
- Comprehensive logging to `logs/` directory
- Screenshot capture and storage
- Platform-specific optimizations
- Debug mode with interactive pause

**Usage:**
```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Your task here"
```

**Implementation:** `gui_agents/cua_v1/cli_app.py`

#### 3.1.4 Local Model Support (Ollama)

**Status:** ✅ Fully Implemented

Privacy-focused execution using local models:

**Features:**
- No API keys required
- No data leaves local machine
- Works offline
- Supports multiple local models (Llama, Mistral, Phi, etc.)
- Default endpoint: `http://localhost:11434/v1`

**How It Works:**
1. Ollama runs as local server
2. CUA-V1 connects via OpenAI-compatible API
3. Models downloaded locally via `ollama pull`
4. Execution happens entirely on local hardware

**Setup:**
```bash
# Install Ollama
# Visit https://ollama.com/download

# Download a model
ollama pull llama3.2

# Run CUA-V1 with Ollama
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    ...
```

#### 3.1.5 Cross-Platform Support

**Status:** ✅ Fully Implemented

Native support for Windows, macOS, and Linux:

**Windows:**
- Uses pywinauto for Windows-specific controls
- pywin32 for Windows API access
- Platform detection via `platform.system()`

**macOS:**
- Uses pyobjc for macOS integration
- AppleScript support for native actions
- Platform detection via `platform.system()`

**Linux:**
- Uses X11/Wayland compatible methods
- xdotool integration where available
- Platform detection via `platform.system()`

**Universal Components:**
- pyautogui for mouse/keyboard control (all platforms)
- PIL/Pillow for screenshots (all platforms)
- Platform-specific code isolated in conditional imports

#### 3.1.6 Reflection System

**Status:** ✅ Fully Implemented

Self-improving agent that reviews actions:

**How It Works:**
1. After each action, reflection agent analyzes outcome
2. Compares expected vs actual result
3. Identifies errors or inefficiencies
4. Suggests corrections or alternative approaches
5. Worker agent incorporates feedback

**Configuration:**
- Enable via `--enable_reflection` flag
- Adjustable via `enable_reflection` parameter in `CUAV1` class

#### 3.1.7 Code Execution Environment

**Status:** ✅ Fully Implemented

Isolated environment for running generated code:

**Features:**
- Python code execution
- Bash command execution
- Output capture and parsing
- Error handling and recovery
- Sandboxed execution (limited by user permissions)

**Use Cases:**
- Complex file operations
- Data processing
- System configuration
- Multi-step programmatic tasks

**Implementation:** `gui_agents/cua_v1/utils/local_env.py`

#### 3.1.8 Logging & Debugging

**Status:** ✅ Fully Implemented

Comprehensive logging system:

**Features:**
- Timed log files in `logs/` directory
- Multiple log levels (DEBUG, INFO, WARNING, ERROR)
- Screenshot capture for debugging
- Action history tracking
- Error tracing

**Log Format:**
```
normal-YYYYMMDD@HHMMSS.log
```

### 3.2 Feature Interaction Matrix

| Feature | Worker | Grounding | Reflection | Code Agent |
|---------|--------|-----------|------------|------------|
| Task Planning | ✅ | ❌ | ✅ | ❌ |
| Visual Analysis | ❌ | ✅ | ✅ | ❌ |
| UI Actions | ❌ | ✅ | ✅ | ❌ |
| Code Execution | ❌ | ❌ | ❌ | ✅ |
| Error Recovery | ✅ | ❌ | ✅ | ✅ |
| Self-Correction | ✅ | ❌ | ✅ | ❌ |

### 3.3 Feature Limitations

**Current Limitations:**
1. **Mobile Apps:** No iOS/Android automation support
2. **Web-Specific:** Limited browser-specific optimizations
3. **Multi-Monitor:** Single monitor support only
4. **Scheduling:** No built-in task scheduling
5. **Recording:** No visual task recording/replay
6. **Tests:** Limited test coverage

**Planned Improvements:**
- See [Roadmap & Future Enhancements](#11-roadmap--future-enhancements)

---

## 4. Architecture

### 4.1 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         CUA-V1 System                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                     CLI Layer                                │ │
│  │  (Argument Parsing, Signal Handling, Logging)               │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              │                                    │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                   Main Agent (CUAV1)                         │ │
│  │  (Orchestration, State Management, Trajectory Tracking)     │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              │                                    │
│        ┌─────────────────────┼─────────────────────┐           │
│        ▼                     ▼                     ▼           │
│  ┌──────────┐         ┌──────────┐         ┌──────────┐       │
│  │  Worker  │◄───────►│ Grounding│◄───────►│  Code    │       │
│  │  Agent   │         │  Agent   │         │  Agent   │       │
│  └──────────┘         └──────────┘         └──────────┘       │
│        │                     │                     │           │
│        │              ┌──────┴──────┐              │           │
│        │              ▼             ▼              │           │
│        │         ┌────────┐   ┌────────┐          │           │
│        └────────►│Reflection│   │  OCR   │◄─────────┘           │
│                  │  Agent   │   │ Engine │                      │
│                  └────────┘   └────────┘                      │
│                              │                                    │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                     LLM Engine Layer                         │ │
│  │  (OpenAI, Anthropic, Google, Ollama, etc.)                   │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              │                                    │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                  UI Automation Layer                         │ │
│  │  (pyautogui, pywinauto, pyobjc, screenshots)               │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Data Flow

#### 4.2.1 Task Execution Flow

```
1. User Input
   └── CLI receives task instruction
   
2. Initialization
   ├── Load configuration
   ├── Initialize agents
   └── Capture initial screenshot
   
3. Planning Phase (Worker Agent)
   ├── Analyze current state
   ├── Decompose task into steps
   └── Generate action plan
   
4. Execution Phase (Grounding Agent)
   ├── Analyze screenshot
   ├── Locate UI elements
   ├── Generate coordinates
   └── Execute action (click/type/scroll)
   
5. Verification Phase (Reflection Agent)
   ├── Capture new screenshot
   ├── Verify action success
   └── Identify errors if any
   
6. Iteration
   ├── If not complete: Go to step 3
   └── If complete: Return results
```

#### 4.2.2 Message Flow

```
User Task
    │
    ▼
CLI Interface
    │
    ▼
CUAV1 (Main Agent)
    │
    ├─────────────────┬─────────────────┐
    ▼                 ▼                 ▼
Worker Agent    Grounding Agent   Code Agent
    │                 │                 │
    ▼                 ▼                 ▼
LMMAgent        LMMAgent          LMMAgent
    │                 │                 │
    ▼                 ▼                 ▼
LLM Engine      LLM Engine        LLM Engine
(OpenAI/etc.)   (OpenAI/etc.)     (OpenAI/etc.)
    │                 │                 │
    ▼                 ▼                 ▼
UI Actions      UI Actions        Code Execution
(pyautogui)     (pyautogui)       (local_env)
```

### 4.3 Component Interaction

| Component | Interacts With | Purpose |
|-----------|---------------|---------|
| CLI | CUAV1, OS | Entry point and configuration |
| CUAV1 | All Agents | Orchestration and state management |
| Worker | Grounding, Reflection | Task planning and execution |
| Grounding | Worker, LLM Engine | Visual analysis and UI actions |
| Reflection | Worker, Grounding | Action review and optimization |
| Code Agent | CUAV1, Local Env | Programmatic task execution |
| LLM Engine | All Agents | Language model inference |
| Local Env | Code Agent | Code execution sandbox |

---

## 5. Component Details

### 5.1 Core Engine Layer

#### 5.1.1 Base Engine (`LMMEngine`)

**File:** `gui_agents/cua_v1/core/engine.py`

**Purpose:** Abstract base class for all LLM engine implementations.

**Methods:**
- `generate(messages, temperature, max_new_tokens, **kwargs)` - Generate response

#### 5.1.2 Engine Implementations

All engines inherit from `LMMEngine` and implement provider-specific logic:

**Common Features:**
- Automatic retry with exponential backoff (max 60 seconds)
- Rate limiting support
- Environment variable API key support
- Custom base URL support

**Engine List:**
1. `LMMEngineOpenAI` - OpenAI GPT models
2. `LMMEngineAnthropic` - Claude models with thinking support
3. `LMMEngineGemini` - Google Gemini models
4. `LMMEngineOpenRouter` - OpenRouter aggregation
5. `LMMEngineAzureOpenAI` - Azure OpenAI deployments
6. `LMMEnginevLLM` - Self-hosted vLLM
7. `LMMEngineHuggingFace` - HuggingFace Inference
8. `LMMEngineParasail` - Parasail inference
9. `LMMEngineOllama` - Local Ollama models

#### 5.1.3 LLM Agent (`LMMAgent`)

**File:** `gui_agents/cua_v1/core/mllm.py`

**Purpose:** High-level interface for LLM interactions.

**Key Methods:**
- `__init__(engine_params, system_prompt, engine)` - Initialize agent
- `add_user_message(message, image)` - Add user message
- `add_assistant_message(message)` - Add assistant response
- `generate(temperature, max_new_tokens, **kwargs)` - Generate response
- `encode_image(image_content)` - Encode image to base64
- `reset()` - Reset conversation history

**Usage Example:**
```python
from gui_agents.cua_v1.core.mllm import LMMAgent

agent = LMMAgent(
    engine_params={
        "engine_type": "openai",
        "model": "gpt-4o",
        "api_key": "your-api-key"
    },
    system_prompt="You are a helpful assistant."
)

response = agent.generate(temperature=0.7)
```

#### 5.1.4 Base Module (`BaseModule`)

**File:** `gui_agents/cua_v1/core/module.py`

**Purpose:** Foundation for creating specialized agent modules.

**Features:**
- Shared engine parameters
- Platform awareness
- Agent factory method (`_create_agent()`)

### 5.2 Agent Layer

#### 5.2.1 Main Agent (`CUAV1`)

**File:** `gui_agents/cua_v1/agents/agent.py`

**Purpose:** Orchestrates all sub-agents and manages workflow.

**Configuration Options:**
- `worker_engine_params` - Worker agent LLM configuration
- `grounding_agent` - Grounding agent instance
- `platform` - Operating system ("windows", "darwin", "linux")
- `max_trajectory_length` - History size limit (default: 8)
- `enable_reflection` - Enable reflection agent (default: True)

**Key Methods:**
- `reset()` - Reset agent state
- `predict(instruction, observation)` - Execute task and return actions

**Usage Example:**
```python
from gui_agents.cua_v1.agents.agent import CUAV1
from gui_agents.cua_v1.agents.grounding import OSWorldACI

grounding_agent = OSWorldACI(
    engine_params={...},
    platform="windows"
)

agent = CUAV1(
    worker_engine_params={...},
    grounding_agent=grounding_agent,
    platform="windows",
    enable_reflection=True
)

agent_info, actions = agent.predict(
    instruction="Open Chrome and search for AI",
    observation={"screenshot": base64_screenshot}
)
```

#### 5.2.2 Grounding Agent (`OSWorldACI`)

**File:** `gui_agents/cua_v1/agents/grounding.py`

**Purpose:** Visual understanding and UI element interaction.

**Key Capabilities:**
- OCR text extraction from screenshots
- UI element localization
- Coordinate generation for actions
- Action execution (click, type, scroll, drag)

**Supported Actions:**
- `click(x, y)` - Click at coordinates
- `type(text)` - Type text
- `scroll(direction, amount)` - Scroll
- `drag(start, end)` - Drag and drop
- `wait()` - Wait for element
- `get_ocr_elements(screenshot)` - Extract text
- `generate_coords(instruction, screenshot)` - Get coordinates

**Usage Example:**
```python
from gui_agents.cua_v1.agents.grounding import OSWorldACI

aci = OSWorldACI(
    engine_params={...},
    platform="windows",
    grounding_width=1920,
    grounding_height=1080
)

# Get OCR elements
elements = aci.get_ocr_elements(screenshot)

# Generate coordinates
x, y = aci.generate_coords("Click the Submit button", screenshot)

# Execute action
aci.click(x, y)
```

#### 5.2.3 Worker Agent (`Worker`)

**File:** `gui_agents/cua_v1/agents/worker.py`

**Purpose:** Task planning and execution orchestration.

**Key Capabilities:**
- Task decomposition
- Action sequence generation
- Trajectory management
- Reflection integration
- Context-aware decision making

**Key Methods:**
- `__init__(worker_engine_params, grounding_agent, platform, ...)`
- `reset()` - Reset state
- `predict(task, current_screenshot, ...)` - Generate next action

**Configuration:**
- `worker_engine_params` - LLM configuration
- `grounding_agent` - Grounding agent instance
- `platform` - Operating system
- `max_trajectory_length` - History limit
- `enable_reflection` - Enable reflection

#### 5.2.4 Code Agent (`CodeAgent`)

**File:** `gui_agents/cua_v1/agents/code_agent.py`

**Purpose:** Programmatic task execution.

**Key Capabilities:**
- Python code generation
- Bash command generation
- Code execution in isolated environment
- Output parsing
- Error handling

**Use Cases:**
- Complex file operations
- Data processing
- System configuration
- Multi-step programmatic tasks

### 5.3 CLI Layer

**File:** `gui_agents/cua_v1/cli_app.py`

**Purpose:** Command-line interface for running CUA-V1.

**Features:**
- Comprehensive argument parsing
- Signal handling (pause/resume with Ctrl+C)
- Logging configuration
- Screenshot capture
- Platform detection

**Command-Line Options:**

| Option | Description | Required | Default |
|--------|-------------|----------|---------|
| `--provider` | LLM provider | No | openai |
| `--model` | Model name | No | gpt-4o |
| `--model_url` | Custom API URL | No | - |
| `--model_api_key` | API key | No | env var |
| `--ground_provider` | Grounding provider | Yes | - |
| `--ground_url` | Grounding API URL | Yes | - |
| `--ground_api_key` | Grounding API key | No | env var |
| `--ground_model` | Grounding model | Yes | - |
| `--grounding_width` | Screenshot width | Yes | - |
| `--grounding_height` | Screenshot height | Yes | - |
| `--task` | Task description | No | - |
| `--enable_reflection` | Enable reflection | No | False |
| `--enable_local_env` | Enable code execution | No | False |

**Signal Handling:**
- **Ctrl+C:** Pause workflow
- **Esc:** Resume workflow
- **Ctrl+C (again):** Exit

### 5.4 Utility Layer

#### 5.4.1 Common Utilities (`common_utils.py`)

**File:** `gui_agents/cua_v1/utils/common_utils.py`

**Purpose:** Shared utility functions.

**Functions:**
- Code generation helpers
- LLM call wrappers
- Response parsing
- Image compression

#### 5.4.2 Formatters (`formatters.py`)

**File:** `gui_agents/cua_v1/utils/formatters.py`

**Purpose:** Response validation and formatting.

**Functions:**
- Action format validation
- Code format validation
- Error message formatting

#### 5.4.3 Local Environment (`local_env.py`)

**File:** `gui_agents/cua_v1/utils/local_env.py`

**Purpose:** Local code execution environment.

**Features:**
- Python code execution
- Bash command execution
- Output capture
- Error handling

---

## 6. API Reference

### 6.1 Engine API

#### `LMMEngineOpenAI`

**Constructor:**
```python
LMMEngineOpenAI(
    base_url: str = None,
    api_key: str = None,
    model: str = None,
    rate_limit: int = -1,
    temperature: float = None,
    organization: str = None,
    **kwargs
)
```

**Methods:**
- `generate(messages, temperature=0.0, max_new_tokens=None, **kwargs)` → str

#### `LMMEngineAnthropic`

**Constructor:**
```python
LMMEngineAnthropic(
    base_url: str = None,
    api_key: str = None,
    model: str = None,
    thinking: bool = False,
    temperature: float = None,
    **kwargs
)
```

**Methods:**
- `generate(messages, temperature=0.0, max_new_tokens=None, **kwargs)` → str
- `generate_with_thinking(messages, ...)` → str (with thoughts)

#### `LMMEngineOllama`

**Constructor:**
```python
LMMEngineOllama(
    base_url: str = None,
    api_key: str = None,
    model: str = None,
    rate_limit: int = -1,
    temperature: float = None,
    **kwargs
)
```

**Note:** API key defaults to "ollama" (placeholder, not required)

### 6.2 Agent API

#### `LMMAgent`

**Constructor:**
```python
LMMAgent(
    engine_params: dict = None,
    system_prompt: str = None,
    engine: LMMEngine = None
)
```

**Methods:**
- `add_system_prompt(system_prompt)` - Set system prompt
- `add_user_message(message, image=None)` - Add user message
- `add_assistant_message(message)` - Add assistant response
- `encode_image(image_content)` → str - Encode image
- `reset()` - Reset conversation
- `generate(temperature=0.0, max_new_tokens=None, **kwargs)` → str

#### `CUAV1`

**Constructor:**
```python
CUAV1(
    worker_engine_params: dict,
    grounding_agent: ACI,
    platform: str = None,
    max_trajectory_length: int = 8,
    enable_reflection: bool = True
)
```

**Methods:**
- `reset()` - Reset agent state
- `predict(instruction: str, observation: dict)` → tuple (agent_info, actions)

#### `OSWorldACI`

**Constructor:**
```python
OSWorldACI(
    engine_params: dict,
    platform: str = None,
    grounding_width: int = 1920,
    grounding_height: int = 1080
)
```

**Methods:**
- `get_ocr_elements(screenshot)` → list
- `generate_coords(instruction, screenshot)` → tuple (x, y)
- `click(x, y)`
- `type(text)`
- `scroll(direction, amount)`

### 6.3 Environment Variables

| Variable | Description | Used By |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | OpenAI provider |
| `ANTHROPIC_API_KEY` | Anthropic API key | Anthropic provider |
| `GEMINI_API_KEY` | Google API key | Gemini provider |
| `OPENROUTER_API_KEY` | OpenRouter API key | OpenRouter provider |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | Azure provider |
| `vLLM_API_KEY` | vLLM API key | vLLM provider |
| `HF_TOKEN` | HuggingFace token | HuggingFace provider |
| `PARASAIL_API_KEY` | Parasail API key | Parasail provider |

---

## 7. Installation & Setup

### 7.1 Prerequisites

- **Python:** 3.9 or higher
- **Operating System:** Windows 10/11, macOS 10.15+, or Linux
- **RAM:** Minimum 4GB (8GB+ recommended for local models)
- **Storage:** 2GB+ free space (more for local models)

### 7.2 Installation Steps

#### 7.2.1 Install from Source

```bash
# Clone the repository
git clone https://github.com/SaadDev-01/CUA-V1.git
cd CUA-V1

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Verify installation
python -m gui_agents.cua_v1.cli_app --help
```

#### 7.2.2 Install Ollama (Optional, for Local Models)

**Windows:**
1. Download from https://ollama.com/download
2. Run the installer
3. Ollama starts automatically

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Download a Model:**
```bash
ollama pull llama3.2
```

#### 7.2.3 Configure API Keys (for Cloud Providers)

**Option 1: Environment Variables (Recommended)**
```bash
# Windows
set OPENAI_API_KEY=your-api-key

# macOS/Linux
export OPENAI_API_KEY=your-api-key
```

**Option 2: Command Line**
```bash
python -m gui_agents.cua_v1.cli_app \
    --model_api_key your-api-key \
    ...
```

### 7.3 Verification

```bash
# Test CLI
python -m gui_agents.cua_v1.cli_app --help

# Test with Ollama (no API key needed)
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Open Notepad"
```

---

## 8. Usage Guide

### 8.1 Basic Usage

#### 8.1.1 Using Local Models (Ollama)

```bash
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

#### 8.1.2 Using Cloud Models (OpenAI)

```bash
export OPENAI_API_KEY=your-api-key

python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Your task here"
```

#### 8.1.3 Using Different Models for Worker and Grounding

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Your task here"
```

### 8.2 Advanced Usage

#### 8.2.1 Enable Reflection

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key $OPENAI_API_KEY \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_reflection \
    --task "Complex multi-step task"
```

#### 8.2.2 Enable Local Code Execution

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key $OPENAI_API_KEY \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_local_env \
    --task "Create a Python script that calculates fibonacci numbers"
```

### 8.3 Common Tasks

#### 8.3.1 Web Automation

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

#### 8.3.2 Desktop Application Automation

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

#### 8.3.3 File Operations

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider openai \
    --model gpt-4o \
    --ground_provider openai \
    --ground_url https://api.openai.com/v1 \
    --ground_api_key $OPENAI_API_KEY \
    --ground_model gpt-4o \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_local_env \
    --task "Create a folder called 'Project' on the Desktop and create 3 text files inside it"
```

### 8.4 Interactive Mode

The CLI supports interactive pause/resume:

1. **Press Ctrl+C** during execution to pause
2. **Press Esc** to resume
3. **Press Ctrl+C again** to exit

---

## 9. Configuration

### 9.1 Configuration Options

#### 9.1.1 Engine Parameters

Common parameters for all engines:

```python
engine_params = {
    "engine_type": "openai",  # or "anthropic", "ollama", etc.
    "model": "gpt-4o",
    "api_key": "your-api-key",  # or use env var
    "base_url": "https://api.openai.com/v1",  # optional
    "rate_limit": -1,  # -1 for no limit
    "temperature": 0.0,  # 0.0 to 1.0
}
```

#### 9.1.2 Agent Configuration

```python
agent_config = {
    "worker_engine_params": {
        "engine_type": "openai",
        "model": "gpt-4o",
        "api_key": "your-api-key"
    },
    "grounding_engine_params": {
        "engine_type": "ollama",
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1"
    },
    "platform": "windows",  # or "darwin", "linux"
    "max_trajectory_length": 8,
    "enable_reflection": True
}
```

### 9.2 Environment Configuration

#### 9.2.1 Windows

```powershell
# Set environment variables
$env:OPENAI_API_KEY = "your-api-key"
$env:PYTHONPATH = "C:\\path\\to\\CUA-V1"

# Run
python -m gui_agents.cua_v1.cli_app ...
```

#### 9.2.2 macOS/Linux

```bash
# Set environment variables
export OPENAI_API_KEY="your-api-key"
export PYTHONPATH="/path/to/CUA-V1"

# Run
python -m gui_agents.cua_v1.cli_app ...
```

### 9.3 Logging Configuration

Logs are automatically saved to `logs/` directory with timestamp:

```
logs/
└── normal-20260423@154732.log
```

**Log Levels:**
- DEBUG: Detailed debugging information
- INFO: General execution information
- WARNING: Non-critical issues
- ERROR: Critical errors

---

## 10. Development Guide

### 10.1 Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/SaadDev-01/CUA-V1.git
cd CUA-V1

# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Install development tools
pip install black flake8 pytest
```

### 10.2 Project Structure

```
CUA-V1/
├── gui_agents/
│   └── cua_v1/
│       ├── agents/          # Agent implementations
│       │   ├── agent.py     # Main CUAV1 agent
│       │   ├── worker.py    # Worker agent
│       │   ├── grounding.py  # Grounding agent
│       │   └── code_agent.py # Code agent
│       ├── core/            # Core engine and LLM interfaces
│       │   ├── engine.py    # LLM engine implementations
│       │   ├── mllm.py      # LLM agent interface
│       │   └── module.py    # Base module
│       ├── memory/          # Memory and prompts
│       ├── utils/           # Utility functions
│       │   ├── common_utils.py
│       │   ├── formatters.py
│       │   └── local_env.py
│       └── cli_app.py       # CLI entry point
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
├── README.md               # Main documentation
├── SOFTWARE_SPECIFICATION.md  # This document
├── ARCHITECTURE.md         # System architecture
├── API.md                  # API reference
├── OLLAMA_SETUP.md         # Ollama setup guide
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Community standards
└── LICENSE                 # Apache 2.0 license
```

### 10.3 Adding New LLM Providers

1. **Create Engine Class** in `core/engine.py`:

```python
class LMMEngineNewProvider(LMMEngine):
    def __init__(self, base_url=None, api_key=None, model=None, **kwargs):
        assert model is not None, "model must be provided"
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.llm_client = None
    
    @backoff.on_exception(
        backoff.expo, (APIConnectionError, APIError, RateLimitError), max_time=60
    )
    def generate(self, messages, temperature=0.0, max_new_tokens=None, **kwargs):
        api_key = self.api_key or os.getenv("NEWPROVIDER_API_KEY")
        if api_key is None:
            raise ValueError("API key required")
        
        # Initialize client if not already done
        if not self.llm_client:
            self.llm_client = NewProviderClient(api_key=api_key)
        
        # Make API call
        response = self.llm_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            **kwargs
        )
        
        return response.choices[0].message.content
```

2. **Add to LMMAgent** in `core/mllm.py`:

```python
elif engine_type == "new_provider":
    from gui_agents.cua_v1.core.engine import LMMEngineNewProvider
    self.engine = LMMEngineNewProvider(**engine_params)
```

3. **Update CLI** in `cli_app.py`:

Add to help text and validation.

4. **Update Documentation**:
- Add to SOFTWARE_SPECIFICATION.md
- Update API.md
- Update README.md

### 10.4 Adding New Actions

1. **Add to Grounding Agent** in `agents/grounding.py`:

```python
def new_action(self, param1, param2):
    """
    Perform new action.
    
    Args:
        param1: Description
        param2: Description
    """
    # Implementation
    pass
```

2. **Update Procedural Memory** in `memory/procedural_memory.py`:

Add prompt template for new action.

3. **Update Documentation**:
- Add to SOFTWARE_SPECIFICATION.md
- Update API.md

### 10.5 Testing

#### 10.5.1 Manual Testing

```bash
# Test with Ollama (no API costs)
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Simple test task"
```

#### 10.5.2 Code Quality

```bash
# Format code
black gui_agents/

# Lint
flake8 gui_agents/
```

---

## 11. Roadmap & Future Enhancements

### 11.1 Planned Features

| Feature | Priority | Status | Description |
|---------|----------|--------|-------------|
| Web Browser Optimization | High | Planned | Chrome/Firefox/Edge specific optimizations |
| Visual Task Recording | High | Planned | Record and replay user actions |
| Model Fine-tuning | Medium | Planned | Custom model training guide |
| Docker Deployment | Medium | Planned | One-command containerized deployment |
| Web Dashboard | Medium | Planned | Browser-based task management UI |
| Multi-Monitor Support | Low | Planned | Support for multiple displays |
| Task Scheduling | Low | Planned | Cron-like task scheduling |

### 11.2 Technical Debt

| Item | Priority | Description |
|------|----------|-------------|
| Test Coverage | High | Add comprehensive unit and integration tests |
| Error Handling | Medium | Improve error messages and recovery |
| Documentation | Medium | Add more code examples and tutorials |
| Performance | Low | Optimize for faster execution |

### 11.3 Long-term Vision

- **Plugin System:** Allow third-party extensions
- **REST API:** HTTP API for remote control
- **Real-time Streaming:** WebSocket support for live updates
- **Distributed Execution:** Multi-machine task execution
- **Mobile Support:** Android/iOS automation (not planned - removed from roadmap)

---

## 12. Appendices

### 12.1 Glossary

| Term | Definition |
|------|------------|
| **Agent** | Autonomous component that performs specific tasks |
| **Grounding** | Converting high-level instructions to concrete UI actions |
| **LLM** | Large Language Model (e.g., GPT-4, Claude) |
| **LMM** | Large Multimodal Model (vision + language) |
| **OCR** | Optical Character Recognition |
| **Reflection** | Self-review and optimization of actions |
| **Trajectory** | History of states and actions |
| **UI** | User Interface |

### 12.2 Error Codes

| Error | Description | Solution |
|-------|-------------|----------|
| `Connection refused` | Ollama not running | Start Ollama service |
| `API key not found` | Missing API key | Set environment variable or use `--api_key` |
| `Model not found` | Model not downloaded | Run `ollama pull <model>` |
| `ModuleNotFoundError` | Package not installed | Run `pip install -e .` |
| `RateLimitError` | Too many requests | Wait or increase rate limit |

### 12.3 Troubleshooting Guide

#### 12.3.1 Common Issues

**Issue:** "Connection refused" with Ollama
- **Cause:** Ollama not running
- **Solution:** Start Ollama from system tray or terminal

**Issue:** Slow performance
- **Cause:** Large model on limited hardware
- **Solution:** Use smaller model (e.g., `phi4` instead of `llama3.3`)

**Issue:** Actions not working
- **Cause:** Incorrect coordinates or UI changes
- **Solution:** Enable reflection or check screenshot resolution

**Issue:** Import errors
- **Cause:** Package not installed properly
- **Solution:** Reinstall with `pip install -e .`

### 12.4 Changelog

**Version 0.3.2 (2026-04-23)**
- Initial release with comprehensive documentation
- Multi-provider LLM support (10+ providers)
- Multi-agent architecture
- CLI interface
- Ollama local model support
- Cross-platform support (Windows, macOS, Linux)
- Reflection system
- Code execution environment
- Comprehensive documentation suite

### 12.5 References

- **Repository:** https://github.com/SaadDev-01/CUA-V1
- **License:** Apache 2.0
- **Python:** 3.9+
- **Ollama:** https://ollama.com
- **OpenAI:** https://openai.com
- **Anthropic:** https://anthropic.com

### 12.6 Contact & Support

- **Issues:** https://github.com/SaadDev-01/CUA-V1/issues
- **Discussions:** https://github.com/SaadDev-01/CUA-V1/discussions
- **Contributing:** See CONTRIBUTING.md

---

**Document End**

*This software specification document provides comprehensive information about CUA-V1. For the latest updates, refer to the repository at https://github.com/SaadDev-01/CUA-V1*
