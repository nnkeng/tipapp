from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    total_bill = float(request.form['total_bill'])
    tip_choice = request.form['tip_choice']

    if tip_choice == '15':
        tip_percentage = 15
    elif tip_choice == '20':
        tip_percentage = 20
    elif tip_choice == '25':
        tip_percentage = 25
    else:
        tip_percentage = float(request.form['custom_tip'])

    tip_amount = round(total_bill * (tip_percentage / 100), 2)
    total_amount = round(total_bill + tip_amount, 2)

    return render_template('result.html', tip_amount=tip_amount, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
