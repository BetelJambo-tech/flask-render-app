from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! My web app is running on Render!"

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)