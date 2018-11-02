"""
快速排序
"""
import random
from base import Comparable, Base
from copy import deepcopy

class Quick(Base):
    def sort(self, a:[Comparable]):
        random.shuffle(a) # 让数组变得更加无序
        self.sort_individual(a, 0, len(a) - 1)

    def sort_individual(self, a:[Comparable], lo:int, hi:int):
        # 到极限情况
        if lo >= hi:
            return
        mid = self.partition(a, lo, hi)
        
        self.sort_individual(a, lo, mid-1)
        self.sort_individual(a, mid+1, hi)

    def partition(self, a:[Comparable], lo:int, hi: int) -> int:
        """
        切分a[lo]到这个序列的正确位置,并返回这个位置;
        """
        value: Comparable = a[lo]
        pos = lo # 记录初始位置
        lo = lo + 1 # 从下一位开始
        while(hi > lo):
            if self.less(a[hi], value) and self.less(value, a[lo]):# 右端元素<value，左端元素>=value，明显需要互换
                self.exch(a, lo, hi)
                lo = lo + 1
                hi = hi - 1
            elif not self.less(a[hi], value) and  self.less(value, a[lo]):# 右端元素>=value, 左端元素>=value，右边指针向左移动，左边指针等待
                hi = hi - 1
            elif self.less(a[hi], value) and not self.less(value, a[lo]):# 右端元素<value, 左端元素<value，右边指针等待，左边向右移动
                lo = lo + 1
            elif not self.less(a[hi], value) and not self.less(value, a[lo]):#右端元素>=value，左端元素<value，指针同时移动
                lo = lo + 1
                hi = hi - 1
            print("lo {}".format(lo))
            print("hi {}".format(hi))

        if hi == lo: # 指针落在中间一个元素上，需要区分这个元素>=还是<value
            if self.less(value, a[hi]):
                self.exch(a, pos, hi - 1)
                return hi - 1
            else:  
                self.exch(a, pos, hi)
                return hi
        else: # 指针移动交叉，这时指针位置hi<lo，a[hi]为较小元素的边界位置
            self.exch(a, pos, hi)
            return hi
            


def main():
    test_list = [1,4,5,3,14,23,50,3,100,201,22,21,2,7,9,5]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Quick()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()