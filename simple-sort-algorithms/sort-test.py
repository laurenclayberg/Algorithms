import sort

t_1 = [24,97,8,102,13,85,44,5,15,17,9,20,9,36,45,71]
t_2 = [10,9,8,7,6,5,4,3,2,1,0]
t_3 = [3,-4,7,8,9,-6,-5,-6,6,7,8,-9,9,-9,3,2,1,2,-3,4,-5,6,-7,-8,5,-5,6,6,-4,3,-2,7,9,0,0]
t_4 = [7,2,4,8,9,-3,-6,-86,-4,-3,-67, 0.4, 100.4, -0.1, -100.89]

tests = [t_1,t_2,t_3,t_4]

for test in tests:
    assert sort.insertion_sort(test.copy()) == sorted(test.copy())
    assert sort.merge_sort(test.copy()) == sorted(test.copy())
    assert sort.heap_sort(test.copy()) == sorted(test.copy())