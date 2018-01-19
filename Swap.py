# Swap on first non-word character
text = clipboard.get_selection().encode('ascii', 'ignore')
keyboard.send_key("<delete>")
try:
    r = re.search(r'([^ ,:;]+)([ ,:;]+)([^ ,:;]+)', text).groups()
    keyboard.send_keys(r[2]+r[1]+r[0])
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    keyboard.send_keys(val)