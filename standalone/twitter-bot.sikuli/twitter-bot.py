# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

import random

ARG_SEARCH = "#today"

# browser
runScript("../platform/cmd-run", 'firefox')
runScript("../platform/firefox-mobile")

# twitter
runScript("../platform/twitter-open")

# home then like
runScript("../platform/twitter-click-home")
random_like = random.randint(1, 3);
for x in range(random_like):    
    runScript("../platform/twitter-like")
    sleep(2)
    #runScript("../platform/twitter-scroll-down"
    random_scroll = random.randint(1, 3);            
    for y in range(random_scroll):    
        sleep(1)
        type(Key.PAGE_DOWN)
    sleep(1)
        
# search then like and repost
runScript("../platform/twitter-search", ARG_SEARCH)
random_like = random.randint(1, 3);    
for x in range(random_like):    
    runScript("../platform/twitter-like")        
    # runScript("../platform/twitter-repost")
    sleep(2)
    #runScript("../platform/twitter-scroll-down")    
    random_scroll = random.randint(1, 3);            
    for y in range(random_scroll):    
        sleep(1)
        type(Key.PAGE_DOWN)
    sleep(1)

# browser
# runScript("../platform/window-close.sikuli")
