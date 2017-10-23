import numpy as np
import random as ra

from pylab import ylim, plot, show, subplot

from file_generator import max_weight, min_weight, train_file, weights_file

class Network:
    """
    Defines a class for a Neural network
    """

    def __init__(self, train_file=train_file, weights_from_file=False):
        """
        :param train_file: file with training data
        :param weights_from_file: whether read weights from file
        """
        self.x, self.y = self.init_input_and_output(train_file)
        self.w = self.init_weights(self.x.shape[1],
                                   self.y.shape[1],
                                   weights_from_file)

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

        def _create_int_array(lines):
            return np.array([[int(item) for item in l.split()] for l in lines])

        with open(file, 'r') as f:
            lines = [l.replace('\n', '') for l in f.readlines()]

        x_lines = lines[1:lines.index('#output')]
        y_lines = lines[lines.index('#output')+1:]

        X = _create_int_array(x_lines)
        # add bias in X[0]
        extended_ones = np.ones((X.shape[0], X.shape[1]+1))
        extended_ones[:, 1:] = X
        X = extended_ones
        Y = _create_int_array(y_lines)
        return X, Y

    @staticmethod
    def trans_function(x, derivative=False):
        if derivative:
            return x*(1-x)
        else:
            return 1/(1+np.exp(-x))

    def calculate_weights(self):
        """
        calculates weights for network
        """
        self.errors = []
        print("Calculating weights")
        for i in xrange(10000):
            w = self.w
            x = self.x
            # input of input layer Px(N+1)
            input0 = x
            # input of second layer (Mx(N+1))x((N+1)xP) -> MxP
            input1 = np.dot(w, input0.T)
            # output of second layer MxP
            result = self.trans_function(input1)
            error = self.y.T - result
            self.errors.append(error)
            delta_error = error*self.trans_function(result, True)
            w += np.dot(delta_error, input0)

        print("Calculated weights: ")
        print(w)
        print('Done!')
        self.w = w

    def draw_errors(self):
        """
        Draws graph with errors
        """
        ylim(-1, 1)
        outputs = []
        # 0..m
        for k in xrange(len(self.errors[0])):
            v = []
            # 0..p
            for j in xrange(len(self.errors[0][0])):
                m = []
                # 0..i
                for i in xrange(len(self.errors)):
                    m.append(self.errors[i][k][j])
                v.append(m)
            outputs.append(v)

        for ou in outputs:
            for i, item in enumerate(ou):
                subplot(220+i)
                plot(item)
        show()
