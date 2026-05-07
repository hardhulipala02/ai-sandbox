import os
import sqlite3
import subprocess

class DatabaseManager:
    def __init__(self, db_name="system.db"):
        self.connection = sqlite3.connect(db_name)

    def get_user_data(self, user_id):
        """
        VULNERABILITY #1: SQL INJECTION
        The developer switched from a parameterized query to an f-string.
        An attacker can now pass "' OR '1'='1" to dump the entire database.
        """
        query = f"SELECT * FROM users WHERE id = '{user_id}'"
        cursor = self.connection.execute(query)
        return cursor.fetchone()

def run_system_check():
    """Standard health check function (Safe)"""
    print("Running system health check...")
    return {"status": "success", "check": "disk_space"}

def run_custom_diagnostic(command_type):
    """
    VULNERABILITY #2: COMMAND INJECTION
    The developer is passing raw user input directly into os.system.
    An attacker could pass 'check; rm -rf /' to execute malicious commands.
    """
    print(f"Executing diagnostic: {command_type}")
    os.system(f"diagnostics_tool --type {command_type}")
    return {"status": "success"}

def process_file_upload(filename):
    """Standard file check (Safe)"""
    if os.path.exists(filename):
        print(f"Processing {filename}")
        return True
    return False

def download_user_report(report_path):
    """
    VULNERABILITY #3: PATH TRAVERSAL
    The developer is opening a file path provided directly by the user.
    An attacker can pass '../../etc/passwd' to read sensitive system files.
    """
    print(f"Fetching report from: {report_path}")
    with open(report_path, 'r') as f:
        return f.read()

def legacy_logger(message):
    """Simple logging utility (Safe)"""
    with open("log.txt", "a") as f:
        f.write(message + "\n")
