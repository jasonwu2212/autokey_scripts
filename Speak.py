# Enter script code
import os
text = clipboard.get_selection().encode('ascii', 'ignore')
try:
    text = text.replace("\"", "\\\"")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    os.system("espeak \""+text+"\"")
except Exception as ex:
    text = type(ex).__name__+" "+ex.args[0]
    os.system("espeak \""+text+"\"")