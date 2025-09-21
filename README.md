# Flask + Redis Counter

A Flask app that increments a counter on each page load and stores the value in Redis. The stack runs with Docker Compose.

## Requirements
- Docker
- Docker Compose

## Quick start
```bash
docker compose up --build
# Browser: http://localhost:5000
```

## Verification
```bash
# App responds
curl -s http://localhost:5000 | head

# Services are up
docker compose ps

# Redis health (runs inside the redis container)
docker compose exec redis redis-cli ping

# Counter value stored in Redis
docker compose exec redis redis-cli get page_counter
```

## (Optional) Network sanity from the web container
```bash
docker compose exec web sh -lc "getent hosts redis && nc -zv redis 6379"
```

## Project structure
```
flask-redis-counter/
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
├─ main.py
└─ templates/
   └─ index.html
```


