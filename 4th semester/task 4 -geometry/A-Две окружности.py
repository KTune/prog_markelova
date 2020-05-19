
circle_1=list(map(int, input().split()))

circle_2=list(map(int, input().split()))

p1=circle_1[0]

z1=circle_1[1]

w1=circle_1[2]

p2=circle_2[0]

z2=circle_2[1]

w2=circle_2[2]

distance_between_centres=((p1-p2)**2+(z1-z2)**2)**(1/2)

if distance_between_centres <= (w1+w2) and distance_between_centres >= (abs(w1-w2)):
    print("YES")
else:
    print("NO")
