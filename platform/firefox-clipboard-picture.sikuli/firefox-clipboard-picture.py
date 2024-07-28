import sys.argv

arg1_img_url = "file://///192.168.8.2/workdir/project-frimousse-social/20210112_233929-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    arg1_img_url = sys.argv[1]

## copy picture to clipboard

## new tab
type("t", KeyModifier.CTRL)

## open picture
type("l", KeyModifier.CTRL)
paste(arg1_img_url)
type(Key.ENTER)

## move mouse to center of screen
screen_center_x = SCREEN.getCenter().getX()
screen_center_y = SCREEN.getCenter().getY()
mouseMove(Location(screen_center_x, screen_center_y))

## copy
rightClick(Location(screen_center_x, screen_center_y))
type("y")

## close tab
type("w", KeyModifier.CTRL)
