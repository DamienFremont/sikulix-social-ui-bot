# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_POST_ID = "20210117_205357"
ARG_TITLE = ARG_POST_ID + " #pet #cat #tabbycat @frimoussethecat (o.o)"
ARG_IMG_DIR = "file://///192.168.8.2/workdir/project-frimousse-social"
ARG_IMG_NAM = ARG_POST_ID + "-x265_new.mp4"
ARG_IMG = ARG_IMG_DIR + "/" + ARG_IMG_NAM
ARG_FFC_ID = "4"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    
    # youtube
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/youtube-open")
    runScript("../platform/youtube-post-vid", ARG_TITLE, ARG_IMG_DIR, ARG_IMG_NAM)
    
    # twitter
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-mobile")
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post-vid", ARG_TITLE, ARG_IMG_DIR, ARG_IMG_NAM)
        
    # facebook
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-mobile")
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post-vid", ARG_TITLE, ARG_IMG_DIR, ARG_IMG_NAM)

    # vimeo
    #runScript("../platform/firefox-container-open", ARG_FFC_ID)
    #runScript("../platform/firefox-mobile")
    #runScript("../platform/vimeo-open")
    # TODO runScript("../platform/vimeo-post-vid", ARG_TITLE, ARG_IMG_DIR, ARG_IMG_NAM)
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
