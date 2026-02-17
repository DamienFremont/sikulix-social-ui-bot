# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_ID    = "20230415_184614"
ARG_TEXT  = " - Meow in Nantes, FRANCE. #pet #cat #france #frimoussethecat"
ARG_TITLE = " - Meow in Nantes, FRANCE."
ARG_DESCR = " - Meow in Nantes, FRANCE. Check me at https://linktr.ee/frimoussethecat #pet #cat #france #frimoussethecat"
ARG_PATH = "file:c:/Users/damien/workspace/project-frimousse-social/"
FF_CONT = "4"

# VARS
POST_IMAGE = ARG_PATH + ARG_ID + "-compressed.jpg"
POST_TEXT =  ARG_ID + ARG_TEXT
POST_TITLE = ARG_ID + ARG_TITLE
POST_DESCR = ARG_ID + ARG_DESCR

try:
    # START ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')    
    runScript("../platform/windows-fullscreen")
    
    # facebook
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post", POST_TEXT, POST_IMAGE)
    
    # instagram
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", POST_TEXT, POST_IMAGE)
    
    # twitter
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post", POST_TEXT, POST_IMAGE)

    # pinterest
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/pinterest-open")
    #runScript("../platform/pinterest-post-pic", ARG_TXT, ARG_IMG_FN)
    
    # imgur
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/imgur-open")
    #runScript("../platform/imgur-post-pic", ARG_TXT, ARG_IMG_FN)
    
    # tumblr
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/tumblr-open")
    runScript("../platform/tumblr-post", POST_TEXT, POST_IMAGE)
 
    # flickr
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/flickr-open")
    runScript("../platform/flickr-post", POST_TITLE, POST_IMAGE, POST_DESCR)
    
    # mastodon
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/mastodon-open")
    runScript("../platform/mastodon-post", POST_TEXT, POST_IMAGE)

    # cara
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/cara-open")
    runScript("../platform/cara-post", POST_TEXT, POST_IMAGE)
    # FIXME next: empty tab 
    sleep(5)
    
    # threads
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/threads-open")
    runScript("../platform/threads-post", POST_TEXT, POST_IMAGE)   
    
    # bluesky
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")

    # CHECK ***********************************************
    
    # browser    
    runScript("../platform/cmd-run", 'firefox')
    # sites

    
    # END ***********************************************
finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
