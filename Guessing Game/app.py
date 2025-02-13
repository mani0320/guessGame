from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

@app.route('/')
def home():
    session['number'] = random.randint(1, 10)  # Generate a random number
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    correct_number = session['number']
    
    if user_guess < correct_number:
        message = "Too low! Try again. 🎯"
    elif user_guess > correct_number:
        message = "Too high! Try again. 🚀"
    else:
        message = "🎉 Congrats! You guessed the right number!"

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
