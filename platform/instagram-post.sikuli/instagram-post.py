import sys.argv

arg1_text = "20220730_220243 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/"
arg3_img_fn ="20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

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
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
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
    paste(arg1_text)
    
    # submit
    click("insta-post-submit.png")
    
    # SUCCESS
    wait("insta-post-submit-confirm.png", 30)
    
    # ERROR: already reposted, cancel
    # TODO
    
    sleep(1)

finally:
    runScript("../platform/windows-takescreenshot", "-instagram")
    keyUp()
