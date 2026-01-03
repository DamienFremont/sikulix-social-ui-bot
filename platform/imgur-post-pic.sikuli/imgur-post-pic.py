import sys.argv

ARG_TXT = "20110001 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/workspace/project-frimousse-social/20110001-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]
    
try:
    # post
    click("imgur-post-pic-create.png")
    sleep(1)

    # add pict
    click("imgur-post-pic-create-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(3)

    # add text
    click("imgur-post-pic-title.png")
    paste(ARG_TXT)
    sleep(1)

    # submit
    click("imgur-post-pic-publish.png")
    sleep(1)
    
    click("imgur-post-pic-confirm.png")
    
finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()
