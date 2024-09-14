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
paste(arg1_text)

# upload picutre
click("mastodon-post-upload.png")
sleep(1)

# select picture
runScript("firefox-file-upload", arg2_img_dir, arg3_img_fn)
sleep(2)

# uploaded
wait("mastodon-post-uploading.png", 10)
# wait_notexists(...)
timeout = 30
time_cnt = 0
while(True):
    time_cnt = time_cnt + 1
    if time_cnt > timeout:
        Debug.error('wait_notexists() timeout: ' + str(timeout))
        break
    if exists("mastodon-post-uploading.png"):
        wait(1)
    else:
        break

# submit
click("mastodon-post-submit-2.png")


# check upload
#wait("mastodon-post-check.png", 120)

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO



