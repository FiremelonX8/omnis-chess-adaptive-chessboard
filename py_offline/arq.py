s = "aereoaerialstresquatrocinco"

if s.find("aereo") >= 0:
    s = s.replace("aereo", "um")

print(type(s))
print(s.find("aereo"))
print(s)