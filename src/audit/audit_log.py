import sqlite3
import json
from datetime import datetime
import os

class AuditLogger:
    """
    Logs security and compliance events to a local SQLite database.
    Simulates a secure audit vault.
    """

    def __init__(self, db_path="audit.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize the audit database schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                user_id TEXT,
                action TEXT NOT NULL,
                resource TEXT,
                details TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_event(self, action: str, user_id: str = None, resource: str = None, details: dict = None):
        """
        Log an event to the audit log.
        
        Args:
            action (str): The action performed (e.g., "CONSENT_GRANTED", "PHI_ACCESS").
            user_id (str, optional): ID of the user performing the action.
            resource (str, optional): The resource being accessed/modified.
            details (dict, optional): Additional context.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        timestamp = datetime.utcnow().isoformat()
        details_json = json.dumps(details) if details else None
        
        cursor.execute('''
            INSERT INTO audit_log (timestamp, user_id, action, resource, details)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, user_id, action, resource, details_json))
        
        conn.commit()
        conn.close()
        # In a real system, we might also hash this entry to a blockchain here.

    def get_logs(self, limit=10):
        """Retrieve recent logs."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM audit_log ORDER BY id DESC LIMIT ?', (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows
