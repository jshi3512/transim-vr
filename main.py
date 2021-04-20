#This the main program file for TranSIM VR experimentation

import sys,argparse, time
import math, pygame
from VRTest import vrTest
from circles import OscillatingCircle
from display import Display
from movingDots import MovingDots

def main():
    parser = argparse.ArgumentParser(description='Choose which test to run.')
    parser.add_argument('-o','--osc',action="store_true",dest="oscillating")
    parser.add_argument('-d', '--dots', action="store_true", dest="dots")
    parser.add_argument('-v','--vr',action="store_true", dest="virtual", default=True)
    args = parser.parse_args()

    if args.oscillating:
        fps = 60
        display = Display(1570, 800, (0, 0, 0))
        osc = OscillatingCircle(display.get_display(), (0, 255, 0), display.get_width() / 2, display.get_height() / 2,
                                display.get_height() / 2, 1, fps)
        display.run_oscillating(osc, fps)

    elif args.dots:
        display = Display(1570, 800, (0, 0, 0))
        dots = MovingDots(display.get_display(), (0, 255, 0), display.get_width(), display.get_height()/2, 20)
        display.run_dots(dots)

    elif args.virtual:
        app = vrTest()  # creates instance of program class
        app.run()  # runs program class


if __name__ == "__main__":
    main()