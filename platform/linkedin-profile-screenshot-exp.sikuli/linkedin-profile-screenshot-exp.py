# NOTE: using 1080p resolution
import sys.argv
import shutil

ARG_1 = "test-exp.png"

# parameters
if len(sys.argv) > 1:
    ARG_1 = sys.argv[1]
    
# RESET ZOOM
type("0", Key.CTRL)
sleep(0.5)

# TAKE SCREENSHOTS
screen = Screen()

# EXPERIENCE
type(Key.HOME)
sleep(0.5)
type(Key.PAGE_DOWN)
sleep(0.5)
region = Region(390, 162, 1190 - 390, 1030 - 162)
file = screen.saveCapture(region)

# moves img to destination
shutil.move(file, file + "-" + ARG_1)

print("Saved screen as " + file)