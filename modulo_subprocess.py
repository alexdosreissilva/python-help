# coding=UTF-8

import subprocess

r = subprocess.call(["ls", "-la"])
print(r)

print("")

r = subprocess.check_output(["ls", "-la"])
print(r)

print("")

for linha in str(r).split("\n"):
    print(linha)
