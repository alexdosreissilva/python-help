# coding=UTF-8

s = "hello, world!"

print(s.upper())
print(s.split(","))
print(s.split(",")[0])
print(s.replace("world", "dude"))

print(s[0])
print(s[2])
print(s[12])

print(s[len(s) - 1])
print(s[-1])

print(s[0:5])
print(s[:5])
print(s[2:4])
print(s[7:13])
print(s[7:])
print(s[:])

url = "http://localhost:8000/arquivo.iso"
protocolo = url[0:url.index(':')]
print(protocolo)
