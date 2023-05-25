"""
This is a simple Flask application.

It contains a single route that returns a greeting message.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Handle the root endpoint.

    Returns:
        str: A greeting message.
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
