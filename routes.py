from flask import Flask, render_template, request, redirect, url_for, session, flash
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


# Homepage
@app.route('/')
def index():
	final_year = int(datetime.datetime.now().strftime("%Y"))
	third_year = final_year + 1
	second_year = final_year + 2
	first_year = final_year + 3
	return render_template('index.html', final_year=final_year, third_year = third_year, second_year=second_year, first_year=first_year)


# action for form
@app.route('/submitForm')
def subForm():
	name = request.form['name']   
	email = request.form['email']
	phone = request.form['phone']
	studentClass = request.form['classof']
	purpose = request.form['purpose']
	return render_template('index.html')

# Log in Page for admins
@app.route('/login')
def login():
    return render_template('login.html')


# operational page for admins
@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
        app.run(debug=True)
