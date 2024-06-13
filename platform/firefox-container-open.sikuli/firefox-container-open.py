import sys.argv

arg1 = "1"

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

# start container
type(arg1, KeyModifier.CTRL + KeyModifier.SHIFT)