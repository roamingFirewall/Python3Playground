
print('testproject starting up!')


def rot_alpha(n, s):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return s.translate(lookup)


with open('input.txt', 'r') as f: 
    for line in f:
        print( rot_alpha(13, line.strip()) )






#todo: lookup hashing (string, file), other interesting (but simple) ciphers