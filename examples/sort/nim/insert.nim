"""
希尔排序
"""
import base

type
    Insertion ref of Base

method sort*(base: Base, a: seq[Comparable]): 
    for i in a:
        for j in range(i):
            if base.less(a[i], a[j]):
                base.exch(a, i, j)

    
proc main():
    test_list: seq[] = @[1,4,5,3,14,23,50]
    comparable_list: seq[Comparable] = [Comparable(i) for i in test_list]
    sort_method = Insertion()
    sort_method.sort(comparable_list)
    
    sort_method.show(comparable_list)
    print(sort_method.inSorted(comparable_list))