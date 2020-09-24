#!/usr/bin/env python
# requires requests and rich
from re import findall
from requests import get
from rich.console import Console
from rich.table import Table

url = "https://media.kxan.com/nxs-kxantv-media-us-east-1/oembed/wx_embed/allergy/allergy_v3.5.js"  # noqa: E501

site = get(url, allow_redirects=False, timeout=(3.05, 27))

allergy_regex = r'<div class="allergen_value">(.*)</div><div class="plusecks">'
date_regex = r'<h3 class="allergy_content">(.*)</h3>'

allergies = findall(allergy_regex, site.text)
date = findall(date_regex, site.text)

table = Table(title="KXAN allergy report from {}".format(date[0]))
table.add_column("allergen")
table.add_column("severity")

for item in sorted(allergies):
    # change formatting from 'Oak - High' to ['Oak', 'High']
    i = item.split(" - ")
    table.add_row(i[0], i[1])

Console().print(table)
