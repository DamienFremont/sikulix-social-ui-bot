import sys.argv

arg1_text = "20220503_130400 #pet #cat #tabbycat #vancouver #canada @frimoussethecat (o.o)"
arg2_img_dir = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/"
arg3_img_fn ="20220503_130400-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:
    
    # page loaded    
    wait("tumblr-post-create-2.png", 30)

    # post
    click("tumblr-post-create-2.png")
    click("tumblr-post-create-txt.png")
    wait("tumblr-post-create-txt2-1.png", 30)

    # add text
    sleep(1)
    paste(arg1_text)
    sleep(1)
    type(Key.ENTER)

    # upload picture   
    click("tumblr-post-create-txt2.png")
    click("tumblr-post-upload2.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)
    
    # uploaded
    wait("tumblr-post-submit-2.png", 30)
    
    
    # submit
    click("tumblr-post-submit-2.png")
    
    #confirm
    sleep(2)
    if exists("tumblr-post-confirm2.png"):
        click("tumblr-post-confirm2-1.png")
    
    # SUCCESS
    # TODO
        
finally:
    runScript("../platform/windows-takescreenshot", "-tumblr")
    keyUp()
