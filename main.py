from flask import Flask
from random import randint

number = randint(0, 10)

app = Flask(__name__)

def make_center(fn):
    def wrapper():
        return "<center>" + fn() + "</center>"
    return wrapper

@app.route("/")
@make_center
def title():
    return '<h1> Guess a Number between 0 to 9</h1>' \
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp">'

@make_center
@app.route("/<int:guess>")
def guess_number(guess):
    if guess == number:
        return f'<h2 style="color:green">{guess} is just right"</h2>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess > number:
        return f'<h2 style="color:blue">{guess} is too high"</h2>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h2 style="color:red">{guess} is too low"</h2>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)
