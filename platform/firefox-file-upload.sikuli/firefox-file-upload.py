import sys.argv

arg1_img_dir = "file://///192.168.8.2/workdir/project-frimousse-social/"
arg2_img_fn ="20210112_233929-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_img_dir = sys.argv[1]
    arg2_img_fn = sys.argv[2]

# wait popup
wait("firefox-file-upload-popup.png")

# find folder
type("l", KeyModifier.CTRL)
paste(arg1_img_dir)
type(Key.ENTER)

sleep(1)

# search file
type(Key.TAB)
paste(arg2_img_fn)
type(Key.ENTER)

sleep(1)

# select file
type(Key.TAB)
type(Key.TAB)
type(Key.TAB)
type(Key.RIGHT)
type(Key.ENTER)
