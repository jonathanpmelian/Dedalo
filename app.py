from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Static Site Generator!</h1>"

if __name__ == '__main__':
    # Do not use run in production
    app.run(debug=True)