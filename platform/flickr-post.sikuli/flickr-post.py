import sys.argv

ARG_TITLE = "TEST #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:c:/Users/damien/workspace/project-frimousse-social/folder.jpg"
ARG_DESCR = "20110001 #pet #cat #tabbycat #france @frimoussethecat (o.o https://linktr.ee/frimoussethecat)"

# parameters
if len(sys.argv) > 1:
    ARG_TITLE = sys.argv[1]
    ARG_IMAGE = sys.argv[2]
    ARG_DESCR = sys.argv[3]

try:

    # post
    click("flickr-post-create.png")
    sleep(1)

    # upload picture
    click("flickr-file-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(1)

    # type description
    click("flickr-post-desc.png")
    paste(ARG_DESCR)
    
    # type title
    type(Key.TAB, KeyModifier.SHIFT)
    paste(ARG_TITLE)

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
