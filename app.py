from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Docker Project 2"

@app.route('/health')
def health():
    return "Application is Healthy"

@app.route('/version')
def version():
    return "Version 3.0"

@app.route('/info')
def info():
    return "Running Three Container Application"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
