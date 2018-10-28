"""
选择排序
"""
from base import Base, Comparable
class Selection(Base):
    def sort(self, a: [Comparable]):
        for i in range(len(a)):
            min = i
            for j in range(i, len(a)):
                if self.less(a[j], a[min]):
                    min = j
                    
            self.exch(a, i, min)


def main():
    test_list = [2,4,1,14,23,50]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Selection()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()
            
                