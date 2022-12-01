----This text file gives information about the Encryptor.----

Name: Encryptor
Description: Encrypts the text inside the given path
Made by: Yusif

----How to use?----

Values and uses:

-t, --text: Path for the text file which will be encrypted. Will give error if value in text can't be found in the base of encryption. Please look at the section "Bases of encryption".

-p, --path: Path where encrypted file will be stored. This text file or the path should be empty.

-n, --number: Rotation number for encryption. Can be any range. Can be activated with a key.

-k, --key: Key for encryption. Should be given correctly for the base of encryption(uppercase letters or only letters).

Will give error if value in key can't be found in the base of encryption. Please look at the section "Bases of encryption".Can be activated with a rotation number.

-rk, --randomised_key : Option for the situation when key is not long enough for the text. Remaining will be done by random values.

Will give error if value in key can't be found in the base of encryption. Please look at the section "Bases of encryption".Can be activated with a rotation number.

-uc, --upper_case: Option for the base of encryption. Can't be used with letters_only. To know about this base please look at the section "Bases of encryption".

-lo, --letters_only: option for the base of encryiption. to know about this base please look at the section "Bases of encryption".
 
----Bases of encryption----

Bases are shown with the format -> value index

Default:

new_line 0
tab 1
empty_space  2
! 3
" 4
# 5
$ 6
% 7
& 8
' 9
( 10
) 11
* 12
+ 13
, 14
- 15
. 16
/ 17
0 18
1 19
2 20
3 21
4 22
5 23
6 24
7 25
8 26
9 27
: 28
; 29
< 30
= 31
> 32
? 33
@ 34
A 35
B 36
C 37
D 38
E 39
F 40
G 41
H 42
I 43
J 44
K 45
L 46
M 47
N 48
O 49
P 50
Q 51
R 52
S 53
T 54
U 55
V 56
W 57
X 58
Y 59
Z 60
[ 61
\ 62
] 63
^ 64
_ 65
` 66
a 67
b 68
c 69
d 70
e 71
f 72
g 73
h 74
i 75
j 76
k 77
l 78
m 79
n 80
o 81
p 82
q 83
r 84
s 85
t 86
u 87
v 88
w 89
x 90
y 91
z 92
{ 93
| 94
} 95
~ 96

Uppercase only base:

A 0
B 1
C 2
D 3
E 4
F 5
G 6
H 7
I 8
J 9
K 10
L 11
M 12
N 13
O 14
P 15
Q 16
R 17
S 18
T 19
U 20
V 21
W 22
X 23
Y 24
Z 25

Letters only:

A 0
B 1
C 2
D 3
E 4
F 5
G 6
H 7
I 8
J 9
K 10
L 11
M 12
N 13
O 14
P 15
Q 16
R 17
S 18
T 19
U 20
V 21
W 22
X 23
Y 24
Z 25
a 26
b 27
c 28
d 29
e 30
f 31
g 32
h 33
i 34
j 35
k 36
l 37
m 38
n 39
o 40
p 41
q 42
r 43
s 44
t 45
u 46
v 47
w 48
x 49
y 50
z 51
