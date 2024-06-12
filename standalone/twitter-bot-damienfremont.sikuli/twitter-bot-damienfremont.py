# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

import random

ARG_SEARCH = "#gaming"
ARG_BOTS = ["3", "4", "5", "6", "7", "8", "9"]

# browser
runScript("../platform/cmd-run", 'firefox')

# account activity
for i in ARG_BOTS:
    
    # browser
    runScript("../platform/firefox-container-open", i)
    runScript("../platform/firefox-mobile")

    # twitter
    runScript("../platform/twitter-open")
    # like tw from home
#    runScript("../platform/twitter-click-home")
#    random_like = random.randint(1, 3);
#    for x in range(random_like):    
#        runScript("../platform/twitter-like")
#        sleep(2)
#        random_scroll = random.randint(1, 3);            
#        for y in range(random_scroll):    
#            sleep(1)
#            type(Key.PAGE_DOWN)
#        sleep(1)
    # rt  and like from search
    runScript("../platform/twitter-search", ARG_SEARCH)
    random_like = random.randint(1, 3);    
    for x in range(random_like):    
        runScript("../platform/twitter-like")        
        runScript("../platform/twitter-repost")
        sleep(2)
        random_scroll = random.randint(1, 3);            
        for y in range(random_scroll):    
            sleep(1)
            type(Key.PAGE_DOWN)
        sleep(1)
    #runScript("../platform/twitter-click-rt")
    #runScript("../platform/twitter-scroll-down")  
    
exit()

for i in c_all:
    # open container
    runScript("../platform/firefox-container-open", i)
    # twitter 
    sleep(1)
    #runScript("../platform/twitter-open")
    #runScript("../platform/firefox-focus-addressbar")
    type("https://x.com/FremontGames/status/1781653039851450536")
    type(Key.ENTER)
    sleep(2)

# stop browser
#runScript("../platform/window-close.sikuli")
