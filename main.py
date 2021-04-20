#This the main program file for TranSIM VR experimentation

import sys,argparse
import math, pygame
from VRTest import vrTest
from circles import OscillatingCircle

def main():
    parser = argparse.ArgumentParser(description='Choose which test to run.')
    parser.add_argument('-o','--osc',action="store_true",dest="oscillating")
    parser.add_argument('-d', '--dots', action="store_true", dest="dots")
    parser.add_argument('-v','--vr',action="store_true", dest="virtual", default=True)
    args = parser.parse_args()

    if args.oscillating:
        print(args.oscillating)
        display = pygame.display.set_mode((1570, 800), flags=pygame.DOUBLEBUF)
        display.fill((0, 0, 0))
        osc = OscillatingCircle(display, (0, 255, 0), 785, 400, 400, 1)
        osc.display_circle()
        exit(0)
    elif args.dots:
        print("Start dots.")
        exit(0)
    elif args.virtual:
        app = vrTest()  # creates instance of program class
        app.run()  # runs program class
        exit(0)

if __name__ == "__main__":
    main()