import sys.argv

arg1_text = "20211220_005455 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg3_img_fn ="20211220_005455-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_img_dir = sys.argv[2]
    arg3_img_fn = sys.argv[3]

# post
click("mastodon-post-create.png")

# add text
type(arg1_text)

# upload picutre
click("mastodon-post-upload.png")
sleep(1)

# select picture
runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
sleep(1)

# FIXME: not diff between loading and loaded post buttons
wait("mastodon-post-uploading.png", 10)
while(True):
    if exists("mastodon-post-uploading.png"):
        wait(1)
    else:
        break

# submit
click("mastodon-post-submit-2.png")
sleep(1)

# check upload
#wait("mastodon-post-check.png", 120)

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO



