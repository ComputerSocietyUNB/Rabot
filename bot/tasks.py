import os
import webbrowser

from invoke import task


@task()
def train_nlu(c):
    c.run(
        'python3 -m rasa_nlu.train -c nlu_config.yml '
        '--fixed_model_name current --data data/intents/ -o models --project nlu --verbose')


@task()
def train_core(c):
    c.run('python3 train.py')


@task()
def train(c):
    """ Trains the bot with dialogs on domain.yml and actions folder """
    train_nlu(c)
    train_core(c)


@task
def test(c, vv=False):
    """ NOT TESTED: Runs all tests """
    pass


@task
def style(c):
    """ Checks if your code is well formatted for this project """
    c.run('pycodestyle . --ignore=E402,W504')


@task()
def run_cli(c):
    """ Runs bot """
    c.run('python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml')


@task()
def run_telegram(c):
    """"Runs bot on telegram. Requires a credentials.yaml to work"""
    c.run("python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --port 5002 --credentials credentials.yml")


@task
def install(c):
    """ Installs the requirements necessary for this project """
    c.run('pip3 install -r bot.requirements.txt')


@task
def lint(c):
    """ NOT TESTED: Checks yaml file structure """
    c.run('yamllint .')
