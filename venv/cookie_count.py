from flask import Flask, request, make_response

app = Flask(__name__)

app.config['DEBUG'] = True
@app.route('/home')
def visitor_count():
    
        # Converting Str to String
        count = int(request.cookies.get('visitor count', 0))
        
        # getting the key visitor count value as 0
        count = count + 1
        output = f'''You visited this page for {count} times'''
        
        resp = make_response(output)
        resp.set_cookie('visitor count', str(count))
        return resp
    
if __name__ == "__main__":
    app.run(debug=True)