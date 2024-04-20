if exists("1683903580253.png"):
    click("1683903580253.png")
    sleep(1)
    
    # SUCCESS
    if exists("1683903657940.png"):
        click("1683903657940.png")
        wait("1683903600276.png")
                
    # ERROR: already reposted, cancel
    elif exists("20240420_181641-screenshot.png"):
        click("20240420_181645-screenshot.png")
    
    sleep(1)