import sys.argv

arg1_text = "TEST #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post
click("tumblr-post-create.png")
sleep(2)

# add text
type(arg1_text)

# add pict
if arg2_clip.lower() == "true":
    type("v", KeyModifier.CTRL)
    sleep(10)

# submit
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.ENTER)
#click("tumblr-post-submit-2.png")

#confirm
sleep(2)
if exists("tumblr-post-confirm-tags1.png"):
    click("tumblr-post-confirm-tags2.png")

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)
