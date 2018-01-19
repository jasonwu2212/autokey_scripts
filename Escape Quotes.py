def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

text = clipboard.get_selection().encode('ascii', 'ignore')
keyboard.send_key("<delete>")
try:
    text = addslashes(text)
    keyboard.send_keys(text)
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    keyboard.send_keys(val)