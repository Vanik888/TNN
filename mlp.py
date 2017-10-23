#!/usr/bin/env python2.7

import argparse

from perceptron import Perceptron
from file_generator import train_file

parser = argparse.ArgumentParser('MLP argparser')
parser.add_argument(
    '--read_weights',
    action='store_true',
    default=False,
    help='if true then weights would be loaded from file'
)

if __name__ == '__main__':
    args = parser.parse_args()
    p = Perceptron(train_file, args.read_weights)
    p.calc()
    p.draw_errors()
print(p.w)