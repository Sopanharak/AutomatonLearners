class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states
    
    # def _repr_(self):
    #     return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def run (self,w):
        # when we put self, it means that we are passing the object itself into its own function. so that the function "can" access the object properties
        # w is the user input string, but it will as the code execute

        #q: we create a "state" variable called q. it represent the state of computation, and it "starts" as an initail state (q0)
        q = self.q0    
         
        while w!= "":
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.F