import sys.argv

arg1_text = "20210123_000517 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post
click("mastodon-post-create.png")

# add text
type(arg1_text)

# add pict
if arg2_clip.lower() == "true":
    type("v", KeyModifier.CTRL)
    sleep(3)
    wait("mastodon-post-submit-2.png", 120)

# submit
click("mastodon-post-submit-2.png")
sleep(1)

# check upload
wait("mastodon-post-check.png", 120)

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO



