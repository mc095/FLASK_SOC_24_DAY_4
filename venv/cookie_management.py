from flask import Flask, request, make_response

app = Flask(__name__)

# Using set_cookie() method to set the key-value pairs
@app.route('/setcookie')
def setcookie():
    # Initializing response object
    resp = make_response('Setting the cookie')
    resp.set_cookie('Vasavi', 'Computer Science Portal')
    return resp

# Getting cookie from the previous set_cookie code
@app.route('/page1')
def getcookie1():
    data = request.cookies.get('Vasavi', 'No cookie data found.')
    return f'''
        <html>
            <body>
                <h2 align="center">Session Management using Cookies</h2>
                <p align="center">This is Cookie Data From Page 1 and Data is: <strong>{data}</strong></p>
            </body>
        </html>
    '''

# Getting cookie from the previous set_cookie code
@app.route('/page2')
def getcookie2():
    data = request.cookies.get('Vasavi', 'No cookie data found.')
    return f'''
        <html>
            <body>
                <h2 align="center">Session Management using Cookies</h2>
                <p align="center">This is Cookie Data From Page 2 and Data is: <strong>{data}</strong></p>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
