#!/usr/bin/env python
import sys
from hasweb import app

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 6400
app.run('0.0.0.0', port=port, debug=True)
