# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_IDS = [ "20210802_220702" ]
ARG_TEXT  = " - Meow in Montreal, CANADA. #pet #cat #canada #frimoussethecat"
ARG_TITLE = " - Meow in Montreal, CANADA."
ARG_DESCR = " - Check me at https://linktr.ee/frimoussethecat #pet #cat #canada #frimoussethecat"
ARG_PATH = "file:c:/Users/damien/workspace/project-frimousse-social/_ARCHIVE/2021/"
FF_CONT = "4"

# START ***********************************************

# browser
runScript("../platform/cmd-run", 'firefox')    
runScript("../platform/windows-fullscreen")
        
for ARG_ID in ARG_IDS:    
    # VARS
    POST_IMAGE = ARG_PATH + ARG_ID + "-compressed.jpg"
    POST_TEXT =  ARG_ID + ARG_TEXT
    POST_TITLE = ARG_ID + ARG_TITLE
    POST_DESCR = ARG_ID + ARG_DESCR
    try:
        # sites
        
        # pinterest
        runScript("../platform/firefox-container-new", FF_CONT)
        runScript("../platform/pinterest-open")
        runScript("../platform/pinterest-post-pic", POST_TITLE, POST_IMAGE, POST_DESCR)
    
        # imgur
        runScript("../platform/firefox-container-new", FF_CONT)
        runScript("../platform/imgur-open")
        runScript("../platform/imgur-post-pic", POST_TITLE, POST_IMAGE, POST_DESCR)
    
        # bluesky
        runScript("../platform/firefox-container-new", FF_CONT)
        runScript("../platform/bluesky-open")
        runScript("../platform/bluesky-post-pic", POST_TEXT, POST_IMAGE)

    finally:
        runScript("../platform/windows-takescreenshot", "-frimoussethecat")
        keyUp()

# CHECK ***********************************************
        
# browser
runScript("../platform/cmd-run", 'firefox')

# sites
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://fr.pinterest.com/frimoussethecat/_pins/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://imgur.com/user/frimoussethecat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://bsky.app/profile/frimoussethecat.bsky.social")
