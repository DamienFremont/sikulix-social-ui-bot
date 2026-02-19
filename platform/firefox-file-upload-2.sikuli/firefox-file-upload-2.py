import sys.argv

ARG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220723_011713-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_FN = sys.argv[1]

# wait popup
wait("firefox-file-upload-popup.png")
sleep(1)

# focus filename
type("n", KeyModifier.ALT)
sleep(0.5)

# overide cached text
type("a", KeyModifier.CTRL)
sleep(0.5)

# type file name
paste(ARG_FN)
sleep(0.5)

# ok
type(Key.ENTER)
