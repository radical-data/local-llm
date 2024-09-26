# Local LLM with Langchain, Ollama and Docker

A proof-of-concept for running large language models (LLMs) locally using Langchain, Ollama and Docker.

## Requirements

- Docker
- Docker Compose

## Quickstart

1. Build and run the services with Docker Compose: `docker compose up --build`
1. Create a `.env` file in the root of the project based on `.env.example`: `cp .env.example .env`.
1. (Optional) You can change the chosen model in the .env file. Refer to [Ollama's model library](https://ollama.com/library) for available models.
1. The service will be available at `http://localhost:8000/chain/playground` for interactive exploration, or you can invoke it via the API with the following example: `curl 'http://localhost:8000/chain/invoke' --data-raw '{"input":{"language":"spanish","text":"hi"}}'`

## API Endpoints

- `/chain/playground`: Provides an interactive UI to test the model.
- `/chain/invoke`: A REST API endpoint for programmatic interaction with the model.
