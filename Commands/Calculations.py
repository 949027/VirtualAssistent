from scipy.optimize import root
import numpy as np
import matplotlib.pyplot as plt
from Commands import *
import re

class Calculations(AbstractCommand):
    def __init__(self):
        self._match = None

    @property
    def name(self) -> str:
        return 'CALCULATIONS'

    @property
    def help(self) -> str:
        return 'Calculation of the first root "cos (x) / x = c"\nFor example: CALCULATIONS\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name}$', command)
        return bool(self._match)

    def execute(self):
        c = 0.5

        def func_cos(x, c):
            return np.cos(x) / x - c

        crange = range(1, 2)
        res = [root(func_cos, c, args=(ci,)).x[0] for ci in crange]
        print('Root of the equation cos(x) / x = c  -->', res)
        y = lambda x: np.cos(x) / x - c
        fig = plt.subplots()
        x = np.linspace(-30, 30, 100)
        plt.plot(x, y(x))
        plt.show()