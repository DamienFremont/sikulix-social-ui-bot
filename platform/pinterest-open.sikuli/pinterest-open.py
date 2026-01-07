ARG_URL = "https://www.pinterest.com/frimoussethecat/_created/"

# focus navbar
type("l", KeyModifier.CTRL)
sleep(0.5)

# copy URL
paste(ARG_URL)
type(Key.ENTER)
sleep(2)

# unfocus navbar
type(Key.ESC)
sleep(1)
