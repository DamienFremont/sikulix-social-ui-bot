import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post
click("threads-post-create-1.png")
sleep(1)

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
type(Key.TAB)
type(Key.TAB)
type(Key.ENTER)

# SUCCESS
# TODO

# ERROR: already reposted, cancel
# TODO

sleep(1)
