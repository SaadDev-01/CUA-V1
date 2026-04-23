# Architecture

This document provides a comprehensive overview of the CUA-V1 architecture, design decisions, and component interactions.

## Overview

CUA-V1 (Computer User Agent - Version 1) is a multi-agent system designed to automate graphical user interface (GUI) tasks using multimodal Large Language Models (LLMs). The system employs a sophisticated architecture that separates concerns across specialized agents, enabling robust and flexible GUI automation.

## System Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────┐
│                    CUA-V1 System                          │
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

## Core Components

### 1. LLM Engine Layer (`core/engine.py`)

The engine layer provides a unified interface for interacting with various LLM providers. Each engine implements the `LMMEngine` base class and handles provider-specific API interactions.

**Supported Engines:**
- `LMMEngineOpenAI` - OpenAI GPT models
- `LMMEngineAnthropic` - Anthropic Claude models (with thinking mode support)
- `LMMEngineGemini` - Google Gemini models
- `LMMEngineOpenRouter` - OpenRouter aggregation service
- `LMMEngineAzureOpenAI` - Azure OpenAI deployments
- `LMMEnginevLLM` - Self-hosted vLLM models
- `LMMEngineHuggingFace` - HuggingFace Inference Endpoints
- `LMMEngineParasail` - Parasail high-performance inference
- `LMMEngineOllama` - Local models via Ollama

**Key Features:**
- Automatic retry with exponential backoff
- Rate limiting support
- Custom base URL support
- Provider-specific optimizations (e.g., Anthropic thinking mode)

### 2. LLM Agent Layer (`core/mllm.py`)

The `LMMAgent` class serves as the primary interface for LLM interactions, abstracting away engine-specific details.

**Responsibilities:**
- Engine selection and initialization
- Message management (system prompts, user messages, images)
- Image encoding for multimodal inputs
- Message history management

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
```

### 3. Base Module (`core/module.py`)

The `BaseModule` class provides a foundation for creating specialized agent modules with shared LLM capabilities.

**Features:**
- Shared engine parameters
- Platform awareness
- Agent factory method

### 4. Agent Layer (`agents/`)

The agent layer contains the core automation logic, organized into specialized components.

#### 4.1 Grounding Agent (`agents/grounding.py`)

The grounding agent is responsible for:
- Visual understanding of GUI elements
- Precise coordinate generation for UI interactions
- OCR text extraction
- Element localization

**Key Classes:**
- `ACI` (Abstract Computer Interaction) - Base class for grounding
- `OSWorldACI` - Implementation for OSWorld-style environments

**Supported Actions:**
- `click` - Click on UI elements
- `type` - Type text into input fields
- `scroll` - Scroll through content
- `drag` - Drag and drop operations
- `wait` - Wait for elements to appear

#### 4.2 Worker Agent (`agents/worker.py`)

The worker agent is the primary planning and execution engine:
- Task decomposition
- Action sequence generation
- Trajectory management
- Integration with grounding agent

**Key Features:**
- Multi-step reasoning
- Context-aware decision making
- Error recovery
- Reflection integration

#### 4.3 Reflection Agent (`agents/worker.py`)

The reflection agent reviews and improves actions:
- Action validation
- Error analysis
- Alternative suggestion
- Performance optimization

#### 4.4 Code Agent (`agents/code_agent.py`)

The code agent handles complex tasks requiring programmatic execution:
- Python code generation
- Bash command generation
- Code execution in isolated environment
- Output parsing and validation

### 5. Main Agent (`agents/agent.py`)

The `CUAV1` class orchestrates all agents:
- Agent initialization
- Workflow coordination
- State management
- Trajectory tracking

**Configuration Options:**
- `max_trajectory_length` - Maximum history to maintain
- `enable_reflection` - Enable/disable reflection agent
- `platform` - Target operating system

### 6. CLI Application (`cli_app.py`)

The CLI application provides a command-line interface for running CUA-V1:
- Argument parsing
- Signal handling (pause/resume)
- Logging configuration
- Screenshot capture
- Task execution

**Key Features:**
- Debug mode with pause/resume
- Comprehensive logging
- Platform-specific optimizations
- Error handling

### 7. Utilities (`utils/`)

#### 7.1 Common Utilities (`utils/common_utils.py`)

Shared utility functions:
- Code generation helpers
- LLM call wrappers
- Response parsing
- Image compression

#### 7.2 Formatters (`utils/formatters.py`)

Response validation and formatting:
- Action format validation
- Code format validation
- Error message formatting

#### 7.3 Local Environment (`utils/local_env.py`)

Local code execution environment:
- Python code execution
- Bash command execution
- Output capture
- Error handling

### 8. Memory (`memory/`)

#### 8.1 Procedural Memory (`memory/procedural_memory.py`)

Prompt templates and procedural knowledge:
- System prompts for each agent
- Task-specific templates
- Formatting instructions
- Reflection prompts

## Data Flow

### Task Execution Flow

```
1. User provides task instruction
   ↓
