#This the main program file for TranSIM VR experimentation

import sys,argparse
import math, pygame
from VRTest import vrTest
from circles import OscillatingCircle
from display import Display

def main():
    parser = argparse.ArgumentParser(description='Choose which test to run.')
    parser.add_argument('-o','--osc',action="store_true",dest="oscillating")
    parser.add_argument('-d', '--dots', action="store_true", dest="dots")
    parser.add_argument('-v','--vr',action="store_true", dest="virtual", default=True)
    args = parser.parse_args()

    if args.oscillating:
        running = True
        ticks = 0

        display = Display(1570, 800, (0, 0, 0))
        osc = OscillatingCircle(display.get_display(), (0, 255, 0), display.get_width() / 2, display.get_height() / 2,
                                display.get_height() / 2, 1)

        while running:
            ticks = ticks + 1

            display.update_display()
            osc.display_circle(ticks)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            display.get_clock().tick(60)

    elif args.dots:
        print("Start dots.")

    elif args.virtual:
        app = vrTest()  # creates instance of program class
        app.run()  # runs program class


if __name__ == "__main__":
    main()