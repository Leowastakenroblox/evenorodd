from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            if number % 2 == 0:
                result = f"{number} is even."
            else:
                result = f"{number} is odd."
        except ValueError:
            result = "Invalid input. Please enter a valid number."
        return render_template('home.html', result=result)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)