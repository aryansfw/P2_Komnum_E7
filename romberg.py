import pandas as pd
import numpy as np
import math

# R(n, m) = 1/(4^m - 1) * (4^m*R(n, m - 1) - R(n - 1, m - 1))
class Romberg:
    def __init__(self, f, lower_limit, upper_limit, max_steps):
        self.f = f
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.max_steps = max_steps
        self.result = []
        self.best_approximation = 0

    def generate(self):
        self.result = []
        self.best_approximation = 0

        # Step size
        h = self.upper_limit - self.lower_limit

        # First trapezoidal step -> h/2*(f(a) + f(b))
        r0 = h * 0.5 * (self.f(self.upper_limit) + self.f(self.lower_limit))
        self.result.append([r0])

        # Calculate approximations
        for i in range(1, self.max_steps):
            h /= 2
            points = 2**(i - 1)

            summ = 0
            for j in range(1, points + 1):
                summ += f(self.lower_limit + (2 * j - 1) * h)
            
            # R(i, 0)
            row = [h * summ + 0.5 * self.result[i - 1][0]]

            # R(i, j)
            for j in range(1, i + 1):
                r = (4**j * row[j - 1] - self.result[i - 1][j - 1])/(4**j - 1)
                row.append(r)
                if (j == i):
                    self.best_approximation = r 
            self.result.append(row)
    
    def print_result(self):
        if len(self.result) == 0:
            print("Please generate the values first using generate().")
            return
        # Print table
        print("Integration using Romberg Method:")
        print(pd.DataFrame(self.result,
                            columns=list(range(self.max_steps)),
                            index=list(range(self.max_steps)))
                            .fillna(''))
        # Print best approximation
        print(f"Best approximation of the definite integral is {self.best_approximation:.6f}")
    
    def get_approximation(self):
        return self.best_approximation

def f(x):
    return 1/(1+x)

if __name__ == '__main__':
    romberg = Romberg(f, 0, 1, 5)

    romberg.generate()
    romberg.print_result()