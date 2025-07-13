from database.models import init_db
import subprocess
import os

def main():
    print("🔧 Initializing Personal Finance Tracker...")
    
    init_db()
    print("✅ Database is ready.")
    
    print("🚀 Launching CLI... (Type --help to see commands)")
    subprocess.run(["python", "cli.py"])

if __name__ == "__main__":
    main()