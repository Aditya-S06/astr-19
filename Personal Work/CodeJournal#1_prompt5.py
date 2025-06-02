import math
import numpy as np

def main():

    xVals = np.linspace(0, 2, 1000)

    for x in xVals:
        y = math.sin(x)
        print(f"x: {x:.4f}    sin(x): {y:.4f}")


if __name__ == "__main__":
    main()