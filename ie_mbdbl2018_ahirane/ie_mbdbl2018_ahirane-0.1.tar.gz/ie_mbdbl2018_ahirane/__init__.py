def  datareader_doc():
    """ function to return the string 'My first Python package that anyone call install it! How cool!!!' """
    return("This is Andres Hirane first package that anyone can install it! How cool!!!")


a = 22695477
b = 1
m = 2**32
x0=1649836483

def linear_congruence_random_generator(): 
  """ function to return a random number using the Method of linear congruences.""" 
  global a
  global b
  global m
  global x0
  return (a*xi+b)%(m)


class c_linear_congruences:
    def __init__(self, x0,a,b,m):
        self.xi = x0
        self.a = a
        self.b = b
        self.m = m

    def linear_congruence_random_generator(self):
        self.xi=(self.a*self.xi+self.b)%(self.m)
        return self.xi