import sys
import os
from unittest.mock import MagicMock

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from core.service import FuzzywiggService

def run_demo():
    print("Initializing Fuzzywigg AI Service...")
    service = FuzzywiggService()
    
    # Mocking the LLM call to avoid actual API costs/keys for this demo
    service.llm_gateway.completion = MagicMock(return_value={
        'choices': [{'message': {'content': 'This is a mocked response from the AI.'}}],
        'usage': {'total_tokens': 50}
    })
    
    print("\n--- Scenario 1: Safe Query ---")
    user_id = "user_alice"
    prompt = "Tell me a joke about coding."
    print(f"User: {prompt}")
    result = service.process_request(user_id, prompt)
    print(f"AI: {result['answer']}")
    
    print("\n--- Scenario 2: PHI Query ---")
    user_id = "user_bob"
    prompt = "My patient John Doe (phone 555-0199) needs a prescription."
    print(f"User: {prompt}")
    result = service.process_request(user_id, prompt)
    print(f"Redacted Prompt sent to AI: {result['redacted_prompt']}")
    print(f"AI: {result['answer']}")
    
    print("\n--- Audit Log Check ---")
    logs = service.audit_logger.get_logs(limit=5)
    for log in logs:
        print(f"Log: {log}")

if __name__ == "__main__":
    run_demo()
