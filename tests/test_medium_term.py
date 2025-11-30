import unittest
import sys
import os
import sqlite3
from unittest.mock import MagicMock, patch

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from audit.audit_log import AuditLogger
from llm.gateway import LLMGateway

class TestMediumTerm(unittest.TestCase):

    def setUp(self):
        # Use in-memory DB for testing
        self.audit_db = "test_audit.db"
        if os.path.exists(self.audit_db):
            os.remove(self.audit_db)
        self.logger = AuditLogger(self.audit_db)

    def tearDown(self):
        if os.path.exists(self.audit_db):
            os.remove(self.audit_db)

    def test_audit_logging(self):
        self.logger.log_event("TEST_ACTION", "user_123", "resource_A", {"foo": "bar"})
        
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][3], "TEST_ACTION") # action is 4th column (0-indexed 3)
        self.assertEqual(logs[0][2], "user_123")    # user_id is 3rd column (0-indexed 2)
        print("\nAudit Log Test Passed: Logged and retrieved event.")

    @patch('litellm.completion')
    def test_llm_gateway(self, mock_completion):
        # Mock the litellm response
        mock_response = {
            'choices': [{'message': {'content': 'Hello world'}}],
            'usage': {'total_tokens': 10}
        }
        mock_completion.return_value = mock_response
        
        gateway = LLMGateway()
        response = gateway.completion("gpt-3.5-turbo", [{"role": "user", "content": "Hi"}])
        
        self.assertEqual(response['choices'][0]['message']['content'], 'Hello world')
        mock_completion.assert_called_once()
        print("LLM Gateway Test Passed: Mocked completion successful.")

if __name__ == '__main__':
    unittest.main()
