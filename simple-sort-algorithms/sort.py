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

        Expected input:
        Must be a list with only real numbers (int or float)
        and at least one value
    '''
    def heapify(input):
        ''' Heap Sort Helper
            O(n) create a min heap from input
        '''
        for index in range(len(input)):
            current_index = index
            while current_index > 0:
                parent_index = int((current_index - 1) / 2)
                if input[current_index] < input[parent_index]:
                    swap = input[current_index]
                    input[current_index] = input[parent_index]
                    input[parent_index] = swap
                    current_index = parent_index
                else:
                    break
        return input

    def extract_min(input):
        ''' Heap Sort Helper
            O(log n) extract min value and re-heapify

            Only O(log n) if the input heap is balanced

            returns (min_value, heap of size n - 1)
        '''
        min_value = input[0]
        index = 0
        while True:
            index_left = index * 2 + 1
            index_right = index * 2 + 2
            child_left = input[index_left] if index_left < len(input) else None
            child_right = input[index_right] if index_right < len(input) else None
            if child_left == None and child_right == None:
                input[index] = None
                return (min_value, input)
            elif child_left != None and child_right == None:
                input[index] = child_left
                input[index_left] = None
                index = index_left
            elif child_left == None and child_right != None:
                input[index] = child_right
                input[index_right] = None
                index = index_right
            else:
                if child_left < child_right:
                    input[index] = child_left
                    input[index_left] = None
                    index = index_left
                else:
                    input[index] = child_right
                    input[index_right] = None
                    index = index_right

    if len(input) == 1:
        return input
    else:
        heap = heapify(input)
        sorted_list = []
        for i in range(len(input)):
            min_value, heap = extract_min(heap)
            sorted_list.append(min_value)
        return sorted_list
