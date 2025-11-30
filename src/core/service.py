from src.security.phi_guard import PhiGuard
from src.llm.gateway import LLMGateway
from src.audit.audit_log import AuditLogger
from src.payments.stripe_manager import StripeManager
import os

class FuzzywiggService:
    """
    Core service layer for Fuzzywigg AI.
    Integrates Security (PHI), AI (LLM), Compliance (Audit), and Monetization (Stripe).
    """

    def __init__(self):
        self.phi_guard = PhiGuard()
        self.audit_logger = AuditLogger()
        self.stripe_manager = StripeManager()
        # Initialize LLM Gateway with a logging callback that saves to Audit Log
        self.llm_gateway = LLMGateway(logging_callback=self._log_llm_usage)

    def _log_llm_usage(self, usage_data):
        """Callback to log LLM usage and cost."""
        self.audit_logger.log_event(
            action="LLM_USAGE",
            resource="LiteLLM",
            details=usage_data
        )

    def process_request(self, user_id: str, prompt: str, model: str = "gpt-3.5-turbo"):
        """
        Process a user request through the full pipeline:
        1. Check Subscription (Monetization)
        2. Redact PHI (Security)
        3. Call LLM (AI)
        4. Log everything (Compliance)
        """
        
        # 1. Check Subscription (Mock check for now)
        # In a real app, we would check self.stripe_manager.get_subscription_status(user_id)
        is_premium = True # Mock
        if not is_premium:
            return {"error": "Subscription required"}

        # 2. Redact PHI
        clean_prompt = self.phi_guard.redact(prompt)
        if clean_prompt != prompt:
            self.audit_logger.log_event(
                action="PHI_REDACTED",
                user_id=user_id,
                details={"original_length": len(prompt), "redacted_length": len(clean_prompt)}
            )

        # 3. Call LLM
        try:
            messages = [{"role": "user", "content": clean_prompt}]
            response = self.llm_gateway.completion(model=model, messages=messages)
            answer = response['choices'][0]['message']['content']
            
            # Log the successful interaction
            self.audit_logger.log_event(
                action="REQUEST_PROCESSED",
                user_id=user_id,
                details={"model": model}
            )
            
            return {
                "status": "success",
                "answer": answer,
                "redacted_prompt": clean_prompt
            }

        except Exception as e:
            self.audit_logger.log_event(
                action="REQUEST_FAILED",
                user_id=user_id,
                details={"error": str(e)}
            )
            return {"status": "error", "message": str(e)}
