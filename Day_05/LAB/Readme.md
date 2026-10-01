# Agentic AI: Foundations and Open-Source Practice

## Day 5 Lab — Serving Models with Ollama and vLLM

This project explores local Large Language Model serving using **Ollama** and introduces **vLLM** for serving multiple requests efficiently.

The lab covers installing and comparing models, creating custom models using Modelfiles, calling the Ollama REST API directly, measuring inference performance, and understanding PagedAttention and continuous batching.

## Aim

The aim of this lab is to work directly with the Ollama server instead of relying only on a client library.

The experiment includes:

- Installing and running local models
- Inspecting model size, context length and licence
- Comparing two models
- Creating customized models using Modelfiles
- Calling Ollama REST API endpoints
- Measuring tokens per second and time to first token
- Understanding vLLM continuous batching

## Objectives

By completing this lab, the following concepts are demonstrated:

- Ollama CLI commands
- Local model management
- Model size and memory usage
- Context length
- Model licences
- Modelfiles
- System prompts and model parameters
- REST API communication
- Streaming responses
- OpenAI-compatible endpoints
- Time to First Token (TTFT)
- Tokens per second
- PagedAttention
- Continuous batching

## Technologies Used

- Python
- Ollama
- Requests
- OpenAI-compatible API
- vLLM
- Visual Studio Code

## Project Structure

```text
day_05/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── Modelfile
├── Modelfile.creative
│
├── api_demo.py
├── bench_models.py
│
├── ModelFile
└── README.md
