# NOTE: using 1080p resolution

# RESET SCREEN
type("0", Key.CTRL)
sleep(0.5)
type(Key.HOME)
sleep(0.5)

# SELECT NAME
location = Location(400, 475)
click(location)
click(location)
click(location)
sleep(0.5)

# COPY TEXT
type("c", Key.CTRL)
sleep(0.5)

# GET TEXT
message_text = Env.getClipboard()
print("LinkedIn getName() as: " +message_text)
