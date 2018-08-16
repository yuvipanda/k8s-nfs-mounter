#!/usr/bin/env python3
import subprocess
import time
import sys


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
             host_script,
        ] + sys.argv[1:])
    except subprocess.CalledProcessError:
        print("Host script failed")
    time.sleep(10)