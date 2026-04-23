# Changelog

All notable changes to CUA-V1 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive architecture documentation (ARCHITECTURE.md)
- Detailed API documentation (API.md)
- Contribution guidelines (CONTRIBUTING.md)
- Code of conduct (CODE_OF_CONDUCT.md)
- Apache 2.0 license (LICENSE)
- Ollama local model support
- Multi-provider LLM support (OpenAI, Anthropic, Google, xAI, Mistral, OpenRouter, Azure, HuggingFace, vLLM, Parasail)
- Multi-agent architecture (Worker, Grounding, Reflection, Code agents)
- CLI interface with pause/resume functionality
- Cross-platform support (Windows, macOS, Linux)
- Reflection system for action optimization
- Local code execution environment

### Changed
- Fixed duplicate import in engine.py
- Updated README with professional structure
- Enhanced contribution messaging
- Removed mobile app automation from roadmap

### Fixed
- Duplicate AzureOpenAI import in engine.py

## [0.3.2] - 2026-04-23

### Added
- Initial release of CUA-V1
- Multi-agent GUI automation system
- Support for multiple LLM providers
- CLI application
- Grounding agent for UI element localization
- Worker agent for task planning
- Reflection agent for action review
- Code agent for programmatic execution
