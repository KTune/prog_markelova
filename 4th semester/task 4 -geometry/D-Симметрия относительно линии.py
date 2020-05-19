
dots_of_line = list(map(int, input().split()))
dot = list(map(int, input().split()))
symmetry_dot = []
A = dots_of_line[3]-dots_of_line[1]
B = dots_of_line[0]-dots_of_line[2]
C=-A*dots_of_line[0]-B*dots_of_line[1]
if B != 0 and A != 0:
    x1 = ((B**2)*dot[0]-A*B*dot[1]-C*A)/(A**2+B**2)
    y1 = (-C-A*x1)/B
elif A == 0 and B != 0:
    x1 = dot[0]
    y1 = dots_of_line[1]
elif A != 0 and B == 0:
    x1 = dots_of_line[0]
    y1 = dot[1]
symmetry_dot.append(2*x1-dot[0])
symmetry_dot.append(2*y1-dot[1])
print(" ".join(map(str, symmetry_dot)))
