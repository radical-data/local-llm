# Local LLM

## Quickstart

1. `docker compose up --build`
1. Can interact with at http://localhost:8000/chain/playground or by running

```
curl 'http://localhost:8000/chain/stream_log' --data-raw '{"input":{"language":"italian","text":"hi"}}'
```
