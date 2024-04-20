if exists("20240420_175941-screenshot.png"):
    do_nothing = 1
else:
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    keyDown("m")
    
    keyUp(Key.CTRL)
    keyUp(Key.SHIFT)
    keyUp("m")
    
    wait("20240420_175941-screenshot.png")