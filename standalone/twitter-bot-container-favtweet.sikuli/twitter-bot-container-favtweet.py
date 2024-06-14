# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

import random

ARG_TWEET ="https://x.com/FremontGames/status/1800508167400640528"
ARG_BOTS = ["3", "4", "5", "6", "7", "8", "9"]

# browser
runScript("../platform/cmd-run", 'firefox')

# account activity
for i in ARG_BOTS:
    try:
        # start *********************************************** 
            
        # browser
        runScript("../platform/firefox-container-open", i)
        runScript("../platform/firefox-mobile")
    
        # twitter
        #runScript("../platform/twitter-open")
        
        # like and repost
        
        runScript("../platform/firefox-focus-addressbar")
        paste(ARG_TWEET)
        type(Key.ENTER)
        sleep(2)
         
        runScript("../platform/twitter-like")        
        runScript("../platform/twitter-repost")

        # end ***********************************************
        runScript("../platform/windows-takescreenshot", "-success") 
    except FindFailed:
        runScript("../platform/windows-takescreenshot", "-error")
    finally:
        keyUp()
        
# browser
#runScript("../platform/window-close.sikuli")
