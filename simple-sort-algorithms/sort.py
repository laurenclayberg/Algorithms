def insertion_sort(input):
    ''' Insertion Sort

        Runtime: O(n^2) worst case, best case O(n)
        Space Complexity: O(1) extra space worst case (in place)

        Expected input:
        Must be a list with only real numbers (int or float)
        and at least one value
    '''
    for idx in range(1, len(input)):
        idx_swap = idx
        while idx_swap >= 1 and input[idx_swap] < input[idx_swap - 1]:
            swap = input[idx_swap]
            input[idx_swap] = input[idx_swap - 1]
            input[idx_swap - 1] = swap
            idx_swap -= 1
    return input

def merge_sort(input):
    ''' Merge Sort [Recursive implementation]

        Runtime: O(n log n) worst case
        Space Complexity: O(n)

        Expected input:
        Must be a list with only real numbers (int or float)
        and at least one value
    '''

    def merge(left, right):
        ''' Merge Sort Helper
        
            Left are right will be sorted lists of numbers
            to be combined into one sorted list
        '''
        merged = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        merged.extend(left[l:])
        merged.extend(right[r:])
        return merged

    if len(input) == 1:
        return input
    else:
        mid_idx = int(len(input) / 2.0)
        left = merge_sort(input[:mid_idx])
        right = merge_sort(input[mid_idx:])
        return merge(left, right)

def heap_sort(input):
    ''' Heap Sort

        Runtime: (n log n) [making the heap is O(n)]
        Space Complexity: O(1) extra space worst case
    '''
    def heapify(input):
        ''' Heap Sort Helper
            O(n) create heap from input
        '''
        # todo