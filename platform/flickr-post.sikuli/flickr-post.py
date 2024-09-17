import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20210112_233929-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

try:

    # post
    click("flickr-post-create.png")
    sleep(1)

    # upload picture
    click("flickr-file-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
    sleep(1)

    # type text
    click("flickr-post-desc.png")
    type(Key.TAB, KeyModifier.SHIFT)
    paste(arg1_text)

    # submit
    click("flickr-post-submit-1.png")
    click("flickr-post-submit2.png")

    # SUCCESS
    # TODO

    # ERROR: already reposted, cancel
    # TODO

    sleep(1)
    
    runScript("../platform/windows-takescreenshot", "-flickr-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-flickr-error")
finally:
    keyUp()
