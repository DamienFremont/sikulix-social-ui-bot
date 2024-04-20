import sys.argv

arg1 = 1

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

# start container
keyDown(Key.ALT)
keyDown("f")

wait("1684095972694.png")

keyUp(Key.ALT)
keyUp("f")

click("1684095972694.png")

wait("1684102548812.png")

type(Key.RIGHT)
sleep(1)

type(Key.DOWN * int(arg1))
sleep(1)

type(Key.ENTER)
