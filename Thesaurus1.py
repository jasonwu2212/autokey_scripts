#thesaurus on selection Ctrl+Super+t
text = clipboard.get_selection()
try:
    text = text.encode('ascii', 'ignore')
    output = system.exec_command("gaiksaurus "+text)
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    keyboard.send_keys(val)