# Workflow System

Workflow System is an experimental personal workflow automation platform designed to capture tasks, study notes, ideas, and reminders from simple inputs and route them into a structured system.

The project is currently in active development. The current version is not the final architecture; it is the first functional foundation for a larger automation ecosystem that will evolve over time.

## Vision

The goal of Workflow System is to become a modular assistant-oriented backend capable of receiving information from different sources, classifying it, storing it, and preparing it for future workflows such as reminders, dashboards, study planning, task management, and integrations with external tools.

At this stage, the system focuses on one essential idea: capture first, organize later.

## Current Status

This repository contains the initial base of the system:

- FastAPI backend
- PostgreSQL database
- SQLAlchemy data model
- Telegram bot input channel
- Docker-based local environment
- Basic text classification for tasks, study items, and notes

The current implementation should be understood as an early MVP foundation. Many components are intentionally simple and will be replaced, expanded, or redesigned as the system grows.

## What It Can Do Now

Currently, the system can:

- Run locally with Docker Compose
- Receive text messages through a Telegram bot
- Send those messages to the FastAPI backend
- Classify incoming text as `task`, `study`, or `note`
- Store items in PostgreSQL
- List stored items through the API

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- PostgreSQL 15
- SQLAlchemy
- Pydantic
- Docker
- Docker Compose
- Telegram Bot API

## Project Structure

```text
workflow-system/
├── app/
│   ├── core/
│   │   └── classifier.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── telegram_bot.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Architecture Overview

```text
Telegram User
    ↓
Telegram Bot
    ↓
FastAPI Backend
    ↓
Classifier
    ↓
PostgreSQL Database
```

The Telegram bot acts as an input channel. The API is responsible for receiving and storing structured items. The classifier provides a simple first layer of organization.

## API Endpoints

### Health/root endpoint

```http
GET /
```

Returns a basic confirmation that the backend is running.

### Create item

```http
POST /items
```

Example request:

```json
{
  "content": "estudiar bases de datos",
  "source": "manual",
  "status": "pending"
}
```

Example response:

```json
{
  "id": 1,
  "content": "estudiar bases de datos",
  "type": "study",
  "source": "manual",
  "status": "pending",
  "created_at": "2026-05-02T22:00:00"
}
```

### List items

```http
GET /items
```

Returns all stored items.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/jdcamargo2/workflow-system.git
cd workflow-system
```

### 2. Create the environment file

```bash
cp .env.example .env
```

Then edit `.env` and set your own values, especially:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 3. Start the system

```bash
docker compose up --build
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

## Environment Variables

| Variable | Description |
| --- | --- |
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `POSTGRES_DB` | PostgreSQL database name |
| `DATABASE_URL` | SQLAlchemy database connection URL |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token |
| `API_BASE_URL` | Internal URL used by the bot to call the API |

## Development Notes

This project is intentionally minimal right now. Some current decisions are temporary and expected to change, including:

- Database tables are created with `Base.metadata.create_all()` instead of migrations.
- The classifier is keyword-based and not yet intelligent.
- There is no authentication layer yet.
- There are no automated tests yet.
- The bot uses polling instead of webhooks.
- The data model is still very small.

These choices are acceptable for the current stage because the priority is to validate the system flow end to end.

## Roadmap

Planned improvements include:

- Add a proper README-driven setup flow
- Add health checks for Docker services
- Add database migrations with Alembic
- Add automated tests
- Add richer item types and metadata
- Improve classification logic
- Add reminders and scheduling
- Add integrations with external productivity tools
- Add a dashboard or admin interface
- Add user/account support if needed
- Improve security and production readiness

## Production Readiness

This project is not production-ready yet.

Before any production deployment, the system will need:

- Secure secret management
- Authentication and authorization
- Proper database migrations
- Logging and observability
- Error handling improvements
- Backup strategy
- Deployment configuration
- Tests and CI checks

## Project Direction

Workflow System is being developed as a long-term personal automation backend. Its purpose is not only to store tasks, but to become a flexible workflow layer that can connect study routines, personal planning, reminders, bots, dashboards, and future AI-assisted processing.

The current repository represents the foundation, not the destination.
