# Using CUA-V1 with Ollama (Local Models)

This guide helps you use CUA-V1 with free, local AI models through Ollama. No API keys or cloud services required!

## What is Ollama?

Ollama is a free tool that lets you run powerful AI models (like Llama 3, Mistral, etc.) directly on your computer. It's completely free and works offline.

## Quick Setup (5 minutes)

### Step 1: Install Ollama

**Windows:**
1. Download from https://ollama.com/download
2. Run the installer
3. Ollama will start automatically

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Download a Model

Open your terminal/command prompt and run:

```bash
# For a good balance of speed and intelligence (recommended)
ollama pull llama3.3

# For smaller/faster models (good for older computers)
ollama pull phi4

# For more capable models (requires more RAM)
ollama pull llama3.1
```

### Step 3: Verify Ollama is Running

```bash
ollama list
```

You should see the model you downloaded.

### Step 4: Run CUA-V1 with Ollama

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.3 \
    --ground_provider ollama \
    --ground_url http://localhost:11434/v1 \
    --ground_model llama3.3 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "your task here"
```

**That's it!** No API keys needed. Ollama handles everything locally.

## Recommended Models

| Model | Size | RAM Required | Speed | Best For |
|-------|------|-------------|-------|----------|
| `phi4` | ~2GB | 4GB | Fast | Older computers, quick tasks |
| `llama3.2` | ~2GB | 4GB | Fast | General use, balanced |
| `llama3.3` | ~4GB | 8GB | Medium | Best performance, complex tasks |
| `llama3.1` | ~4.5GB | 8GB | Medium | Legacy support |
| `mistral` | ~4GB | 8GB | Medium | Coding tasks |
| `deepseek` | ~8GB | 16GB | Slow | Advanced reasoning |

## Troubleshooting

**"Connection refused" error:**
- Make sure Ollama is running (check your system tray/taskbar)
- On Windows, the Ollama app should be running in the background
- Try restarting Ollama

**Slow performance:**
- Use a smaller model (try `phi4` instead of `llama3.3`)
- Close other applications to free up RAM
- Check if your computer meets the RAM requirements above

**Model not found:**
- Run `ollama pull <model-name>` to download it first
- Run `ollama list` to see available models

## Advanced: Using Different Ollama Endpoint

If Ollama is running on a different port or machine:

```bash
python -m gui_agents.cua_v1.cli_app \
    --provider ollama \
    --model llama3.3 \
    --model_url http://YOUR_IP:PORT/v1 \
    --ground_provider ollama \
    --ground_url http://YOUR_IP:PORT/v1 \
    --ground_model llama3.3 \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --task "your task here"
```

## Why Use Ollama?

- **Free**: No API costs, pay nothing
- **Private**: Your data never leaves your computer
- **Offline**: Works without internet
- **Easy**: No complex setup or API keys
- **Flexible**: Switch between many different models

## Need Help?

- Ollama documentation: https://github.com/ollama/ollama
- Available models: https://ollama.com/library
