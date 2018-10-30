"""
插入排序
"""
from base import Comparable, Base


class Shell(Base):
    def sort(self, a:[Comparable]):
        # h为步长
        h = len(a) // 2
        while(h >=1):# 针对每一个步进做插入排序
            print("h{}".format(h))
            # 针对一个步进的每一个序列做插入排序
            for i in range(0, len(a)%h + 1): 
                
                # 针对每一个序列做插入排序
                for j in range(i, len(a), h):
                    for k in range(i, j, h):
                        print("i{}".format(i))
                        print("j{}".format(j))
                        print("k{}".format(k))
                        print(j-h*k)
                        if self.less(a[j], a[k]):
                            self.exch(a, j, k)
            h = h // 2 #直到步长为1

def main():
    test_list = [1,4,5,3,14,23,50,3,100,201,22,21]
    comparable_list = [Comparable(i) for i in test_list]
    sort_method = Shell()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))

if __name__ == '__main__':
    main()