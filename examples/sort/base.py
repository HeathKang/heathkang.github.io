"""
排序模型
"""
from typing import TypeVar, Generic, Sized
T = TypeVar('T')

class Comparable(Generic[T]):
    def __init__(self, a:T):
        self.value = a
    
    def compareTo(self, b:any) -> int:
        if self.value >= b.value:
            return 1
        else:
            return -1
    
    def __str__(self) -> str:
        return str(self.value)


class Base:
    def __init__(self):
        pass
    
    def sort(self, a:[Comparable]):
        pass
    
    def less(self, a:Comparable, b:Comparable) -> bool:
        return a.compareTo(b) < 0

    def exch(self, a:[Comparable], i:int, j:int):
        t = a[i]
        a[i] = a[j]
        a[j] = t
    
    def show(self, a:[Comparable]):
        print("sorted is: \n")
        for i in a:
            print("{} \n".format(i))
    
    def inSorted(self, a: [Comparable]) -> bool:
        for i in range(len(a) - 1):
            if self.less(a[i+1], a[i]):
                return False
        else:
            return True

def main():
    test_list = [1,2,3,4,5]
    comparelist = [Comparable(i) for i in test_list]
    for i in comparelist:
        print(i)


if __name__ == '__main__':
    main()