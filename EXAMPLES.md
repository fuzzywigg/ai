# Fuzzywigg AI - API Examples

This file demonstrates how to use the Fuzzywigg AI service components.

## Quick Start

```python
from src.core import FuzzywiggService

# Initialize the service
service = FuzzywiggService()

# Process a request
result = service.process_request(
    user_id="user_123",
    prompt="How can I improve my health?",
    model="gpt-3.5-turbo"
)

print(result['answer'])
```

## Individual Components

### PHI Guard

```python
from src.security import PhiGuard

guard = PhiGuard()
text = "Contact me at john@example.com or 555-123-4567"
redacted = guard.redact(text)
print(redacted)  # "Contact me at [REDACTED EMAIL] or [REDACTED PHONE]"
```

### LLM Gateway

```python
from src.llm import LLMGateway

gateway = LLMGateway(logging_callback=lambda data: print(f"Cost: ${data['cost']}"))
response = gateway.completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Audit Logger

```python
from src.audit import AuditLogger

logger = AuditLogger()
logger.log_event(
    action="USER_CONSENT_GRANTED",
    user_id="user_123",
    resource="health_records",
    details={"consent_type": "data_sharing"}
)

# View recent logs
logs = logger.get_logs(limit=10)
```

### Stripe Manager

```python
from src.payments import StripeManager

stripe = StripeManager()
customer = stripe.create_customer(
    email="user@example.com",
    name="John Doe"
)
```

## Environment Variables

Create a `.env` file:

```bash
# LLM APIs
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...

# IPFS/Pinata
PINATA_API_KEY=...
PINATA_SECRET_API_KEY=...
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python tests/test_short_term.py
python tests/test_medium_term.py

# Run demo
python demo.py
```

## Pre-commit Hooks

Install and use:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
