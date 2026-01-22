import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:
    
    # post
    wait("mastodon-post-create.png")
    
    # upload picture
    click("mastodon-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    
    # uploaded
    wait("mastodon-post-uploading.png", 10)
    # wait_notexists(...)
    timeout = 30
    time_cnt = 0
    while(True):
        time_cnt = time_cnt + 1
        if time_cnt > timeout:
            Debug.error('wait_notexists() timeout: ' + str(timeout))
            break
        if exists("mastodon-post-uploading.png"):
            wait(1)
        else:
            break
    
    # add text
    click("mastodon-post-create.png")
    sleep(0.5)
    paste(ARG_TXT)
        
    # submit
    click("mastodon-post-submit-2.png")
    
    # access
    click("mastodon-post-access-3.png")
    sleep(1)


    # check upload
    #wait("mastodon-post-check.png", 120)
    
finally:
    runScript("../platform/windows-takescreenshot", "-mastodon")
    keyUp()

