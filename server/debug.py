from app import *
import routes

from flask.ext.runner import Runner

app.debug = True
runner = Runner(app)

if __name__ == '__main__':
    runner.run()
