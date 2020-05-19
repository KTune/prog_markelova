
fact_of_line_1 = list(map(int,input().split()))

fact_of_line_2 = list(map(int,input().split()))

cross = []

l = fact_of_line_2[0]/fact_of_line_1[0]

if l == fact_of_line_2[1]/fact_of_line_1[1]:

    print('NO')

else:

    p0 = (fact_of_line_1[1]*fact_of_line_2[2]-fact_of_line_1[2]*fact_of_line_2[1]) / \
         (fact_of_line_1[0]*fact_of_line_2[1] - fact_of_line_1[1]*fact_of_line_2[0])

    w0 = (fact_of_line_1[2]*fact_of_line_2[0]-fact_of_line_1[0]*fact_of_line_2[2]) / \
         (fact_of_line_1[0]*fact_of_line_2[1] - fact_of_line_1[1]*fact_of_line_2[0])

    cross.append(p0)

    cross.append(w0)

    print(int(round(cross[0])), int(round(cross[1])))
