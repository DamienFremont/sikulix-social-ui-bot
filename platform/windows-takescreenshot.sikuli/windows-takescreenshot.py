import sys.argv

arg1 = "-success"

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    
import shutil

screen = Screen()
file = screen.saveCapture(screen.getBounds())

# moves img to destination
file2 = file + arg1 + ".png"
shutil.move(file, file2)

print("Saved screen as " + file2)