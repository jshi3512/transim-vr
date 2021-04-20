#This the main program file for TranSIM VR experimentation

import sys,argparse
import math, pygame
from VRTest import vrTest

def main():
    parser = argparse.ArgumentParser(description='Choose which test to run.')
    parser.add_argument('-o','--osc',action="store_true",dest="oscillating")
    parser.add_argument('-d', '--dots', action="store_true", dest="dots")
    parser.add_argument('-v','--vr',action="store_true", dest="virtual", default=True)
    args = parser.parse_args()

    if args.oscillating:
        print("Start oscillating.")
    elif args.dots:
        print("Start dots.")
    elif args.virtual:
        app = vrTest()  # creates instance of program class
        app.run()  # runs program class


if __name__ == "__main__":
    main()