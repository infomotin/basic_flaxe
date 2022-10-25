from flask import Flask

app = Flask(__name__)

print("Hello World");

# run the app.py file
if __name__ == "__main__":
    app.run()