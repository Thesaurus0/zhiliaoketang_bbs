from flask import Flask
import click
import os
from extensions import db, init_ext

from cms import init_view_cms, CMSUser
from common import init_view_common
from front import init_view_front
from config import envs
# from cms.models import CMSUser

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




# @app.cli.command('addcmsuser', help='cms user creating')
# @click.option('--name', type=click.STRING, help='cms user name')
# def add_cms_user( name):
#     print('user was inserted.')

init_view_cms(app)
init_view_common(app)
init_view_front(app)
init_ext(app)

print('aaaaaaaaaaaaaaaaaaaaa')



@app.cli.command('addcmsuser', help='cms user creating')
@click.option('--name', type=click.STRING, help='cms user name')
@click.option('--pwd', type=click.STRING, help='cms user password')
@click.option('--email', type=click.STRING, help='cms user email')
def add_cms_user(name, pwd, email):
    user = CMSUser(username = name, password = pwd, email = email)
    db.session.add(user)
    db.session.commit()
    print('user was inserted.')

if __name__ == '__main__':
    # app.run()
    print('main ....')
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)


