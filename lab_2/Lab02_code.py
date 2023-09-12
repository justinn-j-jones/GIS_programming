# part 1 

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

num = 1

for i in part1:
    num = num * i

print('The result for part 1 is:', num)

# part 2 

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

num2 = 0

for i in part2: 
    num2 = num2 + i

print('The result for part 2 is:', num2)

# part 3 

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

num3 = 0

for i in part3:
    if i %2 == 0:
        num3 = num3 + i

print('The result for part 3 is:', num3)
