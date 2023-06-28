class NFA:

    def __init__(self, Q, Sigma, delta, S, F):
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition relation
        self.S = S # set of initial state
        self.F = F # set of final states

    def _repr_(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def do_delta(self,q,x):
        try :
            return self.delta[(q,x)]
        except KeyError:
            return set({})

    def run (self,w):
        P = self.S
        while w!="":
            Pnew = set ({})
            for q in P:
                Pnew = Pnew | self.do_delta(q,w[0])

            w = w[1:]
            P = Pnew
        return (P & self.F) != set({})