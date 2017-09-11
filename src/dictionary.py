__author__ = 'jeroen.weber@hu.nl'

kv = {"0":"jeroen", "1":"weber", "naam":"waarde"}

print(kv.pop("1"))

print(kv["naam"])

for k,v in kv.items():
    print("key {0} with value {1}".format(k,v))

kv["kees"] = "jan"

print(kv["kees"])

if "0" in kv:
    print("yes")

print(kv.get("kees"))
#help(dict)

