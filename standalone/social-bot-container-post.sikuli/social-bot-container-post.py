# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

ARG_TXT = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
ARG_IMG = "file://///192.168.8.2/workdir/project-frimousse-social/20210112_233929-compressed.jpg"
ARG_FFC = "4"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')

    
    # twitter
    runScript("../platform/firefox-container-open", ARG_FFC)
    runScript("../platform/firefox-mobile")
    runScript("../platform/twitter-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/twitter-post", ARG_TXT, "true")
     
    # instagram
    # TODO
    
    # facebook
    # TODO

    # tumblr
    # TODO

    # flickr
    # TODO

    # mastodon
    # TODO

    # cara
    # TODO

    # threads
    # TODO
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
