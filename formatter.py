
import json

def format_mons():
    input_file = "pokemon pack.txt"
    res = {}

    with open(input_file, "r") as f:
        lines = f.read()

    tiers = lines.split("split")
    tiers.pop(0)
    r = ["UR", "SR", "R", "C"]
    c = 0
    for tier in tiers:
        res[r[c]] = []
        mons = tier.split("\n\n")
        for mon in mons:
            res[r[c]].append(mon)
        c+=1



    with open("result.json", "w") as f:
        json.dump(res, f, indent=2)

def format_singular(filename):
    res = {}

    with open(filename, "r") as f:
        lines = f.read()

    tiers = lines.split("split")
    tiers.pop(0)
    r = ["UR", "SR", "R", "C"]
    c = 0
    for tier in tiers:
        res[r[c]] = []
        mons = tier.split("\n")
        for mon in mons:
            res[r[c]].append(mon)
        c+=1



    with open("result.json", "w") as f:
        json.dump(res, f, indent=2)

if __name__ == "__main__":
    format_singular("items pack.txt")