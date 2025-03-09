with open(f"./sprites/regular/ho-oh", "r", encoding="utf-8") as f:
    spritel = f.readlines()

with open(f"./sprites/regular/pikachu", "r", encoding="utf-8") as f:
    sprite = f.read()

print(spritel)
print(sprite)

print()
def split_d(d, all_lines):
    d = "\n"
    res = []
    for line in all_lines:
        res.append([e+d for e in line.split(d) if e])


for i in range(len(spritel)):
    spritel[i] = spritel[i].split("\x1b")



for el in spritel:
    el.reverse()

result = []
for line in spritel:
    for i in range(len(line)):
        if line[i].startswith("["):
            line[i] = "\x1b" + line[i]
    result.append("".join(line))
print()
print(result)
for line in result:
    print(line.replace("\n", ""))
print("test test")
print("   [0m[38;2;0;0;0m▄[38;2;0;0;0m[0m[48;2;94;97;94m▀[0m[38;2;0;0;0m▄              [38;2;0;0;0m▄[38;2;0;0;0m▄[38;2;0;0;0m[48;2;94;97;94m▀[38;2;0;0;0m[48;2;0;0;0m▀                    ")