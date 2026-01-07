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
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.tiktok.com/@frimousse_the_cat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.instagram.com/frimousse_the_cat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://x.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://fr.pinterest.com/frimoussethecat/_pins/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://imgur.com/user/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.tumblr.com/frimoussethecat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.threads.net/@frimousse_the_cat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.flickr.com/photos/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://mastodon.social/@frimoussethecat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://cara.app/frimoussethecat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://www.linkedin.com/in/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://bsky.app/profile/frimoussethecat.bsky.social")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID, "https://vimeo.com/frimoussethecat")

    # @Account1
    runScript("../platform/firefox-cont-new-url", "1", "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", "1", "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-cont-new-url", "1", "https://mastodon.social/@frimoussethecat")
    runScript("../platform/firefox-cont-new-url", "1", "https://cara.app/frimoussethecat")

    # @Account2
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID_2, "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID_2, "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID_2, "https://mastodon.social/@frimoussethecat")
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID_2, "https://cara.app/frimoussethecat")

    # @Account3
    runScript("../platform/firefox-cont-new-url", ARG_FFC_ID_3, "https://www.youtube.com/@FrimousseTheCat")
    
    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
