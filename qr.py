mod = 256
def toNumber(s):
    if s >= "0" and s <= "9": return ord(s) - ord('0')
    elif s >= "A" and s <= "Z": return ord(s) - ord("A") + 10
    elif s == ' ': return 36
    elif s == '$': return 37
    elif s == '%': return 38
    elif s == '*': return 39
    elif s == '+': return 40
    elif s == '-': return 41
    elif s == '.': return 42
    elif s == '/': return 43
    else: return 44
def Versionsize(version):
    if(version[0] == '1'): return 21
    else: return 25
def Swap(x, y):
    z = x
    x = y
    y = z
def Modeindicator():
    return "0010" #暂定Alphanumeric mode为“0010”=“2”这个代码
def CorrectCodeSize():#version1 纠错能力为M的为10 "1H"为8
    return 8
def toBinary(num, len):#44 * 45 + 44 = 2028 < 2048 = 2 ^ 11
    s = ""
    for i in range(len):
        s += str(num & 1)
        num >>= 1
    #print(s)
    s = s[::-1]
    print(s)
    return s
def BtoD(s):
    x = 0
    for i in range(len(s)):
       x = x << 1 | (ord(s[i]) - ord("0"))
    return x
def CharacterCount(s):
    x = 0
    if s == "1L": x = 152
    elif s == "1M": x = 128
    elif s == "1Q": x = 104
    elif s == "1H": x = 72
    elif s == "2L": x = 272
    elif s == "2M": x = 224
    elif s == "2Q": x = 176
    else: x = 128
    return x
def CCindicator(s):
    x = len(s)
    s = ""
    for i in range(9):
        s += str(x & 1)
        x >>= 1
    s = s[::-1]
    return s
def transform(str0, version):#version是版本缩写，如"1L"之类的
    list1 = []
    s = "" 
    for char in str0:
      list1.append(toNumber(char))
    #print(list1)
    for i in range(0, len(list1), 2):
        if(i + 1 < len(list1)):
            s = s + toBinary((list1[i] * 45 + list1[i + 1]), 11)
        else:
            s = s + toBinary(list1[i], 6)
    print(CCindicator(str0))
    s = Modeindicator() + CCindicator(str0) + s
    while(len(s) % 8 != 4): s = s + '0'
    s = s + "0000"
    print(s)
    list2 = []
    for i in range(0, len(s), 8):
      list2.append(BtoD(s[i : i + 8]))
    for i in range((CharacterCount(version) - len(s)) >> 3):
      if(i & 1):list2.append(BtoD("00010001"))
      else:list2.append(BtoD("11101100"))
    return list2
def ValueOfM(A, x):
    sum = 0
    for i in range(len(A)):
      sum = (sum * x % mod + x) % mod
    return sum
inv = []
index = []
GF = []
def Gauss(G, size):
    ans = []
    for i in range(size):
      for j in range(size):
        if(G[j][i] > G[i][i]): Swap(G[i], G[j])
      for j in range(size):
        if(j != i):
            for k in range(size + 1):
               #print(G[i][i])
               G[j][k] = addbybit(G[j][k], mulbybit(G[i][k], mulbybit(G[j][i], inv[G[i][i]]))) % mod
    for i in range(size):
      ans.append(mulbybit(G[i][size], inv[G[i][i]]))
    return ans
def addbybit(x, y):
    return x ^ y
def mulbybit(x, y):
    return GF[(index[x] + index[y]) % 255]
def pow(base, num):
    sum = 1
    while(num > 0):
        if(num & 1):  
            sum = mulbybit(sum, base) % mod
        num >>= 1
        base = mulbybit(base, base)
    return sum
A = transform("ABCDE123", "1H") #M(x)的系数
print(A, "ABCDE123")
#32 65 205 69 41 220 46 128 236
def CorrectCodeGenerator(s, version):
    m = CorrectCodeSize()
    size = 256
    primitive = 285
    GF.append(1)
    for i in range(255):
        if (GF[i] << 1) >= 256: GF.append((GF[i] << 1) ^ primitive) #伽罗华域的生成
        else: GF.append(GF[i] << 1)
    for i in range(256):
        inv.append(i)
        index.append(i)
    # for i in range(255):
    #     print(GF[i])
    # print(len(inv))
    # for i in range(255):
    #     print(inv[i])
    for i in range(256):
        #print(GF[i])
        inv[GF[i]] = GF[255 - i]
        index[GF[i]] = i
    Ex = []  #矩阵右边的系数
    for i in range(m):
        Exr = []
        #print(GF[i])
        for j in range(m):
            Exr.append(pow(GF[i], j)) #第0位就是x^0的系数以此类推
        Ex.append(Exr)
    print(Ex)
    for i in range(m):
        Ex[i].append(mulbybit(ValueOfM(A, GF[i]), pow(GF[i], m)))
    R = Gauss(Ex, m)
    #纠错码生成完毕
    return R
R = CorrectCodeGenerator("HELLO WORLD", "1M")
print(R)
# A.append(R) #链接两个串并且补足位数
# Vsize = Versionsize("1L")
# Ans = []
# for i in range(21):
#     G = []
#     for j in range(21):
#         G.append(1)
#     Ans.append(G) 