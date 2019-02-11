from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

host = 'localhost' # '0.0.0.0' #"127.0.0.1" # I tried all of these ip's

if __name__ == '__main__':
    app.debug = True
    #port = int(os.environ.get("PORT", 8080)) # I also tried port was 5000
    # app.run(host=host, port=port)
    app.run(host='0.0.0.0', port=8080, debug=True)

#      
#This is the error I got 52.15.73.96 The connection has timed out
#The server at 52.15.73.96 is taking too long to respond.
