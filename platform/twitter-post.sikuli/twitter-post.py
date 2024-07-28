import sys.argv

arg1_text = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
arg2_clip = "true"

# parameters
if len(sys.argv) > 1:
    arg1_text = sys.argv[1]
    arg2_clip = sys.argv[2]

# post
if exists("tw-post-button.png"):
    click("tw-post-button.png")
    sleep(1)

    # add text
    ## type text
    type(arg1_text)

    # add pict
    if arg2_clip.lower() == "true":
        type("v", KeyModifier.CTRL)
        sleep(1)


    # submit
    click("tw-post-submit-btn.png")
    
    # SUCCESS
    # TODO
    
    # ERROR: already reposted, cancel
    # TODO

    sleep(1)