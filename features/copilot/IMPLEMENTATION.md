# Copilot implementation notes

This document explains how to integrate the Copilot Milestone 1 service into the invoice-ai-agent system.

Overview
- A new microservice (or module) `backend/copilot_service` provides two endpoints:
  - POST /copilot/suggest
  - POST /copilot/feedback
- A lightweight frontend reviewer component is provided at `frontend/src/components/CopilotReviewer.tsx`.
- Database migrations are provided under `migrations/001_create_copilot_tables.sql`.

Deployment options
- Add `backend/copilot_service` into your backend monorepo or run it as a separate FastAPI microservice.
- The service is provider-agnostic. Implement and register a SuggestionProvider implementation to enable production suggestions (CRM fuzzy matching, or LLM-based suggestion). If no provider is configured the suggest endpoint returns 503.

Testing
- The tests directory contains pytest-based unit/integration tests that use a deterministic MockSuggestionProvider.
- To run tests locally:
  - python -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements-dev.txt
  - pytest -q

Security and privacy
- The service never fabricates missing data in production. The MockSuggestionProvider is used only in tests.

Files added in this milestone
- features/copilot/decision-rules.md
- features/copilot/IMPLEMENTATION.md
- backend/copilot_service/*
- migrations/001_create_copilot_tables.sql
- frontend/src/components/CopilotReviewer.tsx
- tests/*

