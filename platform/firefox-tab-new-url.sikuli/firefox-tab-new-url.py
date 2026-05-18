import sys.argv

ARG_URL = "https://www.google.com/"

# parameters
if len(sys.argv) > 1:
    ARG_URL = sys.argv[1]
    
# TAB ***********************************************
    
# start tab
type("t", KeyModifier.CTRL)

# URL  ***********************************************

# focus navbar
type("l", KeyModifier.CTRL)
sleep(0.5)

# copy URL
paste(ARG_URL)
type(Key.ENTER)

# unfocus navbar
#type(Key.ESC)
#sleep(1)
