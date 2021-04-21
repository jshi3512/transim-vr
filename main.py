#Main.py: main function for TranSIM VR experimentation
#This runs all other program files from a single, consolidated main function
#Use command line arguments in terminal to select between programs

import sys,argparse, time
import math, pygame
from VRTest import vrTest
from circles import OscillatingCircle
from display import Display
from movingDots import MovingDots

def main():
    #Command line argument creation through argparse package
    parser = argparse.ArgumentParser(description='Choose which test to run.')
    parser.add_argument('-o','--osc',action="store_true",dest="oscillating") #oscillating circles
    parser.add_argument('-d', '--dots', action="store_true", dest="dots") #random dots
    parser.add_argument('-v','--vr',action="store_true", dest="virtual", default=True) #panda3d VR
    args = parser.parse_args()

    #oscillating circles
    if args.oscillating:
        # caps framerate to 60 fps, REMEMBER to change period in OscillatingCircle if changed
        fps = 60

        display = Display(1570, 800, (0, 0, 0))
        osc = OscillatingCircle(display.get_display(), (0, 255, 0), display.get_width() / 2, display.get_height() / 2,
                                display.get_height() / 2, 1, fps)
        display.run_oscillating(osc, fps)

    #random dots display
    elif args.dots:
        display = Display(1570, 800, (0, 0, 0))
        dots = MovingDots(display.get_display(), (0, 255, 0), display.get_width(), display.get_height()/2, 20)
        display.run_dots(dots)

    #panda3d virtual reality program
    elif args.virtual:
        app = vrTest()  # instances vrtest
        app.run()  # runs vrtest instance


if __name__ == "__main__":
    main()