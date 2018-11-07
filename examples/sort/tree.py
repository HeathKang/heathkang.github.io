"""
堆排序
"""

from base import Comparable, Base


class Tree(Base):
    def sink(self, a:[Comparable], pos:int, length:int):
        while (pos * 2 <= length):
            j:int = pos * 2
            if (j< length and self.less(a[j], a[j+1])):
                j = j + 1
            if self.less(a[pos], a[j]):
                self.exch(a, pos, j)
                pos = j
            else:
                break

    def sort(self, a:[Comparable]):
        # 构造堆
        a.insert(0,Comparable(0))
        length = len(a) - 1
        for i in range(length//2, 0, -1):
            self.sink(a, i, length)
        for i in a:
            print(i)
        # 排序
        while length > 1:
            self.exch(a, 1, length)
            length = length - 1
            self.sink(a, 1, length)
        

        

def main():
    test_list = [1,4,5,3,14,23,50,3,100,201,22,21]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Tree()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()