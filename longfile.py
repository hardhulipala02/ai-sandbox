import os
import sqlite3
import subprocess

class DatabaseManager:
    def __init__(self, db_name="system.db"):
        self.connection = sqlite3.connect(db_name)

    def get_user_data(self, user_id):
        # BASELINE: This is currently safe
        query = "SELECT * FROM users WHERE id = ?"
        cursor = self.connection.execute(query, (user_id,))
        return cursor.fetchone()

def run_system_check():
    print("Running system health check...")
    return True

def process_file_upload(filename):
    if os.path.exists(filename):
        print(f"Processing {filename}")
        return True
    return False

def legacy_logger(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")
