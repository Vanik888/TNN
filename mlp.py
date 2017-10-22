#!/usr/bin/env python2.7
import random as ra
from numpy import array, insert
from file_generator import max_weight, min_weight, input_file, weights_file


def load_input_and_output(file=input_file):
    """
    :param file: filename with training data X, Y
    :return: arrays X (including bias) and Y
    """
    with open(file, 'r') as f:
        lines = [l.replace('\n', '') for l in f.readlines()]
    lines = list(filter(lambda l: not (l.startswith('#') or l.startswith('\n')), lines))
    data = [l.split() for l in lines]
    # add bias in X[0]
    X = insert(array(data[0]), 1, 1)
    Y = array(data[1])
    return X.T, Y.T


def load_weights(n_len, m_len, from_file=False):
    """
    :param n_len: N + 1 (inputs plus bias)
    :param m_len: M (outputs)
    :param from_file: if True then load weights from file
    :return: (N+1)xM weights matrix
    """
    W = []
    if from_file:
        with open(weights_file, 'r') as f:
            lines = [l.replace('\n', '') for l in f.readlines()]
        W = array([l.split() for l in lines])
    else:
        W = array([[ra.uniform(min_weight, max_weight)
                    for i in xrange(m_len)] for j in xrange(n_len)])
    return W


# vector X=(N+1) vector Y=(M)
X, Y = load_input_and_output()
# weights matrix W=(N+1)xM
W = load_weights(len(X), len(Y), from_file=False)
print(W)