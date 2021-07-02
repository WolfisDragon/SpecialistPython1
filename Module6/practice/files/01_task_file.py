f = open("limericks.txt", "r", encoding="utf=8")

res = 0
for line in f:
    step1 = line.split()
    i = 0
    while i < len(step1):
        res_l = len(step1[i])
        i += 1
        res += res_l
print(res)
