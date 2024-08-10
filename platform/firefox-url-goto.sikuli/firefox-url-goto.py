import sys.argv

ARG1_URL = "https://www.threads.net/"

# parameters
if len(sys.argv) > 1:
    ARG1_URL = sys.argv[1]

type("l", KeyModifier.CTRL)

paste(ARG1_URL)
type(Key.ENTER)

# sleep(1)
