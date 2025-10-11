# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_POST_ID = "20221002_221638"
ARG_TXT = ARG_POST_ID + " #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/workdir/project-frimousse-social/" + ARG_POST_ID + "-compressed.jpg"
ARG_FFC_ID = "4"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')

    # instagram
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", ARG_TXT, ARG_IMG_FN)
    
    # twitter
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post", ARG_TXT, ARG_IMG_FN)
     
    # facebook
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post", ARG_TXT, ARG_IMG_FN)

    # tumblr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/tumblr-open")
    runScript("../platform/tumblr-post", ARG_TXT, ARG_IMG_FN)
 
    # flickr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/flickr-open")
    runScript("../platform/flickr-post", ARG_TXT, ARG_IMG_FN)
    
    # mastodon
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/mastodon-open")
    runScript("../platform/mastodon-post", ARG_TXT, ARG_IMG_FN)

    # cara
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/cara-open")
    runScript("../platform/cara-post", ARG_TXT, ARG_IMG_FN)

    # FIXME next: empty tab 
    sleep(5)
    
    # threads
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/threads-open")
    runScript("../platform/threads-post", ARG_TXT, ARG_IMG_FN)   
    
    # bluesky
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")

    # end ***********************************************

finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
