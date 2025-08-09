import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:

    # page loaded
    wait("insta-post-create-btn.png", 30)
    
    # post
    click("insta-post-create-btn.png")
    sleep(1)

    click("insta-post-post.png")
    
    # upload picture
    click("insta-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)
    
    # next...
    click("insta-post-next.png")
    sleep(1)
    click("insta-post-next.png")
    sleep(1)
    
    # type text
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    paste(ARG_TXT)
    
    # submit
    click("insta-post-submit.png")
    
    # SUCCESS
    wait("insta-post-submit-confirm.png", 30)    
    sleep(1)

finally:
    runScript("../platform/windows-takescreenshot", "-instagram")
    keyUp()
