#!/usr/bin/env python2.7

import argparse

from network import Network
from file_generator import train_file

parser = argparse.ArgumentParser('MLP argparser')
parser.add_argument(
    '--read_weights',
    action='store_true',
    default=False,
    help='if true then weights would be loaded from file'
)
parser.add_argument(
    '--draw_errors',
    action='store_true',
    default=False,
    help='if true then script will draw errors graph'
)


if __name__ == '__main__':
    args = parser.parse_args()
    network = Network(train_file, args.read_weights)
    print(network)
    network.calculate_weights()
    if args.draw_errors:
        network.draw_errors()