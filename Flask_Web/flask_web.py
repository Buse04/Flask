from flask import Flask, render_template, url_for
import socket
import os

app = Flask(__name__)

pic_path = os.path.join('static')
app.config['UPLOAD_FOLDER'] = pic_path

pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'blogpost-img.jpeg')
pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'blogpost-img1.jpg')

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'image' : pic1
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'image': pic2
    }
]

@app.route("/")
def home():
    return render_template('index.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

def find_avaliable_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    _, port = sock.getsockname()
    sock.close()

    return port

if __name__ == "__main__":
    dynamic_port = find_avaliable_port()
    app.run(port= dynamic_port, debug=True)

