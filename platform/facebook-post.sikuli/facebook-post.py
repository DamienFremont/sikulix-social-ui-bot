import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post

click("fb-post-create.png")
sleep(2)

# add text
type(arg1_text)

# add pict
if arg2_clip.lower() == "true":
    type("v", KeyModifier.CTRL)
    sleep(1)

# submit
type(Key.TAB, KEY_SHIFT)
type(Key.TAB, KEY_SHIFT)
type(Key.TAB, KEY_SHIFT)
type(Key.TAB, KEY_SHIFT)
type(Key.ENTER)

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)
