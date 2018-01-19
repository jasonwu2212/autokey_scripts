#TitleCaps selected text Shift+Super+t
#Chicago Manual of Style
text = clipboard.get_selection().encode('ascii', 'ignore')
nocaps = ["a", "an", "the", "for", "and", "nor", "but", "or", "yet", "at", "around", "by", "after", "along", "for", "from", "of", "on", "to", "with", "without"]
out=""
words = text.split()
wordcount = 0
for word in words:
    wordcount += 1
    if word not in nocaps or wordcount == 1 or wordcount == len(words):
        out+=word.title()+" "
    else: out+=word+" "
try:
    keyboard.send_keys(out.strip())
except Exception as ex:
    val = type(ex).__name__+" "+ex.args[0]
    keyboard.send_keys(val)