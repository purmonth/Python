# import the library pulp as p 
import pulp as p 
import numpy as np

# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
# Create problem Variables  

X00 = p.LpVariable("X00", lowBound = 0)
X01 = p.LpVariable("X01", lowBound = 0)
X02 = p.LpVariable("X02", lowBound = 0)
X03 = p.LpVariable("X03", lowBound = 0)
X04 = p.LpVariable("X04", lowBound = 0)
X05 = p.LpVariable("X05", lowBound = 0)
X06 = p.LpVariable("X06", lowBound = 0)
X10 = p.LpVariable("X10", lowBound = 0)
X11 = p.LpVariable("X11", lowBound = 0)
X12 = p.LpVariable("X12", lowBound = 0)
X13 = p.LpVariable("X13", lowBound = 0)
X14 = p.LpVariable("X14", lowBound = 0)
X15 = p.LpVariable("X15", lowBound = 0)
X16 = p.LpVariable("X16", lowBound = 0)
X20 = p.LpVariable("X20", lowBound = 0)
X21 = p.LpVariable("X21", lowBound = 0)
X22 = p.LpVariable("X22", lowBound = 0)
X23 = p.LpVariable("X23", lowBound = 0)
X24 = p.LpVariable("X24", lowBound = 0)
X25 = p.LpVariable("X25", lowBound = 0)
X26 = p.LpVariable("X26", lowBound = 0)
X30 = p.LpVariable("X30", lowBound = 0)
X31 = p.LpVariable("X31", lowBound = 0)
X32 = p.LpVariable("X32", lowBound = 0)
X33 = p.LpVariable("X33", lowBound = 0)
X34 = p.LpVariable("X34", lowBound = 0)
X35 = p.LpVariable("X35", lowBound = 0)
X36 = p.LpVariable("X36", lowBound = 0)

#create a variable xij >=0


##x = p.LpVariable("Y1", lowBound = 0)   # Create a variable x >= 0 
##y = p.LpVariable("Y2", lowBound = 0)   # Create a variable y >= 0 


# Objective Function 
Lp_prob += 750*(X00+X01+X02+X03+X04+X05+X06) + 600*(X10+X11+X12+X13+X14+X15+X16) + 800*(X20+X21+X22+X23+X24+X25+X26) + 450*(X30+X31+X32+X33+X34+X35+X36)
  
# Constraints: 
Lp_prob += X00+X10+X20+X30 <= 8
Lp_prob += X01+X11+X21+X31 <= 4
Lp_prob += X02+X12+X22+X32 <= 4
Lp_prob += X03+X13+X23+X33 <= 4
Lp_prob += X04+X14+X24+X34 <= 8
Lp_prob += X05+X15+X25+X35 <= 2
Lp_prob += X06+X16+X26+X36 <= 2
Lp_prob += X00+X01+X02+X03+X04+X05+X06 <= 5
Lp_prob += X10+X11+X12+X13+X14+X15+X16 <= 6
Lp_prob += X20+X21+X22+X23+X24+X25+X26 <= 4
Lp_prob += X30+X31+X32+X33+X34+X35+X36 <= 8
#Lp_prob += -x + y <= 3
#Lp_prob += x >= 4
#Lp_prob += y <= 3
  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution
Price =  p.value(Lp_prob.objective)
print(p.value(X00),p.value(X01),p.value(X02),p.value(X03),p.value(X04),p.value(X05),p.value(X06))
print(p.value(X10),p.value(X11),p.value(X12),p.value(X13),p.value(X14),p.value(X15),p.value(X16))
print(p.value(X20),p.value(X21),p.value(X22),p.value(X23),p.value(X24),p.value(X25),p.value(X26))
print(p.value(X30),p.value(X31),p.value(X32),p.value(X33),p.value(X34),p.value(X35),p.value(X36))
print(Price)