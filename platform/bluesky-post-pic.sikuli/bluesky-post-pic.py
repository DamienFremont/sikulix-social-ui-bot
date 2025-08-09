import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:
    
    # page loaded
    wait("bluesky-post-btn.png", 30)
    
    # post
    click("bluesky-post-btn-1.png")
    
    # post loaded
    wait("bluesky-post-confirm-no.png", 10)
    
    # add text
    sleep(1)
    click("bluesky-post-txt.png")
    paste(ARG_TXT)
    
    # upload picture
    click("bluesky-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)
    
    # submit
    wait("bluesky-post-confirm-yes.png", 30)
    click("bluesky-post-confirm-yes-1.png")

    # success
    wait("bluesky-post-comfirmed.png", 30)

finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()