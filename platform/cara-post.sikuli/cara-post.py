import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]
    
try:

    # post
    click("cara-post-create.png")
    sleep(1)

    # type text
    type(Key.TAB)
    paste(ARG_TXT)

    # upload picture
    click("cara-post-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)

    # submit
    click("cara-post-submit.png")
    sleep(1)
    
finally:
    runScript("../platform/windows-takescreenshot", "-cara")
    keyUp()
