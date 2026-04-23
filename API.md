# API Documentation

This document provides detailed API documentation for CUA-V1 components.

## Table of Contents

- [LLM Engine API](#llm-engine-api)
- [LLM Agent API](#llm-agent-api)
- [Agent API](#agent-api)
- [Grounding Agent API](#grounding-agent-api)
- [CLI API](#cli-api)

---

## LLM Engine API

### Base Class: `LMMEngine`

Abstract base class for all LLM engine implementations.

### Engine Implementations

#### `LMMEngineOpenAI`

OpenAI GPT model engine.

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

**Parameters:**
- `base_url` (str, optional): Custom API endpoint URL
- `api_key` (str, optional): OpenAI API key (defaults to `OPENAI_API_KEY` env var)
- `model` (str, required): Model name (e.g., "gpt-4o")
- `rate_limit` (int, optional): Requests per minute (-1 for no limit)
- `temperature` (float, optional): Sampling temperature
- `organization` (str, optional): OpenAI organization ID

**Methods:**

##### `generate(messages, temperature=0.0, max_new_tokens=None, **kwargs)`

Generate a response from the model.

**Parameters:**
- `messages` (list): List of message dictionaries
- `temperature` (float, optional): Sampling temperature
- `max_new_tokens` (int, optional): Maximum tokens to generate
- `**kwargs`: Additional parameters passed to API

**Returns:** str - Generated text response

**Raises:**
- `ValueError`: If API key is not provided
- `APIConnectionError`: If connection fails
- `APIError`: If API request fails
- `RateLimitError`: If rate limit exceeded

#### `LMMEngineAnthropic`

Anthropic Claude model engine with thinking mode support.

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

**Parameters:**
- `base_url` (str, optional): Custom API endpoint URL
- `api_key` (str, optional): Anthropic API key (defaults to `ANTHROPIC_API_KEY` env var)
- `model` (str, required): Model name (e.g., "claude-3-5-sonnet")
- `thinking` (bool, optional): Enable thinking mode
- `temperature` (float, optional): Sampling temperature

**Methods:**

##### `generate(messages, temperature=0.0, max_new_tokens=None, **kwargs)`

Generate a response from the model.

##### `generate_with_thinking(messages, temperature=0.0, max_new_tokens=None, **kwargs)`

Generate response with thinking tokens included.

**Returns:** str - Response with thinking tokens in `<thoughts>` tags

#### `LMMEngineGemini`

Google Gemini model engine.

**Constructor:**
```python
LMMEngineGemini(
    base_url: str = None,
    api_key: str = None,
    model: str = None,
    rate_limit: int = -1,
    temperature: float = None,
    **kwargs
)
```

**Parameters:**
- `base_url` (str, optional): Custom API endpoint URL (defaults to `GEMINI_ENDPOINT_URL` env var)
- `api_key` (str, optional): Google API key (defaults to `GEMINI_API_KEY` env var)
- `model` (str, required): Model name (e.g., "gemini-1.5-pro")
- `rate_limit` (int, optional): Requests per minute
- `temperature` (float, optional): Sampling temperature

#### `LMMEngineOllama`

Local model engine via Ollama.

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

**Parameters:**
- `base_url` (str, optional): Ollama endpoint URL (defaults to "http://localhost:11434/v1")
- `api_key` (str, optional): API key (defaults to "ollama", not required)
- `model` (str, required): Model name (e.g., "llama3.2")
- `rate_limit` (int, optional): Requests per minute
- `temperature` (float, optional): Sampling temperature

**Note:** Ollama does not require a real API key. Use "ollama" as placeholder.

#### Other Engines

Additional engines follow similar patterns:
- `LMMEngineOpenRouter` - OpenRouter aggregation
- `LMMEngineAzureOpenAI` - Azure OpenAI deployments
- `LMMEnginevLLM` - Self-hosted vLLM
- `LMMEngineHuggingFace` - HuggingFace Inference
- `LMMEngineParasail` - Parasail inference

---

## LLM Agent API

### Class: `LMMAgent`

High-level interface for LLM interactions.

**Constructor:**
```python
LMMAgent(
    engine_params: dict = None,
    system_prompt: str = None,
    engine: LMMEngine = None
)
```

**Parameters:**
- `engine_params` (dict, optional): Configuration for LLM engine
  - `engine_type` (str): Type of engine ("openai", "anthropic", "ollama", etc.)
  - `model` (str): Model name
  - `api_key` (str, optional): API key
  - Additional engine-specific parameters
- `system_prompt` (str, optional): System prompt for the agent
- `engine` (LMMEngine, optional): Pre-configured engine instance

**Methods:**

##### `add_system_prompt(system_prompt: str)`

Set or update the system prompt.

**Parameters:**
- `system_prompt` (str): System prompt text

##### `add_user_message(message: str, image: str = None)`

Add a user message to the conversation.

**Parameters:**
- `message` (str): User message text
- `image` (str, optional): Path to image file or image bytes

##### `add_assistant_message(message: str)`

Add an assistant response to the conversation.

**Parameters:**
- `message` (str): Assistant response text

##### `encode_image(image_content)`

Encode an image to base64.

**Parameters:**
- `image_content` (str or bytes): Image file path or bytes

**Returns:** str - Base64 encoded image

##### `reset()`

Reset the conversation history, keeping only the system prompt.

##### `generate(temperature: float = 0.0, max_new_tokens: int = None, **kwargs)`

Generate a response from the LLM.

**Parameters:**
- `temperature` (float, optional): Sampling temperature
- `max_new_tokens` (int, optional): Maximum tokens to generate
- `**kwargs`: Additional parameters

**Returns:** str - Generated response

**Example:**
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

---

## Agent API

### Class: `CUAV1`

Main agent class that orchestrates all sub-agents.

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

**Parameters:**
- `worker_engine_params` (dict): Configuration for worker LLM agent
- `grounding_agent` (ACI): Grounding agent instance
- `platform` (str, optional): Operating system ("windows", "darwin", "linux")
- `max_trajectory_length` (int): Maximum number of image turns to keep in history
- `enable_reflection` (bool): Enable reflection agent for action review

**Methods:**

##### `reset()`

Reset agent state and clear trajectory history.

##### `predict(instruction: str, observation: dict)`

Generate next action prediction.

**Parameters:**
- `instruction` (str): Natural language task instruction
- `observation` (dict): Current UI state observation
  - `screenshot` (str): Base64 encoded screenshot
  - Additional observation data

**Returns:** tuple - (agent_info, actions)
- `agent_info` (dict): Agent state information
- `actions` (list): List of action dictionaries

**Example:**
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

---

## Grounding Agent API

### Class: `OSWorldACI`

Grounding agent for UI element localization and interaction.

**Constructor:**
```python
OSWorldACI(
    engine_params: dict,
    platform: str = None,
    grounding_width: int = 1920,
    grounding_height: int = 1080
)
```

**Parameters:**
- `engine_params` (dict): Configuration for grounding LLM agent
- `platform` (str, optional): Operating system
- `grounding_width` (int): Screenshot width for grounding
- `grounding_height` (int): Screenshot height for grounding

**Methods:**

##### `get_ocr_elements(screenshot: str)`

Extract text elements from screenshot using OCR.

**Parameters:**
- `screenshot` (str): Base64 encoded screenshot

**Returns:** list - List of OCR text elements with coordinates

##### `generate_coords(instruction: str, screenshot: str)`

Generate coordinates for UI elements based on instruction.

**Parameters:**
- `instruction` (str): Description of element to locate
- `screenshot` (str): Base64 encoded screenshot

**Returns:** tuple - (x, y) coordinates

##### `click(x: int, y: int)`

Execute click action at coordinates.

**Parameters:**
- `x` (int): X coordinate
- `y` (int): Y coordinate

##### `type(text: str)`

Type text at current cursor position.

**Parameters:**
- `text` (str): Text to type

##### `scroll(direction: str, amount: int)`

Scroll in specified direction.

**Parameters:**
- `direction` (str): "up", "down", "left", or "right"
- `amount` (int): Number of scroll steps

---

## CLI API

### Command-Line Interface

The CLI provides a command-line interface for running CUA-V1.

**Usage:**
```bash
python -m gui_agents.cua_v1.cli_app [OPTIONS]
```

**Options:**

| Option | Description | Required |
|--------|-------------|----------|
| `--provider` | LLM provider (openai, anthropic, ollama, etc.) | No (default: openai) |
| `--model` | Model name | No |
| `--model_url` | Custom API endpoint URL | No |
| `--model_api_key` | API key for the model | No |
| `--ground_provider` | Grounding model provider | Yes |
| `--ground_url` | Grounding model API URL | Yes |
| `--ground_api_key` | Grounding model API key | No |
| `--ground_model` | Grounding model name | Yes |
| `--grounding_width` | Screenshot width | Yes |
| `--grounding_height` | Screenshot height | Yes |
| `--task` | Task description | No |
| `--enable_reflection` | Enable reflection agent | No |
| `--enable_local_env` | Enable local code execution | No |

**Example:**
```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.2 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.2 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "Open Chrome and search for AI"
```

### Signal Handling

The CLI supports pause/resume functionality:

- **Ctrl+C**: Pause workflow
- **Esc**: Resume workflow
- **Ctrl+C (again)**: Exit

---

## Error Handling

### Common Exceptions

#### `ValueError`

Raised when:
- Required parameters are missing
- Invalid engine type specified
- Invalid configuration

#### `APIConnectionError`

Raised when:
- Network connection fails
- API endpoint unreachable

#### `APIError`

Raised when:
- API request fails
- Invalid response received

#### `RateLimitError`

Raised when:
- API rate limit exceeded
- Too many requests

---

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key | For OpenAI provider |
| `ANTHROPIC_API_KEY` | Anthropic API key | For Anthropic provider |
| `GEMINI_API_KEY` | Google API key | For Gemini provider |
| `OPENROUTER_API_KEY` | OpenRouter API key | For OpenRouter provider |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | For Azure provider |
| `vLLM_API_KEY` | vLLM API key | For vLLM provider |
| `HF_TOKEN` | HuggingFace token | For HuggingFace provider |
| `PARASAIL_API_KEY` | Parasail API key | For Parasail provider |

---

## Examples

### Basic Usage

```python
from gui_agents.cua_v1.agents.agent import CUAV1
from gui_agents.cua_v1.agents.grounding import OSWorldACI

# Configure grounding agent
grounding_agent = OSWorldACI(
    engine_params={
        "engine_type": "openai",
        "model": "gpt-4o",
        "api_key": "your-api-key"
    },
    platform="windows"
)

# Configure main agent
agent = CUAV1(
    worker_engine_params={
        "engine_type": "openai",
        "model": "gpt-4o",
        "api_key": "your-api-key"
    },
    grounding_agent=grounding_agent,
    platform="windows"
)

# Execute task
agent_info, actions = agent.predict(
    instruction="Open Notepad and type Hello",
    observation={"screenshot": base64_screenshot}
)
```

### Using Local Models

```python
from gui_agents.cua_v1.agents.agent import CUAV1
from gui_agents.cua_v1.agents.grounding import OSWorldACI

# Use Ollama for local execution
grounding_agent = OSWorldACI(
    engine_params={
        "engine_type": "ollama",
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1"
    },
    platform="windows"
)

agent = CUAV1(
    worker_engine_params={
        "engine_type": "ollama",
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1"
    },
    grounding_agent=grounding_agent,
    platform="windows"
)
```

---

## Versioning

API version: 1.0.0

Breaking changes will be indicated by major version increments.
