def convert(v):
    return tuple(int(v[i:i+2], 16) for i in (0, 2, 4))

hex = '3A224F,4E2557,73326A,A34474,C7506B,E3755F,ED9E70,FCC88D,FFD7A3,FFEFC9,F0EBA8,CFF291,A0DE85,69C976,50AB76,36777A,2E5C6B,223D54,1F2E52'.split(',')
res = []
for i in hex:
    res.append(convert(i))

print(res)