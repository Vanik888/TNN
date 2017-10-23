#!/usr/bin/env python2.7
import argparse
import random as ra
from numpy import random

max_p = 199
x_max_val = 1
y_max_val = 1
x_min_val = 0
y_min_val = 0
n_max_len = 101
m_max_len = 30
max_weight = 0.5
min_weight = -0.5
train_file = 'PA-A-train.dat'
weights_file = 'PA-A-weights.dat'

parser = argparse.ArgumentParser(description='Generate file with random values for input and output')

parser.add_argument(
    '-w',
    '--generate_weights',
    action='store_true',
    default=False,
    help='whether to generate weights and save them to file'
)
parser.add_argument(
    '-i',
    '--inputs_and_outputs',
    action='store_true',
    default=False,
    help='whether to generate inputs and outputs'
)
parser.add_argument(
    '-P',
    type=int,
    default=max_p,
    required=True,
    help='amount of train results'
)
parser.add_argument(
    '-M',
    type=int,
    default=m_max_len,
    required=True,
    help='size of output M <= 30'
)
parser.add_argument(
    '-N',
    type=int,
    default=n_max_len,
    required=True,
    help='size of input N <= 101'
)


def fill_weights(n_len, m_len,
                 left_border=min_weight, right_border=max_weight,
                 file=weights_file):
    """
    :param n_len: inputs count
    :param m_len: outputs count
    :param left_border: min value of weight
    :param right_border: max value of weight
    :param file: filename to store generated values
    :return: generates random floats from left_border to right border and
             saves values to file
    """
    print('generating weights')
    with open(file, 'wr') as f:
        for n in xrange(m_len):
            for m in xrange(n_len+1):
                f.write("%s " % ra.uniform(left_border, right_border))
            f.write('\n')
    print('weights matrix %sx%s successfully saved in %s' % (m_len,
                                                             n_len+1,
                                                             weights_file
                                                             ))


def fill_input_and_output(p, n_len, m_len,
                          x_min_val=x_min_val, x_max_val=x_max_val,
                          y_min_val=y_min_val, y_max_val=y_max_val,
                          file=train_file,
                          ):
    """
    :param n_len: len of input vector N
    :param m_len:  len of output vector M
    :param x_min_val: min value of item in N
    :param x_max_val: max value of item in N
    :param y_min_val: min value of item in M
    :param y_max_val: min value of item in M
    :param file: file to save generated values
    :return: generates random values for N and M and writes it to file
    """
    with open(file, 'wr') as f:
        print('generating %s inputs' % n_len)
        f.write('#input\n')
        for i in xrange(p):
            X = random.randint(x_min_val, x_max_val+1, n_len)
            for x in X:
                f.write("%s " % str(x))
            f.write('\n')

        print('generating %s outputs' % m_len)
        f.write('#output\n')
        for i in xrange(p):
            Y = random.randint(y_min_val, y_max_val+1, m_len)
            for y in Y:
                f.write("%s " % str(y))
            f.write("\n")
        print('inputs and outputs successfully saved in %s' % file)


if __name__ == '__main__':
    args = parser.parse_args()
    n_len = args.N
    m_len = args.M
    p = args.P
    if args.inputs_and_outputs:
        if n_len > n_max_len:
            print("Error: N=%s should be <= %s" % (n_len, n_max_len))
            exit(1)
        elif m_len > m_max_len:
            print("Error M=%s should be <= %s" % (m_len, m_max_len))
            exit(1)
        elif p > max_p:
            print("Error P=%s should be <= %s" % (p, max_p))
        fill_input_and_output(p, n_len, m_len)
    if args.generate_weights:
        fill_weights(n_len, m_len)

