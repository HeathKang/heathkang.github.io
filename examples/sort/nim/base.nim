"""
nim base moudle
"""

type
    Base* = ref object

method sort*(base: Base, a: Comparable[]): =
    ...

method isSorted(base: Base, a: seq[Comparable]): bool =
    for i in range(len(a) - 1):
        if Base.less(a[i+1], a[i])
        return False

method less(a: Comparable, b: Comparable): bool =
    return a.compareTo(b) < 0

method exch(a: seq[Comparable], i: int, j: int): =
    temp: Comparable = a[i]
    a[i] = a[j] 
    a[j] = temp


type
    Comparable*[T] = ref object
    data: T

method compareTo(a, b:Comparable): bool =
    if a.data > b.data:
        return 1
    else:
        return -1
        
    

