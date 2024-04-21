import random

ARG_TWEET ="https://twitter.com/FremontGames/status/1782034295000854614"
ARG_BOTS = ["3", "4", "5", "6", "7", "8", "9", "0"]

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
