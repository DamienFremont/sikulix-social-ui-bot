import sys.argv

arg1_text = "20210223_204831 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20210223_204831-x265_new.mp4"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]
    
wait("vimeo-post-create.png", 60)

# post
click("vimeo-post-create.png")
sleep(1)
click("vimeo-post-create2.png")
sleep(5)

# upload picture
click("vimeo-post-file-upload.png")
sleep(1)

# select picture
runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
sleep(2)

# wait optimizing
wait("vimeo-post-optimizing.png", 120)

# type desc
click("vimeo-post-form-desc.png")
paste(arg1_text)
sleep(1)

# type title
type(Key.TAB, KEY_SHIFT)
paste(arg1_text)

# no submit

# check upload



