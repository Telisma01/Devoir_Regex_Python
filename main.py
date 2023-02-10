import re
text = "Je vais sur #facebook et sur #whatsapp mais pas sur tiktok"
pattern = "#\w+"
result = re.sub(pattern, lambda x: "<a href=''>{}</a>".format(x.group()), text)
print(result)
