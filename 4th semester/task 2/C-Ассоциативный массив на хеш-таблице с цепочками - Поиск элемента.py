
def pol_hash(s):
    p = 0

    for j in range(len(s)):

        p = p*91+ord(s[j])

    return p % 100

def search(t, p):

    h = pol_hash(p)

    if t[h%10] == []:

        return 'KeyError'

    else:

        for j in range(len(t[h%10])):

            if t[h%10][j][1] == p:

                return t[h%10][j][2]
        else:
            return 'KeyError'
