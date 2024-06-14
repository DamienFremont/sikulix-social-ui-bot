# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

import random

ARG_BOTS = ["3"]
ARG_BOTS = ["3", "4", "5", "6", "7", "8", "9"]

# browser
runScript("../platform/cmd-run", 'firefox')

# account activity
for i in ARG_BOTS:
    try:
        # start ***********************************************
        
        # browser
        runScript("../platform/firefox-container-open", i)
    
        # twitter
        runScript("../platform/twitter-open")
        
        # nav to followers
        click("20240613_152159-screenshot.png")
        click("20240613_152307-screenshot.png")
        
        # follow back "verified followers"
        random_follow = random.randint(1, 3);    
        for x in range(random_like):
            sleep(1)
            click("20240613_152525-screenshot.png")
    
        # follow back "verified followers"
        click("20240613_152615-screenshot.png")
        random_follow = random.randint(1, 3);    
        for x in range(random_like):
            sleep(1)
            click("20240613_152525-screenshot.png")
            
        # end *********************************************** 
        runScript("../platform/windows-takescreenshot", "-success") 
    except FindFailed:
        runScript("../platform/windows-takescreenshot", "-error")
    finally:
        keyUp()

# browser
#runScript("../platform/window-close.sikuli")