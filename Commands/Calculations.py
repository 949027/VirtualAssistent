from Commands import *
import re
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
import warnings


class Calculations(AbstractCommand):
    def __init__(self):
        self._match = None

    @property
    def name(self) -> str:
        return 'CALC'

    @property
    def help(self) -> str:
        return 'Calculation one of the roots of an equation like f(x) = 0 in a given interval. All characters must be lowercase\nFor example: CALC sin(x) -1.00 1.00\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\S+) (\S+.\d+) (\S+.\d+)$', command)
        return bool(self._match)

    def execute(self):
        def opt_fun(x):
            return ((eval(input_replace) ** 2))

        input = self._match.group(1)
        x1 = float(self._match.group(2))
        x2 = float(self._match.group(3))

        try:
            input_replace = input.replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan').replace('sqrt', 'np.sqrt')
            res = minimize(lambda x: opt_fun(x), x0=0.001, bounds=[(x1, x2)])
        except:
            print('Error! Check if the equation is correct')
            return()

        if float(res.x[0]) == x1 or float(res.x[0]) == x2:
            delta = (x2 - x1) / 3
            x1 += delta
            x2 -= delta
            res = minimize(lambda x: opt_fun(x), x0=0.001, bounds=[(x1, x2)])

            if float(res.x[0]) == x1 or float(res.x[0]) == x2:
                print('No roots of the equation in this section')
                return()
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        print('Finded root of equation "', input_replace, '= 0 "  --> ', round(res.x[0], 2))


        y = lambda x: (eval(input_replace))
        fig = plt.subplots()
        x = np.linspace(float(x1), float(x2), 10000)
        plt.plot(x, y(x))
        plt.scatter(res.x[0], 0, color='red', s=50, marker='o')
        plt.grid()
        plt.show()