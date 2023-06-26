import dfa
import nfa

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


    # still doing it
    # num = input("Enter 1 to test / O to quit")
    # while(num != 0):
    #     FA = nfa.NFA(newA, newB, newC, newD, newE)
    #     FA.run()
    #     if(FA == True):
    #         print("FA accept this string.")
    #     else:
    #         print("FA does not accept this string.")
    #     num = input("Enter 1 to test / O to quit")
    
else:
    newA = [int(i) for i in a.split(",")]
    newB = b.split(",")

    newC = {}
    CSplit = c.split("; ")
    for i in CSplit:
        j = i.split(",")
        d0 = int(j[0])
        d2 = int(j[2])
        newC[d0, j[1]] = d2

    newD = int(d)
    newE = [int(i) for i in e.split(",")]
    print("Test is DFA")
    print(newA)
    print(newB)
    print(newC)
    print(newD)
    print(newE)

    num = input("Enter 1 or 0: ")
    while(num != 0):
        FA = dfa.DFA(newA, newB, newC, newD, newE)
        userString = input("Enter String: ")
        aceptString = FA.run(userString)
        if(aceptString == True):
            print("FA accept this string.")
        else:
            print("FA does not accept this string.")
        num = input("Enter 1 to test / O to quit")
    # 0,a,0; 0,b,1; 1,a,2; 1,b,2; 2,a,2; 2,b,2;