
coord_of_triangle = list(map(int, input().split()))

sym_dot = list(map(int, input().split()))

new_coord_of_sym_triangle = []

for i in range(3):

    new_coord_of_sym_triangle.append(2*sym_dot[0]-coord_of_triangle[2*i])

    new_coord_of_sym_triangle.append(2*sym_dot[1]-coord_of_triangle[2*i+1])

print(" ".join(map(str, new_coord_of_sym_triangle)))
