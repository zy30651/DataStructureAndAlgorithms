import time

# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# 方法1：三重循环
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a**2 + b**2 == c**2 and a+b+c == 1000:
#                 print('a, b, c: %d, %d, %d' % (a, b, c))
# end_time = time.time()
# print('耗时：%f' % (end_time - start_time))        # 耗时：945.267512
# print('complete!')
# 本案例共计计算步数为：1000*1000*1000*2
# 采用问题规模N来标记：  N  *  N *  N *2 = 2 * N^3
# 采用时间复杂度T(N)标记：T(N)=2 * N^3        T(n) = O(n*n*n) = O(n3)
# 最终用大O记法为：O(N^3)

# 方法2：二重循环
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print('a, b, c: %d, %d, %d' % (a, b, c))
end_time = time.time()
print('耗时：%f' % (end_time - start_time))        # 耗时：0.517660
print('complete!')
# 本案例共计计算步数为：1000*1000*3
# 采用问题规模N来标记：  N  *  N * 3 = 3 * N^2
# 采用时间复杂度T(N)标记：T(N)=3 * N^2
# 最终用大O记法为：O(N^2)




