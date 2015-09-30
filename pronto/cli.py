import os
import click
from git import Repo
import webbrowser
from urlparse import urljoin
from jira import JIRA


JIRA_URL = os.environ.get('JIRA_URL')
JIRA_USER = os.environ.get('JIRA_USER')
JIRA_PASS = os.environ.get('JIRA_PASS')


@click.command()
@click.argument('task', default=None, required=False)
def jira(task):
    """Open current JIRA task. If Task number is not provided than it is taken from a name of current branch."""
    repo = Repo(os.getcwd())
    click.echo("Opening related jira task {0} in browser...".format(repo.head.ref.name))
    webbrowser.open(urljoin(BASE_JIRA_URL, task or repo.head.ref.name))


@click.command()
@click.argument('task', default=None, required=False)
def comments(task):
    repo = Repo(os.getcwd())
    jr = JIRA({'server': JIRA_URL}, basic_auth=(JIRA_USER, JIRA_PASS))
    issue = jr.issue(task or repo.head.ref.name)
    for comment in issue.fields.comment.comments:
        click.echo('-----------------------------------------------------------')
        click.echo(click.style(comment.author.displayName + ': \n', fg='green'))
        click.echo('\r' + comment.body)

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """Tool to make PR realeasing easier"""
    click.echo('Do some staff here')

