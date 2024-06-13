# type(Key.F4, KEY_ALT)

try:
   # some code that may fail   
   keyDown(Key.ALT)
   keyDown(Key.F4)
finally:
   # this is done in all cases
   keyUp()