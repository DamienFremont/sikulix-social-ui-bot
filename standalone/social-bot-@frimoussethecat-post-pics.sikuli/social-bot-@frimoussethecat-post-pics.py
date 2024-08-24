# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_POST_ID = "20210622_180936"
ARG_TXT = ARG_POST_ID + " #pet #cat #tabbycat #montreal #canada @frimoussethecat (o.o)"
ARG_IMG_DIR = "file:c:/workdir/project-frimousse-social"
ARG_IMG_NAM = ARG_POST_ID + "-compressed.jpg"
ARG_IMG = ARG_IMG_DIR + "/" + ARG_IMG_NAM
ARG_FFC_ID = "4"

try:
    # start ***********************************************

    # POST ************************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    
    # instagram
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)
    
    # twitter
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/twitter-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/twitter-post", ARG_TXT, "true")
     
    # facebook
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/facebook-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/facebook-post", ARG_TXT, "true")
    
    # tumblr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/tumblr-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/tumblr-post", ARG_TXT, "true")

    # flickr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/flickr-open")
    runScript("../platform/flickr-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)

    # mastodon
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/mastodon-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/mastodon-post", ARG_TXT, "true")

    # cara
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/cara-open")
    runScript("../platform/cara-post", ARG_TXT, ARG_IMG_DIR, ARG_IMG_NAM)

    # threads
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
#    runScript("../platform/firefox-mobile")
    runScript("../platform/threads-open")
    runScript("../platform/firefox-clipboard-picture", ARG_IMG)
    runScript("../platform/threads-post", ARG_TXT, "true")

    # CHECK ************************************************

    # "delimiter"
    runScript("../platform/firefox-tab-new")
    
    # instagram
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.instagram.com/frimousse_the_cat/")
    # twitter
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://x.com/frimoussethecat/")
    # facebook
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.facebook.com/frimoussethecat/")
    # mastodon
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://mastodon.social/@frimoussethecat")
    # cara
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://cara.app/frimoussethecat")
    # threads
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.threads.net/@frimousse_the_cat")
    # tumblr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.tumblr.com/frimoussethecat")
    # flickr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.flickr.com/photos/frimoussethecat/")
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
