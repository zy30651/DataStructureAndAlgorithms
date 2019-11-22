# 归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
# 将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，
# 谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，
# 最后把另一个数组的剩余部分复制过来即可。
"""
最优时间复杂度：O(nlogn)
最坏时间复杂度：O(nlogn)
稳定性：稳定
"""


from day01.utils import time_deco, random_nums
@time_deco
def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist)//2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    """合并操作，将2个有序数组left[]、right[]合并到一个大的有序数组"""
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    li = random_nums()
    merge_sort(li)
# 0.053秒