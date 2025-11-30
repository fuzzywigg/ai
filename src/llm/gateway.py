import litellm
import os
from dotenv import load_dotenv

load_dotenv()

class LLMGateway:
    """
    Gateway for LLM interactions using LiteLLM.
    Provides a unified interface for various LLM providers (OpenAI, Anthropic, etc.)
    with built-in logging and cost tracking.
    """

    def __init__(self, logging_callback=None):
        """
        Initialize the gateway.
        
        Args:
            logging_callback (callable, optional): Function to call with usage stats.
        """
        self.logging_callback = logging_callback
        # Configure litellm callbacks if needed
        # litellm.success_callback = [self._success_handler]

    def completion(self, model: str, messages: list, **kwargs):
        """
        Wrapper around litellm.completion.
        
        Args:
            model (str): The model name (e.g., "gpt-3.5-turbo", "claude-2").
            messages (list): List of message dictionaries.
            **kwargs: Additional arguments for completion.
            
        Returns:
            dict: The completion response.
        """
        try:
            response = litellm.completion(model=model, messages=messages, **kwargs)
            
            if self.logging_callback:
                self.logging_callback({
                    "model": model,
                    "usage": response.get('usage', {}),
                    "cost": litellm.completion_cost(completion_response=response)
                })
                
            return response
        except Exception as e:
            # In a real app, log this error to Sentry/etc.
            print(f"LLM Error: {e}")
            raise e

    def _success_handler(self, kwargs, completion_response, start_time, end_time):
        # Internal handler if we use litellm's callback system directly
        pass
