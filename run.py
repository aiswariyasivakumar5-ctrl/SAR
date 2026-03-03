import subprocess
import sys
import os

def main():
    print("="*60)
    print("🚀 Starting Bharat Sagar Surveillance System")
    print("="*60)
    print("\n📱 The app will open in your browser shortly...")
    print("Press Ctrl+C to stop the server\n")
    
    # Run streamlit
    try:
        subprocess.run([
            "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=localhost"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
