import sys.argv

arg1_text = "20211231_999999 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20211231_999999-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:

    # page loaded
    wait("fb-post-create.png", 30)
    
    # post
    click("fb-post-create.png")
    sleep(1)
    
    wait("facebook-post-form.png", 10)
      
    # add text
    paste(arg1_text)
    
    sleep(1)
        
    # upload picture
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    sleep(2)
        
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)
        
    # submit
    click("facebook-post-confirm.png")
    
    # SUCCESS
    # TODO
        
finally:
    runScript("../platform/windows-takescreenshot", "-facebook")
    keyUp()
