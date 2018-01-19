cite = clipboard.get_selection().encode('ascii', 'ignore')
keyboard.send_key("<delete>")
try:
    cite = "(" + cite.replace(" (", ", ")
    cite = re.sub("[., ]*$", ".", cite)
    keyboard.send_keys(cite)
except Exception as ex:
    val = type(ex).__name__ + " " + ex.args[0]
    keyboard.send_keys(val)