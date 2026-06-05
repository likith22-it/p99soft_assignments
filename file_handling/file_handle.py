import os

with open("data.txt","r") as f:
    print(f.read())
    print(f.read(5))
    print(f.readline())
    print(f.readline())


"""with open("data.txt","b") as m:
    print(m.read(3))"""


with open("data.txt","w") as k:
    k.write("jkbauva")

with open("data.txt") as j:
    j.read()