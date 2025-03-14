# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_POST_ID = "20220420_090635"
ARG_TXT = ARG_POST_ID + " #pet #cat #tabbycat #vancouver #canada @frimoussethecat (o.o)"
ARG_IMG_DIR = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/"
ARG_IMG_NAM = ARG_POST_ID + "-compressed.jpg"
ARG_IMG = ARG_IMG_DIR + "/" + ARG_IMG_NAM
ARG_FFC_ID = "4"

try:
    # start ***********************************************

    # POST ************************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    

    # mastodon
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/mastodon-open")
    runScript("../platform/mastodon-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)

    # cara
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/cara-open")
    runScript("../platform/cara-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)

    # FIXME next: empty tab 
    sleep(5)
    
    # threads
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/threads-open")
    runScript("../platform/threads-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)   


    # end ***********************************************  

finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
