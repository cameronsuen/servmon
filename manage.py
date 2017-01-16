"""A Flask script to manage all the routines of the application"""

from flask_script import Manager
from servmon import app
import subprocess

# Enable debugging mode for development purposes
app.config['DEBUG'] = True

manager = Manager(app)

@manager.command
def makedoc():
    """Generate HTML documentation for APIs and common utils in docs/_build/html"""
    subprocess.run(['make', '-C', 'docs', 'html'])

@manager.command
def test():
    """Execute test cases"""
    subprocess.run('pytest')

if __name__ == '__main__':
    manager.run()
