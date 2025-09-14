# NOTE: using 1080p resolution
import sys.argv
import shutil

ARG_1 = "test-head.png"

# parameters
if len(sys.argv) > 1:
    ARG_1 = sys.argv[1]

# RESET ZOOM
type("0", Key.CTRL)
sleep(0.5)

# TAKE SCREENSHOTS
screen = Screen()

# HEADER
type(Key.HOME)
sleep(0.5)
region = Region(390, 190, 1190 - 390, 668 - 190)
file = screen.saveCapture(region)

# moves img to destination
shutil.move(file, file + "-head.png")

print("Saved screen as " + file)