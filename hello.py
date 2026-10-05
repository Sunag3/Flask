from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/ping")
def ping():
    return {"message": "why are you pinging me?"}

@app.route("/hello")
def hello_name():
    return {"message": "Hello, my name is ChatGPT!"}

# RUN in debug mode
if __name__ == "__main__":
    app.run(debug=True)