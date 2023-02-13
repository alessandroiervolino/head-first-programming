def replace_letters(text):
    lst = list(text)
    for i in range(len(lst)):
        lst = replace_a(i, lst)
        lst = replace_e(i, lst)             
    return ''.join(lst)
    
def replace_a(i, lst):
    if lst[i] == "a" or lst[i]=="á":
        lst[i] = "@"
    return lst

def replace_e(i,lst):
    if lst[i] == "e":
        lst[i] = "€"
    return lst


new_text = replace_letters("Lá meva contrasenya és molt segura" )
print(new_text)
new_text2 = replace_letters("ajkdhksjhwqwjwwweeesssaaaa")
print(new_text2)
