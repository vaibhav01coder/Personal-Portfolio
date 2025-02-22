from flask import Flask
import os
import datetime
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Vivek Vaibhav"
    username = "vivek"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30) 
    server_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    top_output = subprocess.getoutput("top -b -n 1 | head -20") 

    return f"""
    <h1>HTOP Endpoint</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
