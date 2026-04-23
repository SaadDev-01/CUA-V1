from setuptools import find_packages, setup

setup(
    name="cua-v1",
    version="0.3.2",
    description="A library for creating general purpose GUI agents using multimodal LLMs.",
    author="SaadDev-01",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "backoff",
        "pandas",
        "openai",
        "anthropic",
        "fastapi",
        "uvicorn",
        "together",
        "scikit-learn",
        "websockets",
        "tiktoken",
        "selenium",
        'pyobjc; platform_system == "Darwin"',
        "pyautogui",
        "toml",
        "pytesseract",
        "google-genai",
        'pywinauto; platform_system == "Windows"',  # Only for Windows
        'pywin32; platform_system == "Windows"',  # Only for Windows
    ],
    extras_require={"dev": ["black"]},  # Code formatter for linting
    entry_points={
        "console_scripts": [
            "cua_v1=gui_agents.cua_v1.cli_app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
    ],
    keywords="ai, llm, gui, agent, multimodal, automation, ollama, local-llm",
    project_urls={
        "Source": "https://github.com/SaadDev-01/CUA-V1",
        "Bug Reports": "https://github.com/SaadDev-01/CUA-V1/issues",
    },
    python_requires=">=3.9",
)
