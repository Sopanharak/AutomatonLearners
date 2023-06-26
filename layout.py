a = "0,1,2"
b = "a,b"
c = "0,a,0; 0,b,1; 1,a,2; 1,b,1; 2,a,2; 2,b,2"
cPrime = "q0,a,0; q0,b,q1; q1,a,q2; q1,b,q1; q2,a,q2; q2,b,q2"
d = "0"
e = "0,1"



NewA = [int(i) for i in a.split(",")]
NewB = b.split(",")

NewC = {}
CSplit = c.split("; ")
for i in CSplit:
    j = i.split(",")
    d0 = int(j[0])
    d2 = int(j[2])
    NewC[d0, j[1]] = d2

NewCPrime = {}
CSplit = cPrime.split("; ")
for i in CSplit:
    j = i.split(",")
    d0 = int(j[0].replace("q", ""))
    d2 = int(j[2].replace("q", ""))
    #print(d1)
    NewC[d0, j[1]] = d2

NewD = int(d)
NewE = [int(i) for i in e.split(",")]


#print(NewA)
#print(NewB)
#print(NewC)
#print(NewD)
#print(NewE)


class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states
    
    def _repr_(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def run (self,w):
        q = self.q0
        while w!= "":
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.F
    

D0 = DFA(NewA, NewB, NewC, NewD, NewE)
D1 = DFA(
    [0,1,2], 
    ["a", "b"],
    {(0, "a"):0, (0, "b"):1, (1, "a"):2, (1, "b"):1, (2, "a"):2, (2, "b"):2},
    0,
    [0,1]
)


trueInput = "aaaaaba"
test = D0.run(trueInput)

if(test == True):
    print("The FA accept this String")
else:
    print("The FA does not accept this String")

