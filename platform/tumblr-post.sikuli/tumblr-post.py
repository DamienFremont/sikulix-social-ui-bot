import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:
    
    # page loaded    
    wait("tumblr-post-create-2.png", 30)

    # post
    click("tumblr-post-create-2.png")
    click("tumblr-post-create-txt.png")
    wait("tumblr-post-create-txt2-1.png", 30)

    # add text
    sleep(1)
    paste(ARG_TXT)
    sleep(1)
    type(Key.ENTER)

    # upload picture   
    click("tumblr-post-create-txt2.png")
    click("tumblr-post-upload2.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)
    
    # uploaded
    wait("tumblr-post-submit-2.png", 30)
    
    
    # submit
    click("tumblr-post-submit-2.png")
    
    #confirm
    sleep(2)
    if exists("tumblr-post-confirm2.png"):
        click("tumblr-post-confirm2-1.png")
    sleep(1)
        
finally:
    runScript("../platform/windows-takescreenshot", "-tumblr")
    keyUp()
