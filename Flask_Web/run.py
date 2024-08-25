import socket
from flask_web import create_app

app = create_app()

def find_avaliable_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    _, port = sock.getsockname()
    sock.close()

    return port

if __name__ == "__main__":
    dynamic_port = find_avaliable_port()
    app.run(port= dynamic_port, debug=True)

