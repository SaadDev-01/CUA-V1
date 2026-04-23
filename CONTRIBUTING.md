# Contributing to CUA-V1

Thank you for your interest in contributing to CUA-V1! We welcome contributions from everyone and appreciate your help in making this project better.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Environment details** (OS, Python version, model used)
- **Screenshots** or **logs** if applicable

### Suggesting Enhancements

We love feature suggestions! Please:

- Use a clear and descriptive title
- Provide a detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- Include examples if applicable

### Pull Requests

We welcome pull requests! Here's how to contribute:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Write clean, readable code
   - Add comments for complex logic
   - Follow existing code style
4. **Commit your changes**
   ```bash
   git commit -m "Add your feature description"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Ensure all checks pass

## 📋 Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Testing

- Test your changes thoroughly before submitting
- Ensure the CLI still works with your changes
- Test with different providers if applicable

### Documentation

- Update README.md if you add new features
- Update docstrings for modified functions
- Add examples for new functionality

## 🏗️ Project Structure

```
CUA-V1/
├── gui_agents/
│   └── cua_v1/
│       ├── agents/          # Agent implementations
│       ├── core/            # Core engine and LLM interfaces
│       ├── memory/          # Memory and prompts
│       ├── utils/           # Utility functions
│       └── cli_app.py       # CLI entry point
├── setup.py                 # Package configuration
├── requirements.txt         # Dependencies
├── README.md               # Main documentation
└── OLLAMA_SETUP.md         # Ollama setup guide
```

## 🎯 Areas for Contribution

We particularly welcome contributions in:

- **New provider support**: Add support for additional LLM providers
- **Model optimizations**: Improve performance for specific models
- **Documentation**: Improve guides, add examples
- **Bug fixes**: Help us squash bugs
- **Testing**: Add test coverage
- **Examples**: Create example use cases
- **Cross-platform**: Improve Windows/macOS/Linux compatibility

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

- `feat: Add support for new provider`
- `fix: Resolve memory leak in agent`
- `docs: Update README with new examples`
- `refactor: Simplify grounding logic`
- `test: Add tests for code agent`

## ⚖️ License

By contributing to CUA-V1, you agree that your contributions will be licensed under the Apache License 2.0.

## 🌟 Recognition

Contributors will be recognized in the project's contributors list. Your name will appear in:
- GitHub contributors list
- Release notes (for significant contributions)
- Documentation (for major contributions)

## 💬 Getting Help

If you need help contributing:

- Open a discussion on GitHub
- Ask questions in existing issues
- Check the documentation first

## 📧 Contact

For questions about contributions, please open a GitHub issue or discussion.

---

**Thank you for contributing to CUA-V1!** 🎉
