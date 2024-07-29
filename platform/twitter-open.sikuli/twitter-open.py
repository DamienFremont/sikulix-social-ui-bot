type("l", KeyModifier.CTRL)

# start twitter
paste("https://x.com/")
type(Key.ENTER)

wait("1683900184529.png")

# accept
if exists("1683902305109.png"):
    click("1683902305109.png")
