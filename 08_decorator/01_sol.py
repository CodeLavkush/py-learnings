import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

def funcCount(func):
    def wrapper(*args):
        argsCount = len(args)
        result = func(*args)
        print(f"{func.__name__} has {argsCount} arguments!")
        return result
    return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(4)

@funcCount
def displayNums(nums):
    for i in nums:
        print(i)

displayNums([1,2,3,4,5,6,7,8,9])