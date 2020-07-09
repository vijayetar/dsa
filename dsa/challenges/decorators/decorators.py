from functools import wraps, singledispatch
from time import time
#_________________________________________________________________________
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

def say_nothing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"{func(*args, *kwargs)} ...... <awkard silence>"
    return wrapper
@timing
def very_excited(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        return  f"{func(*args,*kwargs)}?!?!"
    return wrapper

@say_nothing
@very_excited
def invite_friends(txt):
    return txt
#___________________________________________________

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        return f"hi there, {arg}!!"
    return arg

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        return f"{arg} is NOT enough!!"
    return f"have {arg} of it"

@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        for i,item in enumerate(arg):
            print(f"Please get this: {i+1}. {item.upper()}")
        return
    return f"This {len(arg)} in the list is too much "

@fun.register(float)
def _(arg,verbose=False):
    if verbose:
        return f"this is {arg} that needs to be converted into fraction"
    return f"please select {arg} wisely"
#_______________________________________________________

@timing
def f(a):
    for _ in range(a):
        i=0
    return -1

@timing
def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr)-1
    if left < right:
        pos = partition(arr,left,right)
        quick_sort(arr, left, pos-1)
        quick_sort(arr, pos+1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    low = left-1
    # iterate over left to the pivot-1
    for i in range(left,right):
        if arr[i]<= pivot:
            low = low + 1
            swap(arr, i, low)
    swap(arr, right, low+1)
    return low+1

def swap(arr, i, low):
    arr[i], arr[low] = arr[low], arr[i]
    return



if __name__ == "__main__":
    print(invite_friends("Do you want to come?"))
    print(fun("Karen", verbose=True))
    print(fun(12, verbose=True))
    print(fun(["lemons","honey"]))
    print(fun(["lemons","honey"], verbose=True))
    print(fun(0.12))
    print(fun(0.12, verbose=True))
    print(f(10000000))
    print(quick_sort([5,4,33,5,3,7,876]))
