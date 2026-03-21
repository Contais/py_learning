def is_prime(num):
    """判断是否为质数"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def num_sum(num_list):
    """数字列表求和"""
    return sum(num_list)