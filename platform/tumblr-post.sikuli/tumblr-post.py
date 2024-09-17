import sys.argv

arg1_text = "20211220_005455 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20211220_005455-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:
    
    # post
    click("tumblr-post-create-1.png", 30)
    wait("tumblr-post-upload.png", 10)
    
    # upload picture
    click("tumblr-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)
    
    # uploaded
    wait("tumblr-post-submit-2.png", 30)
    
    # add text
    click("tumblr-post-text.png")
    paste(arg1_text)
    sleep(1)
    
    # submit
    click("tumblr-post-submit-2.png")
    
    #confirm
    sleep(2)
    if exists("tumblr-post-confirm-tags1.png"):
        click("tumblr-post-confirm-tags2.png")
    
    # SUCCESS
    # TODO
    
    # ERROR: already reposted, cancel
    # TODO
    
    sleep(1)
    
    runScript("../platform/windows-takescreenshot", "-tumblr-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-tumblr-error")
finally:
    keyUp()
