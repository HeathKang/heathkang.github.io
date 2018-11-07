"""
基于堆的优先队列
"""
from base import Comparable, Base

class MaxPQ(Base):
    def __init__(self, pq:[Comparable]):
        self.pq: [Comparable] = pq
        self.length: int = len(self.pq) - 1
    
    def size(self) -> int:
        return self.length

    def isEmpty(self) -> int:
        return self.length <= 0
    
    def insert(self,value: Comparable):
        self.pq.append(value)
        self.length = len(self.pq) - 1
        self.swim(self.length)
    
    def delMax(self):
        self.exch(self.pq, 1, self.length)
        max:Comparable = self.pq.pop() # 交换后弹出最大元素 
        self.sink(1)
        return max

    def swim(self, pos:int):
        """
        上浮法，从下而上，找到元素的真正位置
        """
        while pos > 1 and self.less(self.pq[pos//2], self.pq[pos]):
            self.exch(self.pq, pos//2, pos) # 当父节点比元素小时，且自己不是根节点时，与自己的父节点进行交换
            pos: int = pos // 2
    
    def sink(self, pos:int):
        """
        下沉法，从上而下，找到元素的真正位置
        """
        while(pos*2 <= self.length):
            j: int = pos * 2
            if (j < self.length and self.less(self.pq[j],self.pq[j+1])):
                j = j + 1 #寻找子树上较大的节点来进行下一步的比较和交换
            if self.less(self.pq[pos], self.pq[j]):
                self.exch(self.pq, pos, j)
                pos = j
            else:
                break # 父节点大于子节点，说明已交换到位置
    
    def show_pq(self):
        print("sorted is: \n")
        for i in self.pq:
            print("{} \n".format(i))

def main():
    test_list = [0,55,33,44,22,21,19,18,16,17,14,13,10,9,8,7]
    comparable_list = [Comparable(i) for i in test_list]
    pq = MaxPQ(comparable_list)
    pq.insert(Comparable(30))
    pq.show_pq()
    max = pq.delMax()
    pq.show_pq()


if __name__ == '__main__':
    main()