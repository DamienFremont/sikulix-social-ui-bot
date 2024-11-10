import sys.argv

arg1_text = "20200112_160334 #pet #cat #tabbycat #nantes #france @frimoussethecat (o.o)"
arg2_img_dir = "file:c:/workdir/project-frimousse-social/"
arg3_img_fn ="20200112_160334_006-compressed-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:
    
    # page loaded
    wait("bluesky-post-btn.png", 30)
    
    # post
    click("bluesky-post-btn-1.png")
    
    # post loaded
    wait("bluesky-post-confirm-no.png", 10)
    
    # add text
    sleep(1)
    click("bluesky-post-txt.png")
    paste(arg1_text)
    
    # upload picture
    click("bluesky-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)
    
    # submit
    wait("bluesky-post-confirm-yes.png", 300)
    click("bluesky-post-confirm-yes-1.png")

    # success
    wait("bluesky-post-comfirmed.png", 300)

finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()