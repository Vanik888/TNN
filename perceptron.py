import numpy as np
import random as ra

from file_generator import max_weight, min_weight, train_file, weights_file

class Perceptron:
    """
    Defines a class for a Perceptron
    """
    w = None

    def __init__(self, train_file=train_file, weights_from_file=False):
        """
        :param train_file: file with training data
        :param weights_from_file: whether read weights from file
        """
        self.x, self.y = self.init_input_and_output(train_file)
        self.w = self.init_weights(len(self.x), len(self.y), weights_from_file)

    @staticmethod
    def init_weights(n_len, m_len, from_file=False):
        """
        :param n_len: N + 1 (inputs plus bias)
        :param m_len: M (outputs)
        :param from_file: if True then load weights from file
        :return: Mx(N+1) weights matrix
        """
        W = []
        if from_file:
            with open(weights_file, 'r') as f:
                lines = [l.replace('\n', '') for l in f.readlines()]
            W = np.array([[float(v) for v in l.split()] for l in lines])
        else:
            W = np.array([[ra.uniform(min_weight, max_weight)
                        for i in xrange(n_len)] for j in xrange(m_len)])
        return W

    @staticmethod
    def init_input_and_output(file=train_file):
        """
        :param file: filename with training data X, Y
        :return: arrays X (including bias) and Y
        """
        with open(file, 'r') as f:
            lines = [l.replace('\n', '') for l in f.readlines()]
        lines = list(
            filter(lambda l: not (l.startswith('#') or l.startswith('\n')),
                   lines))
        data = [[int(item) for item in l.split()] for l in lines]
        # add bias in X[0]
        X = np.insert(np.array(data[0]), 0, 1)
        Y = np.array(data[1])
        return X.T, Y.T

    @staticmethod
    def trans_function(x, derivative=False):
        if derivative:
            return x*(1-x)
        else:
            return 1/(1-np.exp(-x))

    def get_weights(self):
        """
        Returns the weights of the weight matrix.
        Format for a perceptron with one output unit.
        [wb, w1, ..... wn]
        :return:
        """
        return self.w

    def fprop(self, x):
        """
        Forward propagates an input vector through the perceptron

        Args:
        ----
        x: vector of training exemplar
        """
        assert x is not None
        print x.shape
        x = np.append([1], x, axis=0)
        if len(x.shape) == 1:
            x = np.expand_dims(x, axis=1)
        return np.where(np.dot(self.w, x) > 0, 1, 0)


# p = Perceptron(3, 3)
# p.get_weights()

# print p.fprop(np.array([1, 0, 1]))

# A = np.array([[2,3,4],[3,4,5]])
# B = np.array([[2,3,4],[3,4,5]])

# C = np.dot(A,np.transpose(B))

# print C
