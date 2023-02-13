nums = [[2,1,10],[2,13,5],[2,7,4],[3,9,9,6],[0]]
biggest = 0
for i in range(len(nums)):
    limit = nums[i][0]
    for c in range(1):
        if nums[i][0]==0:
            print(nums[i][0], "->", biggest)
        else:   
            for b in range(1, limit+1):
                if nums[i][b] > biggest: 
                    biggest = nums[i][b]
            print(nums[i][1:limit+1], "->", biggest)
            biggest = 0
               
