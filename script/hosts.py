import requests
import shutil

url = "https://raw.hellogithub.com/hosts"
response = requests.get(url)

with open("D:\\hosts", "wb") as f:
    f.write(response.content)

print("文件下载成功！")

shutil.copy2("D:\\hosts", "C:\\Windows\\System32\\drivers\\etc\\hosts")

print("操作成功!")
