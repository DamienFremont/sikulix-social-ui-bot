# NOTE: using 1080p resolution
import sys.argv
import shutil

runScript("../platform/linkedin-profile-getname")
name = Env.getClipboard()
print("LinkedIn getName() as: " +name)

filename = name + "-head.png"
runScript("../platform/linkedin-profile-screenshot-head", filename)

runScript("../platform/linkedin-profile-getname")
name = Env.getClipboard()
print("LinkedIn getName() as: " +name)

filename = name + "-exp.png"
runScript("../platform/linkedin-profile-screenshot-exp", filename)

print("Saved screen as " + file1)