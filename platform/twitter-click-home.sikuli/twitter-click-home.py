if exists("twitter-home-on.png"):
    do_nothing = 1
    
elif exists("twitter-home-off.png"):
    click("twitter-home-off.png")

wait("twitter-home-on.png")