limit = input()
arr = limit.split()
arr_int = list(map(int,arr))
while arr_int[0] != 0:
    arr_int.sort()
    is_par = ""
    if (len(arr_int)-1)%2 == 0:
        is_par = True
    else:
        is_par = False
    if is_par == False:
        print(arr_int[int(((len(arr_int)-1)/2)+0.5)])
    if is_par == True:
        print((arr_int[int(((len(arr_int)-1)/2)+0.5)]+arr_int[int(((len(arr_int)-1)/2)+0.5)+1])/2)

    #----------------    
    arr = input()
    arr = arr.split()
    arr_int = list(map(int,arr))
