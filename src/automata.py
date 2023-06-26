a = input("a: ")
b = input("b: ")
c = input("c: ")
d = input("d: ")
e = input("e: ")


isNFA = False
for i in c.split("; "):
    j = i.split(",")
    if len(j) > 3:
        isNFA = True
    
if isNFA:
    newA= [int(i) for i in a.split(",")]
    newB= b.split(",")

    newC = {}
    CSplit = c.split("; ")
    for i in CSplit:
        j = i.split(",")
        d0 = int(j[0])
        d2 = set({})
        for k in range(2, len(j)):
            d2.add(int(j[k]))
        newC[d0, j[1]] = d2

    newD = set({int(d)})
    newE = set({})
    for i in e.split(","):
        newE.add(int(i))
    print("Test is NFA")
    print(newA)
    print(newB)
    print(newC)
    print(newD)
    print(newE)
    
else:
    newA = [int(i) for i in a.split(",")]
    newB = b.split(",")

    NewC = {}
    CSplit = c.split("; ")
    for i in CSplit:
        j = i.split(",")
        d0 = int(j[0])
        d2 = int(j[2])
        NewC[d0, j[1]] = d2

    newD = int(d)
    newE = [int(i) for i in e.split(",")]
    print("Test is DFA")