# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_IMAGE = "20260206_152100-gb.512.gif"
ARG_TITLE = "Testing stuff..."
ARG_DESCR = " #gamedev #retro #demake"
ARG_PATH = "file:c:/Users/damien/workspace/project-demake/_MARKETING/"
FF_CONT = "5"

# VARS
POST_IMAGE = ARG_PATH + ARG_IMAGE
POST_TITLE = ARG_TITLE
POST_DESCR = ARG_DESCR
POST_TEXT =  ARG_TITLE + ARG_DESCR

try:
    # START ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')    
    runScript("../platform/windows-fullscreen")
    
    # facebook
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post", POST_TEXT, POST_IMAGE)
    
    # twitter
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post", POST_TEXT, POST_IMAGE)
    
    # mastodon
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/mastodon-open")
    #runScript("../platform/mastodon-post", POST_TEXT, POST_IMAGE)
    
    # bluesky
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")

    # CHECK ***********************************************
    
    # browser    
    #runScript("../platform/cmd-run", 'firefox')
    # sites

    
    # END ***********************************************
finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
