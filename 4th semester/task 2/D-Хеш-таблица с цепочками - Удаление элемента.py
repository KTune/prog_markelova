
def pol_hash(s):

    p = 0

    for i in range(len(s)):

        p = p*91+ord(s[i])

    return p % 100

def remove(t, p):

    h = pol_hash(p)

    if t[h%10] == []:

        return 'KeyError'

    else:
        for i in range(len(t[h%10])):

            if t[h%10][i][1] == p:

                o = t[h%10][i][2]

                del t[h % 10][i]

                return o
        else:
            return 'KeyError'
