
gopher = list(map(int, input().split()))
dog = list(map(int, input().split()))
n = int(input())
v_gopher = 10
v_dog = 2*v_gopher
coordinates_of_minks = []
dist_mink_gopher = 0
dist_mink_dog = 0
flag = False
for i in range(n):
    coordinates_of_minks.append(list(map(int, input().split())))
for i in range(n):
    dist_mink_gopher = ((gopher[0]-coordinates_of_minks[i][0])**2+(gopher[1]-coordinates_of_minks[i][1])**2)**(1/2)
    dist_mink_dog = ((dog[0]-coordinates_of_minks[i][0])**2+(dog[1]-coordinates_of_minks[i][1])**2)**(1/2)
    if dist_mink_gopher/v_gopher<=dist_mink_dog/v_dog:
        print(i+1)
        flag = True
        break

if not flag:
    print('-1')
