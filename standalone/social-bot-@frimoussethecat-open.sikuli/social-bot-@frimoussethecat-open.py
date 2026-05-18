# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
CONT_FRIMOUSSE = "4"
CONT_INDY = "5"
CONT_STREETBOOZE = "6"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')
    runScript("../platform/windows-maximize")
    
    # main Account
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.tiktok.com/@frimousse_the_cat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.instagram.com/frimousse_the_cat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://x.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://fr.pinterest.com/frimoussethecat/_pins/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://imgur.com/user/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.tumblr.com/frimoussethecat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.threads.net/@frimousse_the_cat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.flickr.com/photos/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://mastodon.social/@frimoussethecat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://cara.app/frimoussethecat")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://www.linkedin.com/in/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://bsky.app/profile/frimoussethecat.bsky.social")
    runScript("../platform/firefox-cont-new-url", CONT_FRIMOUSSE, "https://vimeo.com/frimoussethecat")

    runScript("../platform/firefox-tab-new-url", "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-tab-new-url", "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-tab-new-url", "https://x.com/frimoussethecat/")    
    runScript("../platform/firefox-tab-new-url", "https://mastodon.social/@frimoussethecat")
    runScript("../platform/firefox-tab-new-url", "https://cara.app/frimoussethecat")

    runScript("../platform/firefox-cont-new-url", CONT_INDY, "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_INDY, "https://www.youtube.com/@FrimousseTheCat")
    runScript("../platform/firefox-cont-new-url", CONT_INDY, "https://www.instagram.com/frimousse_the_cat/")
    runScript("../platform/firefox-cont-new-url", CONT_INDY, "https://x.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_INDY, "https://www.tumblr.com/frimoussethecat")

    # runScript("../platform/firefox-cont-new-url", CONT_STREETBOOZE, "https://www.facebook.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_STREETBOOZE, "https://www.instagram.com/frimousse_the_cat/")
    runScript("../platform/firefox-cont-new-url", CONT_STREETBOOZE, "https://x.com/frimoussethecat/")
    runScript("../platform/firefox-cont-new-url", CONT_STREETBOOZE, "https://www.tumblr.com/frimoussethecat")

    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()
