import sys.argv

arg1_text = "20210112_205357 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20210117_205357-x265_new.mp4"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]
    
# post
click("youtube-studio-post-create.png")
sleep(1)
click("youtube-studio-post-create2.png")
sleep(1)

# upload picutre
click("youtube-post-upload.png")
sleep(1)

# select picture
runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
sleep(2)

# type text
wait("youtube-post-next.png")
type("a", KeyModifier.CTRL)
sleep(1)
type(arg1_text)

# next...
click("youtube-post-next.png")
sleep(1)
click("youtube-post-next.png")
sleep(1)
click("youtube-post-next.png")
sleep(1)

# submit
click("youtube-post-select-public.png")
#sleep(1)

# submit
#click("youtube-post-submit.png")

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)