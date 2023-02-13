alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o", "u"]
str = ""
end = "pfin"
position_p = 0
position_encripted = 0
difference = 0
def cesar1(str):
    v_f = 0
    code = list(str)
    stop = list(end)
    print(code)
    for i in range(len(alpha)):
        if stop[0] == alpha[i]:
            position_p = i
    print(position_p)
    for b in range(len(alpha)):
        if code[0] == alpha[b]:
            position_encripted = b
    print(position_encripted)
    difference = position_encripted - position_p
    print("the distance between is: ", difference)
    for c in range(len(code)):
        for n in range(len(alpha)):
            if code[c] == alpha[n]:
                code[c] = alpha[n-(difference)]
    for h in range(len(code)): 
        for m in range(len(vocals)):
            if code[h] == vocals[m]:
                v_f = v_f + 1
    code = ''.join(code)
    print(code,",",v_f,"vocals founded")
cesar1("ojkr")
#pfin
#sukp
#encontrar posicion de p