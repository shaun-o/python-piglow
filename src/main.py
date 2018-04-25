import sys
import piglow
import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Shaun This is  Python Hello World!' + sys.version

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
