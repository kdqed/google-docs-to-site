import config
import os
import requests
from bs4 import BeautifulSoup

os.makedirs("build/", exist_ok=True)

soup = BeautifulSoup(requests.get(config.PUB_URL).text, features="lxml")
title = soup.select_one("title").text
content = soup.select_one("div.doc-content").decode_contents()
template = open("template.html").read()
render = template.replace("{{title}}", title).replace("{{content}}", content)
f = open("build/index.html", "w")
f.write(render)
f.close()

os.makedirs("build/edit/", exist_ok=True)
editor_template = open("edit.html").read()
render = editor_template.replace("{{BUILD_HOOK}}", config.BUILD_HOOK).replace("{{EDIT_URL}}", config.EDIT_URL)
f = open("build/edit/index.html", "w")
f.write(render)
f.close()
