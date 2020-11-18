import re
import numpy as np
import matplotlib.pyplot as plt


class Linear_Algebra(object):
    def plot_linear(self, formula):
        if isinstance(formula, str):
            formula = [formula]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        x = np.linspace(-5, 5, 100)
        for i, item in enumerate(formula):
            plt.plot(x, eval(item), color=np.random.rand(3,),
                     label='y={0}'.format(item))
        plt.legend(loc='upper left')
        plt.savefig('test/img/demo.png')

    @staticmethod
    def get_cmap(n, name='hsv'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)

    @staticmethod
    def convert_equations(m, r, v=None):
        if v is None:
            v = ['x', 'y', 'z']

        cols = len(v)
        l = []
        for index, item in enumerate(m):
            s = ''
            for ind, it in enumerate(item):
                if it:
                    if it == 1:
                        coef = ''
                    elif it == -1:
                        coef = '-'
                    else:
                        coef = str(it)
                    if ind+1 == cols:
                        sign = ''
                    else:
                        sign = '+' if item[ind+1] >= 0 else ''
                    s += coef + v[ind]+sign
            l.append(s+'='+str(r[index]))
        return l

    @staticmethod
    def solve(s):
        l = re.split(r'\n', s)
        l_r = map(lambda item: re.split(r'=', item), l)
        left = []
        right = []
        for item in l_r:
            l = item[0]
            r = item[1]
            coefs = list(map(lambda it: it if re.search(r'\d', it)
                             else '1', re.findall(r'(\d+|\s|^)\w', l)))
            result = re.search(r'(\d+)', r).group()
            left.append(coefs)
            right.append(result)
            print(coefs)
        x = np.linalg.solve(left, right)
        return x
