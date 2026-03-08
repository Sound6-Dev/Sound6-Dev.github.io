from flask import Flask, render_template, request
from games.dice_game import DiceGame
import random

app = Flask(__name__)
game = DiceGame()

@app.route("/", methods=["GET", "POST"])
def dice():
    message = ""
    roll_value = ""

    if request.method == "POST":

        # Start a new game
        if "new_game" in request.form:
            game.reset()
            message = "New game started."

        # Random roll
        elif "random_roll" in request.form:
            roll = random.randint(2, 12)
            game.play_turn(roll)
            roll_value = roll
            message = f"Random roll: {roll}. {game.result}"

        # Manual roll
        else:
            roll_value = request.form.get("roll")
            try:
                roll = int(roll_value)
                game.play_turn(roll)
                message = game.result
            except ValueError:
                message = "Error: Please enter a number."

    return render_template(
        "dice.html",
        turn=game.turn,
        point=game.point,
        finished=game.finished,
        result=game.result,
        message=message,
        roll_value=roll_value
    )

if __name__ == "__main__":
    app.run(debug=True)
