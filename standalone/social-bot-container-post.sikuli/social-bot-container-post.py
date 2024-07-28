# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_POST_ID = "20210112_233929"
ARG_TXT = ARG_POST_ID + " #pet #cat #tabbycat @frimoussethecat (o.o)"
ARG_IMG_DIR = "file://///192.168.8.2/workdir/project-frimousse-social"
ARG_IMG_NAM = ARG_POST_ID + "-compressed.jpg"
ARG_IMG = ARG_IMG_DIR + "/" + ARG_IMG_NAM
ARG_FFC_ID = "4"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    
    # twitter
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-mobile")
    runScript("../platform/twitter-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/twitter-post", ARG_TXT, "true")
     
    # instagram
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-mobile")
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)
    
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
