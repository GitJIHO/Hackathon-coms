"""Templates Demo

"""

import argparse
import threading
import time
import webbrowser

try:
    from bottle import get, run
except ImportError:
    print('''\
Error: Templates demo requires the "bottle" web framework.
Install the "bottle" package using:

    $ python3 -m pip install bottle

Then try executing the demo again.''')
    exit(1)

from templates import HTMLTemplate
from templates.bootstrap import Starter, Jumbotron


class Index(HTMLTemplate):
    def body(self):
        with self.tag('h1'):
            self.add('Python Templates')
        with self.tag('ul'):
            with self.tag('li'):
                with self.tag('a', attrs={'href': '/starter/'}):
                    self.add('Bootstrap Starter')
            with self.tag('li'):
                with self.tag('a', attrs={'href': '/jumbotron/'}):
                    self.add('Bootstrap Jumbotron')


@get('/')
def index():
    doc = Index()
    return doc.format()


@get('/starter/')
def starter():
    doc = Starter()
    return doc.format()


@get('/jumbotron/')
def jumbotron():
    doc = Jumbotron()
    return doc.format()


def launch(host, port):
    time.sleep(1)
    webbrowser.open(f'http://{host}:{port}/')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-launch', dest='launch', action='store_false')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=5050, type=int)
    parser.add_argument('--reload', action='store_true')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    if args.launch:
        thread = threading.Thread(target=launch, args=(args.host, args.port))
        thread.start()

    run(host=args.host, port=args.port, reloader=args.reload, debug=args.debug)


if __name__ == '__main__':
    main()
