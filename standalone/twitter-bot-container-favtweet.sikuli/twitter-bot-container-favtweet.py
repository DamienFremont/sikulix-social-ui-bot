import random

ARG_TWEET ="https://x.com/FremontGames/status/1795846372186533907"
ARG_BOTS = ["3", "4", "5", "6", "7", "8", "9"]

# browser
runScript("../platform/cmd-run", 'firefox')

# account activity
for i in ARG_BOTS:
    
    # browser
    runScript("../platform/firefox-container-open", i)
    runScript("../platform/firefox-mobile")

    # twitter
    #runScript("../platform/twitter-open")
    
    # like and repost
    
    runScript("../platform/firefox-focus-addressbar")
    type(ARG_TWEET)
    type(Key.ENTER)
    sleep(2)
     
    runScript("../platform/twitter-like")        
    runScript("../platform/twitter-repost")

# browser
#runScript("../platform/window-close.sikuli")
