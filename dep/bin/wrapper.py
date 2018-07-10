#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import base64
import hashlib
import os
import random
import shutil
import signal
import string
import sys
import time

# def solve(prefix):
#     ha = hashlib.sha1()
#     for i in itertools.product(string.ascii_letters+string.digits, repeat = 5):
#         ha = hashlib.sha1()
#         ha.update((prefix+str(i)))
#         if ord(ha.digest()[-1]) == 0 and ord(ha.digest()[-2]) == 0 and ord(ha.digest()[-3]) == 0:
#             print prefix+str(i)
#             return


def proof_of_work():
    signal.alarm(60)
    proof = random_str(16)
    print(
        "Please provide your proof of work, a sha1 sum ending in 24 bit's set to 0, it must be of length %d bytes, starting with %s\n"
        % (len(proof) + 5, proof))

    test = input()
    test = test.strip()
    if len(test) != len(proof) + 5:
        print("check failed! incorrect length")
        sys.exit(-1)

    ha = hashlib.sha1()
    ha.update(test.encode('utf-8'))
    if test[:16] != proof or ha.digest()[-1] != 0 or ha.digest()[-2] != 0 \
        or ha.digest()[-3] != 0:
        print("check failed!")
        sys.exit(-1)
    signal.alarm(0)


def random_str(randomlength=8):
    a = list(string.ascii_letters)
    random.shuffle(a)
    return ''.join(a[:randomlength])


proof_of_work()

dirname = os.path.abspath(os.path.dirname(__file__))
db = os.path.join(dirname, 'camera.db')
binary = os.path.join(dirname, 'camera')
tmp = os.path.join('/tmp', random_str())
os.mkdir(tmp)

os.chdir(tmp)
shutil.copyfile(db, os.path.join(tmp, 'camera.db'))
os.system('%s' % (binary, ))
