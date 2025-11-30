import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from security.phi_guard import PhiGuard
from payments.stripe_manager import StripeManager

class TestShortTerm(unittest.TestCase):

    def test_phi_guard_redaction(self):
        guard = PhiGuard()
        text = "Contact me at john.doe@example.com or 555-123-4567. My SSN is 123-45-6789."
        redacted = guard.redact(text)
        
        self.assertIn("[REDACTED EMAIL]", redacted)
        self.assertIn("[REDACTED PHONE]", redacted)
        self.assertIn("[REDACTED SSN]", redacted)
        self.assertNotIn("john.doe@example.com", redacted)
        self.assertNotIn("555-123-4567", redacted)
        self.assertNotIn("123-45-6789", redacted)
        print(f"\nOriginal: {text}")
        print(f"Redacted: {redacted}")

    def test_stripe_manager_init(self):
        # Test initialization without API key (should warn but not crash)
        manager = StripeManager()
        self.assertIsNone(manager.api_key)
        
        # Test method handling without key
        result = manager.create_customer("test@example.com", "Test User")
        self.assertEqual(result, {"error": "Stripe not configured"})

if __name__ == '__main__':
    unittest.main()
