# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_FFC_ID = "4"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    
    # instagram
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.instagram.com/frimousse_the_cat/")
    
    # twitter
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://x.com/frimoussethecat/")

    # tiktok
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.tiktok.com/@frimousse_the_cat")
   
    # youtube
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.youtube.com/@FrimousseTheCat")
    
    # facebook
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.facebook.com/frimoussethecat/")

    # linkedin
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.linkedin.com/in/frimoussethecat/")

    # mastodon
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://mastodon.social/@frimoussethecat")
    
    # cara
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://cara.app/frimoussethecat")
    
    # threads
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.threads.net/@frimousse_the_cat")

    # vimeo
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://vimeo.com/frimoussethecat")
    
    # tumblr
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.tumblr.com/frimoussethecat")

    # flickr
    runScript("../platform/firefox-container-open", ARG_FFC_ID)
    runScript("../platform/firefox-url-open", "https://www.flickr.com/photos/frimoussethecat/")
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
