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
    click("cara-post-create.png")
    sleep(1)

    # type text
    type(Key.TAB)
    paste(arg1_text)

    # upload picture
    click("cara-post-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)

    # submit
    click("cara-post-submit.png")

    # SUCCESS
    # TODO

    # ERROR: already reposted, cancel
    # TODO

    sleep(1)
    
finally:
    runScript("../platform/windows-takescreenshot", "-cara")
    keyUp()
