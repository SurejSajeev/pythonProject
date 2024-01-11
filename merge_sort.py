list_to_sort = [1,5,10,12,6,9]


def mergesort(input_array):
    """Merge sort with split the array into half and
    keep doing it until it has a single element to sort,
    and then it will merge the sorted arrays."""
    if len(input_array) > 1:
        # Split the input array into two halves
        l_array = input_array[:len(input_array)//2]
        r_array = input_array[len(input_array)//2:]

        mergesort(l_array)
        mergesort(r_array)

        # Initialize all pointers to 0
        i = j = k = 0

        # This while loop is to compare l_array and r_array and then replace the lowest value
        # from either one of the arrays as an element in the main array.
        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                input_array[k] = l_array[i]
                i += 1
            else:
                input_array[k] = r_array[j]
                j += 1
            k += 1

        # After the previous while loop we will have elements in either l_array or r_array
        # These two while loops will merge them to the input array.
        while i < len(l_array):
            input_array[k] = l_array[i]
            i += 1
            k += 1

        while j < len(r_array):
            input_array[k] = r_array[j]
            j += 1
            k += 1
    return input_array

if __name__ == '__main__':
    print(mergesort(list_to_sort))