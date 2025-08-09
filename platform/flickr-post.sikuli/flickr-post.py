import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:

    # post
    click("flickr-post-create.png")
    sleep(1)

    # upload picture
    click("flickr-file-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)

    # type text
    click("flickr-post-desc.png")
    type(Key.TAB, KeyModifier.SHIFT)
    paste(ARG_TXT)

    # submit
    click("flickr-post-submit-1.png")
    click("flickr-post-submit2.png")
    sleep(1)

    # success
    wait("flickr-post-continue.png")
    click("flickr-post-continue-1.png")
    
finally:
    runScript("../platform/windows-takescreenshot", "-flickr")
    keyUp()
