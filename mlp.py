#!/usr/bin/env python2.7

from perceptron import Perceptron
from file_generator import train_file

# vector X=(N+1) vector Y=(M)
# X, Y = load_input_and_output()
# weights matrix W=(N+1)xM
# W = load_weights(len(X), len(Y), from_file=False)
# print(W)
p = Perceptron(train_file, True)
print(p.w)