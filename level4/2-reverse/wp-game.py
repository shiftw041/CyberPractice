v2 = [0] * 32
v2[0] = 158
v2[1] = 149
v2[2] = 99
v2[3] = 155
v2[4] = 113
v2[5] = 157
v2[6] = 81
v2[7] = 156
v2[8] = 109
v2[9] = 103
v2[10] = 97
v2[11] = 103
v2[12] = 110
v2[13] = 157
v2[14] = 150
v2[15] = 150
v2[16] = 153
v2[17] = 103
v2[18] = 111
v2[19] = 92
v2[20] = 149
v2[21] = 109
v2[22] = 103
v2[23] = 105
v2[24] = 147
v2[25] = 150
v2[26] = 124
v2[27] = 103
v2[28] = 105
v2[29] = 156
v2[30] = 133
v1 = [0] * 32
for i in range(0, 31):
    v1[i] ^= v2[i]
    v1[i] ^= 0x14
    v1[i] -= 20
for i in v1:
    print(chr(i), end="")