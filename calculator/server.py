
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

history_file = "calculator/data/calculation_history.txt"   # stores file path for calculation history

# Serves homepage, pretty straightforward.
@app.route("/")
def home():
    print("Serving homepage 'calculator.html'")
    return render_template("calculator.html")

# performs the calculations and displays them to the user.
@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    print("Evaluating Expression...")
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = calculate_expression(expression)
            if result is not None:
                save_to_history(expression, result)
            return render_template("calculator.html", expression=expression, result=result)
        except Exception as e:
            error_message = "Error: Invalid expression"
            print({e})
            return render_template("calculator.html", error=error_message)
    return render_template("calculator.html")


# Read history from history.txt
@app.route("/history")
def history():
    print("Serving 'history.html' so the user can see what calculations have already been done!")
    history_data = []
    try:
        with open(history_file, "r") as file:
            history_data = file.readlines()
    except FileNotFoundError:
        pass  # If history.txt doesn't exist, leave history_data as an empty list
    
    return render_template("history.html", history=history_data)


 # sends the user to a 404 page if they try to go somewhere on the webpage that doesnt exist.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Read history from history.txt and format into JSON
@app.route("/api/history")
def api_history():
    history_data = []
    try:
        with open(history_file, "r") as file:
            history_data = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass  # If history.txt doesn't exist, leave history_data as an empty list

    return jsonify({"history": history_data})


# Helper Functions


# For simplicity, let's assume eval() can be used.
def calculate_expression(expression):
    result = eval(expression)
    return result

# Helper to write an expression into our data file
def save_to_history(expression, result):
    try:
        with open(history_file, "a") as file:
            file.write(f"{expression} = {result}\n")
    except Exception as e:
        print(f"Error occurred while saving to history: {e}")

# Driver code
if __name__ == '__main__':
   app.debug = True
   app.run(port=60012)


