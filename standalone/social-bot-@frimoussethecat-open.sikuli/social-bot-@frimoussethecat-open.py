# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_FFC_ID = "4"
ARG_FFC_ID_2 = "3"
ARG_FFC_ID_3 = "8"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')

    # @MainAccount
    
    # instagram
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.instagram.com/frimousse_the_cat/")
    # twitter
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://x.com/frimoussethecat/")
    # tiktok
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.tiktok.com/@frimousse_the_cat")
    # youtube
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.youtube.com/@FrimousseTheCat")
    # facebook
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.facebook.com/frimoussethecat/")
    # linkedin
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.linkedin.com/in/frimoussethecat/")
    # mastodon
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://mastodon.social/@frimoussethecat")
    # cara
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://cara.app/frimoussethecat")
    # threads
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.threads.net/@frimousse_the_cat")
    # vimeo
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://vimeo.com/frimoussethecat")
    # tumblr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.tumblr.com/frimoussethecat")
    # flickr
    runScript("../platform/firefox-container-new", ARG_FFC_ID)
    runScript("../platform/firefox-url-goto", "https://www.flickr.com/photos/frimoussethecat/")

    # @Account1
    # twitter
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://x.com/frimoussethecat/")
    # youtube
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://www.youtube.com/@FrimousseTheCat")
    # facebook
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://www.facebook.com/frimoussethecat/")
    # mastodon
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://mastodon.social/@frimoussethecat")
    # cara
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://cara.app/frimoussethecat")
    # bluesky
    runScript("../platform/firefox-tab-new")
    runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")
    
    # @Account2
    # instagram
    runScript("../platform/firefox-container-new", ARG_FFC_ID_2)
    runScript("../platform/firefox-url-goto", "https://www.instagram.com/frimousse_the_cat/")
    # twitter
    runScript("../platform/firefox-container-new", ARG_FFC_ID_2)
    runScript("../platform/firefox-url-goto", "https://x.com/frimoussethecat/")
    # youtube
    runScript("../platform/firefox-container-new", ARG_FFC_ID_2)
    runScript("../platform/firefox-url-goto", "https://www.youtube.com/@FrimousseTheCat")
    # facebook
    runScript("../platform/firefox-container-new", ARG_FFC_ID_2)
    runScript("../platform/firefox-url-goto", "https://www.facebook.com/frimoussethecat/")
    
    # @Account3
    # youtube
    runScript("../platform/firefox-container-new", ARG_FFC_ID_3)
    runScript("../platform/firefox-url-goto", "https://www.youtube.com/@FrimousseTheCat")
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
