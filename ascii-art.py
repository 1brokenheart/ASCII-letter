# ASCII letter art

letter_a = """
  A
 A A
A   A
AAAAA
A   A
A   A"""

letter_b = """
BBBBB
B   B
B   B
BBBB
B   B
B   B
BBBBB"""

letter_c ="""
 CCC
C   C
C    
C
C
C   C
 CCC"""

letter_d = """
 DDDD
 D   D
 D   D
 D   D
 D   D
 D   D
 DDDD"""

letter_e ="""
 EEEEE
 E
 E
 EEE
 E
 E
 EEEEE"""

letter_f="""
 FFFFF
 F
 F
 FFF
 F
 F
 F"""

letter_g= """
 GGG
G   G
G
GGGGG
G   G
G   G
 GGG"""

letter_h= """
H   H
H   H
H   H
HHHHH
H   H
H   H
H   H"""

letter_i = """
IIIII
  I  
  I
  I
  I
  I
IIIII"""

letter_j = """
JJJJJ
  J
  J
  J
J J
J J
 JJ"""

letter_k= """
K   K
K  K
K K
KK
K K
K  K
K   K"""

letter_l="""
l
l
l
l
l
l
lllll"""

letter_m = """
M    M
MM MM
MM MM
M M M
M   M
M   M
M   M"""

letter_n = """ 
N   N
NN  N
N N N
N  NN
N   N
N   N
N   N"""

letter_o="""
 OOO
O   O
O   O
O   O
O   O
O   O
 OOO"""

letter_p = """
PPPP
P   P
P   P
PPPP
P
P
P"""

letter_q= """
 QQQ
Q   Q
Q   Q
Q   Q
Q   Q
Q  Q
 QQ  Q"""

letter_r= """
RRRR
R   R
R   R
RRRR
R R
R  R
R   R"""

letter_s= """
 SSS
S   S
S
 SSS
    S
S   S
 SSS"""

letter_t="""
 TTTTT
   T
   T
   T
   T
   T
   T"""

letter_u= """
U   U
U   U
U   U
U   U
U   U
U   U
 UUU"""

letter_v= """
V   V
V   V
V   V
V   V
V   V
 V V
  V"""

       
letter_w= """
W   W
W   W
W   W
W W W
WW WW
WW WW
W   W"""

letter_x= """
X   X
X   X
 X X
  X
 X X
X   X
X   X"""

letter_y = """
Y   Y
 Y Y
  Y
  Y 
  Y 
  Y
  Y"""

letter_z="""
ZZZZZ
   Z
  Z
 Z
Z
ZZZZZ"""

#create a dictionary called letters that containes all the letters of the alphabet.
letters = {'a':letter_a, 'b':letter_b, 'c':letter_c, 'd':letter_d, 'e':letter_e, 'f':letter_f, 'g':letter_g, 'h':letter_h, 'i':letter_i, 'j':letter_j, 'k':letter_k, 'l':letter_l, 'm':letter_m, 'n':letter_n, 'o':letter_o, 'p':letter_p, 'q':letter_q, 'r':letter_r, 's':letter_s, 't':letter_t, 'u':letter_u, 'v':letter_v, 'w':letter_w, 'x':letter_x, 'y':letter_y, 'z':letter_z}

#print the name using the ascii and leaving 1 space in between each letter.
print(letters['a'], '\n', letters['n'], '\n', letters['g'],'\n', letters['e'], '\n', letters['l'], '\n', letters['a'])
