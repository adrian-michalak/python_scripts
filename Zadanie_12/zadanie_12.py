import re
file_html = open("index.html", "r")
file_html_tags = open("index_noTags.html", "w")
content = file_html.read()
find_tags = re.compile("<[^>]*>", re.DOTALL | re.MULTILINE)
remove_tags = re.sub(find_tags, " ", content)
print(remove_tags)
file_html_tags.write(remove_tags)
file_html_tags.close()
