#!/usr/bin/env python
import sys
from hasweb import application
from werkzeug.serving import run_simple

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 6400


if __name__ == '__main__':
    run_simple('0.0.0.0', port, application,
               use_reloader=True, use_debugger=True, use_evalex=True)
