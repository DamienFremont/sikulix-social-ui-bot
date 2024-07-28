import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)

# add text
type(arg1_text)

# add pict
if arg2_clip.lower() == "true":
    type("v", KeyModifier.CTRL)
    sleep(5)

# submit
click("mastodon-post-submit.png")

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)
