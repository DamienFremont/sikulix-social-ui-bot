import random

# start browser
runScript("../platform/cmd-run", 'firefox')

#containers = ["0"]
#containers = ["0", "11", "10", "2,", "3", "4", "5", "6", "7", "8", "9"]
c_all = ["1", "12", "11", "3", "4", "5", "6", "7", "8", "9", "0"]
c_like = c_all
c_bots = ["3"]

# account activity
for i in c_bots:
    # open container
    runScript("../platform/firefox-container-open", i)
    runScript("../platform/firefox-mobile")
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
    runScript("../platform/twitter-search", "#gaming")
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
    type("https://twitter.com/FremontGames/status/1781653039851450536")
    type(Key.ENTER)
    sleep(2)

# stop browser
#runScript("../platform/window-close.sikuli")
