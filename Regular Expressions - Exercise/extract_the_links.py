import re
links = input()
link_pattern = re.compile(r"(?P<sub_domain>w{3}\.)(?P<domain>[A-Za-z0-9\-]+\.)(?P<extension>[a-z]+[\-.]*[a-z0-9\-.]*)")
while len(links):
    valid_link = link_pattern.finditer(links)
    for valid in valid_link:
        print(f"{valid['sub_domain']}{valid['domain']}{valid['extension']}")
    links = input()