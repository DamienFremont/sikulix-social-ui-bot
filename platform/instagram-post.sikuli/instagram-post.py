import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20210112_233929-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]
    
# post
click("insta-post-create-btn.png")
sleep(1)

# upload picutre
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
type(arg1_text)

# post
click("insta-post-submit.png")

# SUCCESS
         
# ERROR: already reposted, cancel

sleep(1)