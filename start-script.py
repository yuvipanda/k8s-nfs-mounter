#!/usr/bin/env python3
import subprocess
import time
import sys
import os

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'mounter.py')) as f:
    HOST_SCRIPT = f.read()

while True:
    try:
        subprocess.check_call([ 'nsenter',
            # nseenter on alpine wants its options like this, and will print
            # a really unhelpful error message otherwise, boo
            '--target=1',
            '--mount',
            '--net',
            '--',
            'python3',
            '-c',
            HOST_SCRIPT
        ] + sys.argv[1:])
    except subprocess.CalledProcessError:
        print("Host script failed")
    time.sleep(10)