import os
import stripe
from dotenv import load_dotenv

load_dotenv()

class StripeManager:
    """
    Manages Stripe interactions for monetization.
    Currently a skeleton for testing purposes.
    """

    def __init__(self):
        self.api_key = os.getenv("STRIPE_SECRET_KEY")
        if self.api_key:
            stripe.api_key = self.api_key
        else:
            print("Warning: STRIPE_SECRET_KEY not found in environment variables.")

    def create_customer(self, email: str, name: str):
        """
        Creates a new customer in Stripe.
        """
        if not self.api_key:
            return {"error": "Stripe not configured"}
        
        try:
            customer = stripe.Customer.create(
                email=email,
                name=name,
            )
            return customer
        except Exception as e:
            return {"error": str(e)}

    def create_subscription(self, customer_id: str, price_id: str):
        """
        Creates a subscription for a customer.
        """
        if not self.api_key:
            return {"error": "Stripe not configured"}

        try:
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': price_id}],
            )
            return subscription
        except Exception as e:
            return {"error": str(e)}
