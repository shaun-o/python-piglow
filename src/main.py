import sys
import piglow
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    piglow.red(64)
    piglow.show()
    return 'Shaun This is  Python Hello World!' + sys.version

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
