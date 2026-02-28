# Agentic AI - Local LLM Agent

A simple CLI-based reasoning agent built using:

- Python
- LangChain
- Ollama (local LLM)
- TinyLlama model

## Features

- Structured reasoning output
- CLI interaction loop
- Fully local inference (no paid API)

## Architecture

CLI → LangChain → Ollama → Local Model

## Setup

1. Install Ollama
2. Pull model:
   ollama pull tinyllama
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python main.py