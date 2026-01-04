import sys.argv

ARG_CONT = "1"
ARG_URL = "https://www.google.com/"

# parameters
if len(sys.argv) > 1:
    ARG_CONT = sys.argv[1]
    ARG_URL = sys.argv[2]
    
# CONTAINER ***********************************************
    
# start container
type(ARG_CONT, KeyModifier.CTRL + KeyModifier.SHIFT)

# URL  ***********************************************

# focus navbar
type("l", KeyModifier.CTRL)
sleep(0.5)

paste(ARG_URL)
type(Key.ENTER)
sleep(0.5)

# unfocus navbar
#type(Key.ESC)
#sleep(1)
