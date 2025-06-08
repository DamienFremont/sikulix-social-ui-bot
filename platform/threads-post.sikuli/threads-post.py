import sys.argv

arg1_text = "20220716_151715 #pet #cat #tabbycat #vancouver #canada @frimoussethecat (o.o)"
arg2_img_dir = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/"
arg3_img_fn ="20220716_151715-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]
    
try:

    # page loaded
    wait("threads-post-create-2.png", 30)
    
    # post
    click("threads-post-create-2.png")
    
    # add text
    sleep(1)
    paste(arg1_text)
    
    # upload picture
    click("threads-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)
    
    # submit
    wait("threads-post-confirm.png", 30)
    click("threads-post-confirm.png")
    
    # SUCCESS
    # TODO
    
finally:
    runScript("../platform/windows-takescreenshot", "-threads")
    keyUp()
