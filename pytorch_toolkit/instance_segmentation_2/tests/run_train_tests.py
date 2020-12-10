# Copyright (C) 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.

""" This module contains unit tests. """

import argparse
import os
import sys
import unittest


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern', default='train_tests_*.py')

    return parser.parse_args()


def main():
    if os.path.abspath(os.getcwd()) == os.path.abspath(os.path.join(os.path.dirname(__file__), '..')):
        return 0

    args = parse_args()
    testsuite = unittest.TestLoader().discover(
        os.path.dirname(__file__), pattern=args.pattern.replace('-', '_')
    )
    ret = not unittest.TextTestRunner(verbosity=1).run(testsuite).wasSuccessful()
    sys.exit(ret)


if __name__ == '__main__':
    main()