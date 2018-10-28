"""
冒泡排序
"""
from base import Comparable, Base


class Bubble(Base):
    def sort(self, a:[Comparable]):
        for i in range(len(a)):
            for j in range(len(a) - i - 1):
                if self.less(a[j+1], a[j]):
                    self.exch(a, j, j+1)


def main():
    test_list = [1,4,5,3,14,23,50]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Bubble()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()