# Modified clipboard replaces <h> tags with <p>
import os
text = clipboard.get_selection().encode('ascii', 'ignore')
try:
    text = re.sub(r"<(.?)h[1-5]>", r"<\1p>", text, flags=re.IGNORECASE)
    os.system("xsel -bi <<<\""+text+"\"")
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    os.system("festival --tts <<<\""+val+"\"")