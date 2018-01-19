#Evaluate whole line as Python code
#abbreviation: =.
#Type in a formula like chr(65) =.
#Set =[dot][space] to trigger the keyboard macro: prints chr(65)= A 
from math import *
def rpt(c, n):
    return "".join([c for i in range(0, n)])
keyboard.send_keys("<shift>+<home>")
time.sleep(0.1)
text = clipboard.get_selection().encode('ascii', 'ignore')
keyboard.send_keys("<right>= ")
try:
    val = str(eval(text))
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
keyboard.send_keys(val)