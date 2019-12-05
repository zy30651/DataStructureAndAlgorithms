import random
import time

#
# start = time.time()
# merge_sort(li)
# end = time.time()
# print(end-start)


def random_nums(max_value=200000, total_nums=10000):
    num_list = []
    for i in range(total_nums):
        num_list.append(random.randint(1, max_value))
    return num_list


def time_deco(sort_func):
    """时间装饰器函数"""
    def wrapper(num_list):
        start_time = time.time()
        sort_func(num_list)
        end_time = time.time()
        print('耗时为：', (end_time-start_time))
    return wrapper


def time_mut_deco(sort_func):
    """时间装饰器函数"""
    def wrapper(num_list, start, end):
        start_time = time.time()
        sort_func(num_list, start, end)
        end_time = time.time()
        print('耗时为：', (end_time-start_time))
    return wrapper


def time_search(search_func):
    """时间装饰器函数"""
    def wrapper(num_list, item):
        start_time = time.time()
        search_func(num_list, item)
        end_time = time.time()
        print('耗时为：', (end_time-start_time))
    return wrapper
