if exists("1683902552913.png"):
    click("1683902552913.png")
    sleep(1)    
    
    # SUCCESS
    if exists("1683902610260.png"):
        do_nothing = 1
        
    # ERROR: missclick comment, back
    elif exists("20240420_183320-screenshot.png"):
        keyDown(Key.ALT)
        keyDown(Key.LEFT)
        keyUp(Key.ALT)
        keyUp(Key.LEFT)
        
    sleep(1)