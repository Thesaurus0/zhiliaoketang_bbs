from flask import Flask
import click
import os

from flask.cli import load_dotenv
load_dotenv()

envionment = os.environ.get("FLASK_ENV") or 'production'
print('envionment ==' + str(envionment))
if envionment.find('dev') >= 0:
    env = 'dev'
elif envionment.find('uat') >= 0:
    env = 'uat'
elif envionment.find('prod') >= 0:
    env='prod'
else:
    raise 'the FLASK_ENV is incorrect: ' + envionment
print('env:' + env)

app = Flask(__name__)
app.config.from_object(envs.get(env))



if __name__ == '__main__':
    app.run()
