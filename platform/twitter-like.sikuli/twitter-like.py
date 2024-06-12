if exists("20240612_095753-screenshot.png"):
    click("20240612_095753-screenshot.png")
    sleep(1)    
    
    # SUCCESS
    if exists("20240612_100024-screenshot.png"):
        do_nothing = 1
        
    # ERROR: missclick comment, back
    elif exists("20240612_095936-screenshot.png"):
        keyDown(Key.ALT)
        keyDown(Key.LEFT)
        keyUp(Key.ALT)
        keyUp(Key.LEFT)
        
    sleep(1)