2. CLI captures initial screenshot
   ↓
3. Grounding agent analyzes screenshot
   ↓
4. Worker agent plans action sequence
   ↓
5. Grounding agent generates coordinates
   ↓
6. Action is executed (click/type/scroll)
   ↓
7. New screenshot captured
   ↓
8. Reflection agent reviews action (if enabled)
   ↓
9. Process repeats until task complete
```

### Message Flow

```
User Task → CLI → CUAV1 → Worker Agent → LMMAgent → LLM Engine → Provider
                ↓
           Grounding Agent → LMMAgent → LLM Engine → Provider
                ↓
           Reflection Agent → LMMAgent → LLM Engine → Provider
                ↓
           Code Agent → LMMAgent → LLM Engine → Provider
```

## Design Decisions

### 1. Multi-Agent Architecture

**Rationale:** Separating concerns across specialized agents allows for:
- Modular development and testing
- Easy addition of new capabilities
- Independent optimization of each component
- Clear separation of responsibilities

### 2. Provider Agnostic Design

**Rationale:** Supporting multiple LLM providers enables:
- Flexibility in model selection
- Cost optimization
- Privacy control (local models)
- Redundancy and reliability

### 3. Dual-Model Architecture

**Rationale:** Using separate models for planning and grounding:
- Optimizes for different tasks (reasoning vs. visual understanding)
- Allows model selection based on task requirements
- Improves accuracy through specialization

### 4. Reflection System

**Rationale:** The reflection agent provides:
- Self-correction capabilities
- Error recovery
- Performance optimization
- Learning from mistakes

## Extension Points

### Adding New LLM Providers

1. Create new engine class in `core/engine.py`:
```python
class LMMEngineNewProvider(LMMEngine):
    def __init__(self, ...):
        # Initialize provider-specific client
        pass
    
    def generate(self, messages, ...):
        # Implement generation logic
        pass
```

2. Add import and mapping in `core/mllm.py`

3. Update CLI provider options in `cli_app.py`

### Adding New Actions

1. Add action method to `agents/grounding.py`:
```python
def new_action(self, ...):
    # Implement action logic
    pass
```

2. Update procedural memory with action template

3. Add to action space documentation

### Adding New Agent Types

1. Create new agent class in `agents/`
2. Inherit from appropriate base class
3. Integrate with `CUAV1` orchestrator
4. Add configuration options

## Performance Considerations

### Optimization Strategies

1. **Model Selection:** Use smaller models for simple tasks, larger for complex reasoning
2. **Caching:** Cache model responses for repeated queries
3. **Batching:** Batch multiple actions when possible
4. **Parallel Execution:** Run independent agents in parallel
5. **Local Models:** Use Ollama for privacy and cost savings

### Resource Management

- **Memory:** Limit trajectory length to manage memory usage
- **API Rate Limits:** Implement rate limiting and backoff
- **Screenshot Size:** Optimize screenshot resolution for performance
- **Code Execution:** Use isolated environments for safety

## Security Considerations

### Code Execution Safety

- Run code in isolated environments
- Validate generated code before execution
- Limit execution time and resources
- Sanitize outputs

### API Key Management

- Support environment variables
- Never log API keys
- Provide secure default behavior
- Document security best practices

### Privacy

- Support local-only execution via Ollama
- Allow users to control data flow
- Document data handling policies
- Provide privacy-focused configuration options

## Testing Strategy

### Unit Tests

- Test each engine independently
- Test agent logic in isolation
- Test utility functions
- Mock external dependencies

### Integration Tests

- Test agent interactions
- Test end-to-end workflows
- Test with real LLM providers
- Test across platforms

### Manual Testing

- Test real-world use cases
- Test error scenarios
- Test performance under load
- Test with different models

## Future Enhancements

### Planned Improvements

- Web browser-specific optimizations
- Visual task recording and replay
- Custom model fine-tuning
- Docker deployment
- Web dashboard
- Multi-monitor support
- Task scheduling

### Architectural Improvements

- Plugin system for extensions
- Configuration file support
- REST API for remote control
- Real-time streaming interface
- Distributed execution support

## Contributing

When contributing to the architecture:

1. Maintain separation of concerns
2. Follow existing patterns
3. Add appropriate documentation
4. Update this architecture document
5. Consider backward compatibility
6. Add tests for new components

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.
