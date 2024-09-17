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
    click("threads-post-create-1.png", 30)
    
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
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    
    # SUCCESS
    # TODO
    
    # ERROR: already reposted, cancel
    # TODO
    
    sleep(1)
    
    runScript("../platform/windows-takescreenshot", "-threads-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-threads-error")
finally:
    keyUp()
