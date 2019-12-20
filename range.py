#清单产生器
import random

range(5) #[0, 1, 2, 3, 4]
range(3) #[0, 1, 2]
range(2, 5) # [2,3,4] 开始值包含，结尾不包含
range(8, 10) # [8, 9]
range(2, 10, 3) #[2, 5, 8] 开始值，每次增加2+第三个值（递增值，step值），第二个数字是结束范围
range(10, 3, -2) #[10, 8, 6, 4]

for i in range(100): #执行固定次数
	r = random.randint(1, 1000)
	print('这是第', i+1, '次产生随机数:', r) 
	