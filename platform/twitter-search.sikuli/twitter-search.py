import sys.argv

arg1 = "#gaming"

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

if exists("20240420_180530-screenshot.png"):
    click("20240420_180530-screenshot.png")

sleep(1)

if exists("20240420_173932-screenshot.png"):
    click("20240420_173932-screenshot.png")

sleep(1)

type(arg1)
type(Key.ENTER)

sleep(2)
