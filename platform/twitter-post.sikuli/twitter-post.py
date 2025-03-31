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

    # post
    click("twitter-post-text-area.png")
    sleep(1)

    # add text
    paste(arg1_text)

    # add pict
    click("twitter-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(3)

    # submit
    click("tw-post-submit-btn.png")

    # SUCCESS
    # TODO

finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()
