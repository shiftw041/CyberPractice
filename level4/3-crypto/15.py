import numpy as np
from sympy import Matrix
import itertools
import re
import tqdm 
plain = 'vmc{  }'
ctext = '>u\x10l9\npI,0\x04^J\x00ib\x03\x0c\x158d\x1f\x08Ixk\nF\x19fz\x14PT\x04\x03>R~'
R=Zmod(127)
vcode = {}
for i in range(len(ctext)//3):
    vcode[i] = vector([R(ctext[3*i]),R(ctext[3*i+1]),R(ctext[3*i+2])])
print(vcode)

def sol1():#情况1 三个空格
    for i in range(32,127):
        for j in range(32,127):
            mp = Matrix(R,3,3,[ord('v'),ord('m'),ord('c'),
                                ord('{'),i,j,
                                0x20,0x20,0x20])
            mc = Matrix(R,3,3,[ctext[0],ctext[1],ctext[2],
                                ctext[3],ctext[4],ctext[5],
                                ctext[-3],ctext[-2],ctext[-1]])
            try:
                key = mp.solve_right(mc)
                cipher = ''
                key = key.inverse()
                for k in range(len(ctext)//3):
                    v = vcode[k]*key;
                    for l in range(3):
                        assert (v[l] == 0x20 or chr(v[l].isalnum() or chr(v[l]) in '{}_'))
                    cipher +=chr(v[0])+chr(v[1])+chr(v[2])
                print(cipher)
                return 1
            except:
                pass
        return 0
    
def sol2():#情况2，}加两个空格
    for i in range(32,127):
        for j in range(32,127):
            mp = Matrix(R,3,3,[ord('v'),ord('m'),ord('c'),
                                ord('{'),i,j,
                                ord('}'),0x20,0x20])
            mc = Matrix(R,3,3,[ctext[0],ctext[1],ctext[2],
                                ctext[3],ctext[4],ctext[5],
                                ctext[-3],ctext[-2],ctext[-1]])
            try:
                key = mp.solve_right(mc)
                cipher = ''
                key = key.inverse()
                for k in range(len(ctext)//3):
                    v = vcode[k]*key;
                    for l in range(3):
                        assert (v[l] == 0x20 or chr(v[l].isalnum() or chr(v[l]) in '{}_'))
                    cipher +=chr(v[0])+chr(v[1])+chr(v[2])
                print(cipher)
                return 1
            except:
                pass
        return 0
    
def sol3():
    for i in range(32,127):
        for j in range(32,127):
            for m in range(32,127):
                mp = Matrix(R,3,3,[ord('v'),ord('m'),ord('c'),
                                    ord('{'),i,j,
                                    m, ord('}'),0x20])
                mc = Matrix(R,3,3,[ctext[0],ctext[1],ctext[2],
                                    ctext[3],ctext[4],ctext[5],
                                    ctext[-3],ctext[-2],ctext[-1]])
                try:
                    key = mp.solve_right(mc)
                    cipher = ''
                    key = key.inverse()
                    for k in range(len(ctext)//3):
                        v = vcode[k]*key;
                        for l in range(3):
                            assert (v[l] == 0x20 or chr(v[l].isalnum() or chr(v[l]) in '{}_'))
                        cipher +=chr(v[0])+chr(v[1])+chr(v[2])
                    print(cipher)
                except:
                    pass
    return 0

if not sol1():
    if not sol2():
        sol3()

'''
print('vmc{d8euED8uaj47suIie34uI9weo01pdKiD}')
print('vmc{dleuhD8wajs7sfIio345I9BeoI1pTKii}')