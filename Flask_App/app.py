from flask import Flask , render_template, redirect , url_for, request, session 
import socket

app = Flask(__name__)
app.secret_key = ""

@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"] 
        return redirect(url_for("user" , name = name))  
    else:
        return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello {name}!</h1>"
   

def find_avaliable_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    _, port = sock.getsockname()
    sock.close()

    return port

if __name__ == "__main__":
    dynamic_port = find_avaliable_port()
    app.run(port= dynamic_port, debug=True)