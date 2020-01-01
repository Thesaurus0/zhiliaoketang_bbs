from flask import Flask
import click
import os

from cms import init_view_cms
from common import init_view_common
from front import init_view_front
from config import envs


def get_env_by_os_environment(envionment):
    if envionment.find('dev') >= 0:
        return 'dev'
    elif envionment.find('uat') >= 0:
        return 'uat'
    elif envionment.find('prod') >= 0:
        return 'prod'
    else:
        raise 'the FLASK_ENV is incorrect: ' + envionment

from flask.cli import load_dotenv
load_dotenv()

envionment = os.environ.get("FLASK_ENV") or 'production'
env = get_env_by_os_environment(envionment)
print('env:' + env)

app = Flask(__name__)
app.config.from_object(envs.get(env))

init_view_cms(app)
init_view_common(app)
init_view_front(app)


if __name__ == '__main__':
    # app.run()
    print('main ....')
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)


