import sys.argv

arg1_title = "20210117_205357 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20210117_205357-x265_new.mp4"

# parameters
if len(sys.argv) > 1:
    arg1_title = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

# post
click("tw-post-button.png")
sleep(1)

# add text
## type text
type(arg1_title)

# add vid
click("tw-post-vid.png")
sleep(1)

runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
sleep(2)
#wait("tw-post-vid-ok.png", 120)

# submit
# TODO click("tw-post-submit-btn.png")

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)