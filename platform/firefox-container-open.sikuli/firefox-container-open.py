import sys.argv

arg1 = 1

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

# start container
keyDown(Key.CTRL)
keyDown(Key.SHIFT)
keyDown(arg1)

keyUp(Key.CTRL)
keyUp(Key.SHIFT)
keyUp(arg1)
