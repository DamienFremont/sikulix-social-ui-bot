# NOTE: using 1080p resolution
import sys.argv
import shutil

# CONST
ARG_1 = "test-head.png"
ARG_VERTICAL_MARGIN = "0"

# parameters
if len(sys.argv) > 1:
    ARG_1 = sys.argv[1]
    ARG_VERTICAL_MARGIN = sys.argv[2]

# RESET ZOOM
type("0", Key.CTRL)
sleep(0.5)

# TAKE SCREENSHOTS
screen = Screen()

type(Key.HOME)
sleep(0.5)

x1 = 390
y1 = 78
x2 = 1190
y2 = 555

x = x1
y = y1 + int(ARG_VERTICAL_MARGIN)
w = x2 - x1
h = y2 - y

region = Region(x, y, w, h)
file = screen.saveCapture(region)

# moves img to destination
shutil.move(file, file + "-" + ARG_1)

print("Saved screen as " + file)