from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for user information
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Get data from the registration form
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    # Store the data in user_data
    user_data[username] = {
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }

    return redirect(url_for('user_details', username=username))

@app.route('/user_details/<username>')
def user_details(username):
    # Display user information
    user_info = user_data.get(username, {})
    return render_template('user_details.html', username=username, user_info=user_info)

@app.route('/login', methods=['POST'])
def login():
    # Get data from the login form
    username = request.form.get('login_username')
    password = request.form.get('login_password')

    # Check if the username and password match
    if user_data.get(username, {}).get('password') == password:
        return redirect(url_for('user_details', username=username))
    else:
        return "Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True)