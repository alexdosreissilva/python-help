# coding=UTF-8

import hashlib

h = hashlib.md5()
h.update(b"uma frase qualquer")
print(h.hexdigest())

h = hashlib.sha256()
h.update(b"uma frase qualquer")
print(h.hexdigest())
