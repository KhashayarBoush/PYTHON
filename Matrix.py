

m1 = [[1,2]]

m2 = [[1,1],
      [2,4]]

m3 = [[[],[]]]

print(m3[0][0])

m3[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2 [1][0]

print(m3[0][0])

m3[0][1] = m1[0][0] * m2[0][1] + m1 [0][1] * m2 [1][1]

print(m3)

# ======================================================================
m4 = [[1,6,7]]

m5 = [[1,5,8],
      [2,5,8],
      [6,5,8]]


m6 = [[[],[],[]]]

print(m6[0][2])

m6 [0][0] = m4[0][0] * m5[0][0] + m4 [0][1] * m5 [1][0] + m4 [0][2] * m5 [2][0]

print(m6[0][0])