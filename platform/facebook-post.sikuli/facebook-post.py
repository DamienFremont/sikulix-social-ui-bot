import sys.argv

arg1_text = "20211230_234721 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20211230_234721-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:
    
    # post
    click("fb-post-create.png")
    sleep(1)
    
    wait("facebook-post-form.png")
      
    # add text
    paste(arg1_text)
    
    # upload picture
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    sleep(1)
        
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    
    sleep(5)
        
    # submit
    type(Key.TAB, KEY_SHIFT)
    type(Key.TAB, KEY_SHIFT)
    type(Key.TAB, KEY_SHIFT)
    type(Key.TAB, KEY_SHIFT)
    type(Key.TAB, KEY_SHIFT)
    type(Key.ENTER)
    
    # SUCCESS
    # TODO
    
    # ERROR: already reposted, cancel
    # TODO
        
finally:
    runScript("../platform/windows-takescreenshot", "-facebook")
    keyUp()
