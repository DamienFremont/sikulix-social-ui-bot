ARG_URL = "https://www.pinterest.com/"

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
