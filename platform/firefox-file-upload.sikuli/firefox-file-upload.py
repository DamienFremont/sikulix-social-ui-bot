import sys.argv

arg1_img_dir = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/"
arg2_img_fn ="20220723_011713-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_img_dir = sys.argv[1]
    arg2_img_fn = sys.argv[2]

# wait popup
wait("firefox-file-upload-popup.png")
sleep(1)

# focus path
#type("l", KeyModifier.CTRL)
#sleep(1)

# focus filename
#type(Key.TAB, KEY_SHIFT)
#type(Key.TAB, KEY_SHIFT)
#type(Key.TAB, KEY_SHIFT)
#type(Key.TAB, KEY_SHIFT)
#type(Key.TAB, KEY_SHIFT)
type("n", KeyModifier.ALT)
sleep(0.5)

paste(arg1_img_dir + arg2_img_fn)
sleep(0.5)

# ok
type(Key.ENTER)

# ARCHIVE: folder then file

# find folder
#type("l", KeyModifier.CTRL)
#paste(arg1_img_dir)
#type(Key.ENTER)

#sleep(1)

# search file
#type(Key.TAB)
#paste(arg2_img_fn)
#type(Key.ENTER)

#sleep(1)

# select file
#type(Key.TAB)
#type(Key.TAB)
#type(Key.TAB)
#type(Key.RIGHT)
#type(Key.ENTER)
