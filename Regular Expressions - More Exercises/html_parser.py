import re

text_input = input()
title_pattern = r'<title>(.+)<\/title>'
content_pattern = r'>([^<>]*)<?'
match_title = re.search(title_pattern, text_input)
match_content = re.findall(content_pattern, text_input)
content = ''

for part in match_content:
    if part != match_title.group(1):
        part = part.replace('\\n', '')
        content += part.strip() + ' '

print(f"Title: {match_title.group(1)}")
print(f'Content: {content.strip()}')
content = content.strip()