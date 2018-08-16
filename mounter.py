#!/usr/bin/env python3
"""
Ensure a set of fileservers are mounted in the host.

This is run every few seconds on the Kubernetes hosts, and should
rely only on packages in the standard library for 3.5.
"""
import subprocess
import os
import json
import sys
import argparse


def mount_fileserver(share, mount_path):
    os.makedirs(mount_path, exist_ok=True)

    subprocess.check_call(['mount'])
    subprocess.check_call([
        'mount', 
        '-t', 'nfs4', 
        '-v',
        share,
        mount_path,
        '-o', 'soft,rw'
    ])


def is_mounted(mount_path):
    try:
        subprocess.check_call([
            'mountpoint',
            '-q',
            mount_path
        ])
        return True
    except subprocess.CalledProcessError:
        return False
    

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'mount_specs',
        help='Specification of what to mount where, in the form of nfs-share-spec=mount-path',
        nargs='+'
    )
    args = argparser.parse_args()

    for mount_spec in args.mount_specs:
        share, mount_path = mount_spec.split('=', 1)
        print('Ensuring {} is mounted at {}'.format(share, mount_path))

        if is_mounted(mount_path):
            print("{} is already mounted, skipping".format(fileserver))
        else:
            print("{} is not mounted, mounting".format(fileserver))
            mount_fileserver(share, mount_path)

if __name__ == '__main__':
    main()
