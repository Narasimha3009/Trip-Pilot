import sys
import os
import uvicorn
import socket

# Ensure utf-8 stdout encoding for Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

if __name__ == "__main__":
    port = 8000
    if is_port_in_use(8000):
        port = 8080

    print("==================================================================")
    print(" Trip Pilot - Global Travel Guidance & AI Agent Server")
    print(f" Web Interface: http://127.0.0.1:{port}")
    print(f" Interactive API Docs: http://127.0.0.1:{port}/docs")
    print("==================================================================")
    uvicorn.run("backend.main:app", host="127.0.0.1", port=port, reload=True)