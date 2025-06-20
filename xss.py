from flask import Flask, request, render_template_string, redirect
import bleach

app = Flask(__name__)
vulnerable_comments = []
safe_comments = []
@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                background-color: #f0f8ff; 
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            h1 {
                color: #003366;
            }
            a {
                text-decoration: none;
                color: #0066cc;
                font-size: 18px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
        </style>
    </head>
    <body>
        <h1>XSS(Cross site scripting)</h1>
        <ul>
            <li><a href="/vulnerable">Vulnerable Comment Page (XSS Possible)</a></li><br>
            <li><a href="/safe">Safe Comment Page (XSS Prevented)</a></li>
        </ul>
    </body>
    </html>
    '''
@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    if request.method == 'POST':
        comment = request.form['comment']
        vulnerable_comments.append(comment)  
        return redirect('/vulnerable')

    return render_template_string('''
        <html>
        <head>
            <style>
                body {
                    background-color: #fff8dc; 
                    text-align: center;
                    font-family: Verdana, sans-serif;
                    padding-top: 40px;
                }
                textarea, input {
                    font-size: 16px;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
            </style>
        </head>
        <body>
            <h2>Vulnerable Comment Section (Unsafe)</h2>
            <form method="POST">
                <textarea name="comment" rows="4" cols="40"></textarea><br><br>
                <input type="submit">
            </form>
            <h3>The recent comments are:</h3>
            <ul>
                {% for c in comments %}
                    <li>{{ c|safe }}</li>  <!-- Allows raw HTML/JS (bad) -->
                {% endfor %}
            </ul>
            <br>
            <a href="/">Back to Home</a>
        </body>
        </html>
    ''', comments=vulnerable_comments)
@app.route('/safe', methods=['GET', 'POST'])
def safe():
    if request.method == 'POST':
        comment = request.form['comment']
        clean_comment = bleach.clean(comment)  
        safe_comments.append(clean_comment)
        return redirect('/safe')

    return render_template_string('''
        <html>
        <head>
            <style>
                body {
                    background-color: #e6ffe6; 
                    text-align: center;
                    font-family: Georgia, serif;
                    padding-top: 40px;
                }
                textarea, input {
                    font-size: 16px;
                }
                ul {
                    list-style: none;
                    padding: 0;
                }
            </style>
        </head>
        <body>
            <h2>Safe comment section </h2>
            <form method="POST">
                <textarea name="comment" rows="4" cols="40"></textarea><br><br>
                <input type="submit">
            </form>
            <h3>The recent comments are:</h3>
            <ul>
                {% for c in comments %}
                    <li>{{ c }}</li>  <!-- Auto-escaped (safe) -->
                {% endfor %}
            </ul>
            <br>
            <a href="/">Back to Home</a>
        </body>
        </html>
    ''', comments=safe_comments)
if __name__ == '__main__':
    app.run(debug=True)
