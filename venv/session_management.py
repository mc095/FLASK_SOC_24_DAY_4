from flask import Flask, session, render_template_string

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/setsession')
def setsession():
    # Initializing response object
    session['Vasavi'] = 'Sri Vasavi Engineering College'
    return 'Session created with Data'

# Getting session from the code
@app.route('/page1')
def getsession():
    data = session.get('Vasavi', 'No session data found.')
    return f'''
        <html>
            <body>
                <h2>Session Management using Cookies</h2>
                <p>This is Session Data from Page 1 and Data is: <strong>{data}</strong></p>
            </body>
        </html>
    '''

# Getting session from the previous set_cookie code
@app.route('/page2')
def getsession2():
    data = session.get('Vasavi', 'No session data found.')
    return f'''
        <html>
            <body>
                <h2>Session Management using Cookies</h2>
                <p>This is Session Data from Page 2 and Data is: <strong>{data}</strong></p>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
