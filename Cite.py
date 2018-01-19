#Turn highlighted reference into citation. Alt+Ctrl+c
text = clipboard.get_selection().encode('ascii', 'ignore')
keyboard.send_key("<delete>")
cite = re.sub("[A-Z]\.,*", "", text)
cite = cite.replace("&", "and")
cite = re.sub(",\s+", ", ", cite)
cite = re.sub("[\., ]*\(", " (", cite)
if len(re.findall(",", cite)) == 1:
    cite = re.sub(",\s+", " ", cite)
cite = re.sub("[\., ]+$", "", cite)
try:
    keyboard.send_keys(cite + ", ")
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    keyboard.send_keys(val)