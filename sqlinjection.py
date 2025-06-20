from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
@app.before_request
def setup():
    db.create_all()
    if not User.query.first():
        db.session.add_all([
            User(username='admin', password='adminpass'),
            User(username='guest', password='guest123'),
            User(username='user123', password='password321')
        ])
        db.session.commit()
@app.route('/')
def index():
    return '''
        <body style="background-color:white; color:black; text-align:center; font-family:sans-serif;">
            <h2>SQL Injection Demo</h2>
            <ul style="list-style: none; padding: 0; font-size: 18px;">
                <li><a href="/vulnerable" style="color:black; text-decoration: none;"> Vulnerable Login</a></li>
                <li><a href="/secure" style="color:black; text-decoration: none;"> Secure Login</a></li>
            </ul>
        </body>
    '''
@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    message = ""
    users_list = ""
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']
        sql = text(f"SELECT * FROM user WHERE username = '{username_input}' AND password = '{password_input}'")
        result = db.session.execute(sql).fetchall()
        if result:
            # Check for SQLi patterns
            if "'" in username_input or "'" in password_input or "OR" in username_input.upper() or "OR" in password_input.upper():
                all_users = User.query.all()
                users_list = '''
                    <div style="text-align:center; font-family:sans-serif;">
                        <h3>All Users</h3>
                        <table border="1" style="margin:auto; border-collapse: collapse;">
                            <tr><th>ID</th><th>Username</th><th>Password</th></tr>
                '''
                for u in all_users:
                    users_list += f"<tr><td>{u.id}</td><td>{u.username}</td><td>{u.password}</td></tr>"
                users_list += "</table></div>"
            else:
                user = result[0]
                message = f"<p style='color:red;'> Welcome, {user.username} (vulnerable mode)</p>"
        else:
            message = "<p style='color:red;'> Invalid credentials.</p>"

    return f'''
        <div style="text-align:center; font-family:sans-serif;">
            <h3>Vulnerable Login</h3>
            <form method="POST">
                Username: <input name="username"><br><br>
                Password: <input name="password" type="password"><br><br>
                <input type="submit" value="Login">
            </form>
            {message}
            {users_list}
            <br><a href="/">⬅ Back</a>
        </div>
    '''
@app.route('/secure', methods=['GET', 'POST'])
def secure():
    message = ""
    if request.method == 'POST':
        username_input = request.form['username']
        password_input = request.form['password']

        user = User.query.filter_by(username=username_input, password=password_input).first()
        if user:
            message = f"<p style='color:green;'> Welcome, {user.username} (secure mode)</p>"
        else:
            message = "<p style='color:green;'> Invalid credentials.</p>"

    return f'''
        <div style="text-align:center; font-family:sans-serif;">
            <h3> Secure Login</h3>
            <form method="POST">
                Username: <input name="username"><br><br>
                Password: <input name="password" type="password"><br><br>
                <input type="submit" value="Login">
            </form>
            {message}
            <br><a href="/">⬅ Back</a>
        </div>
    '''
if __name__ == '__main__':
    app.run(debug=True)
