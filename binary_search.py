def binary_search(input_array, search_element, low, high):
    """Binary search can be implemented only in a sorted array.
    It works by repeatedly dividing the search range in half until
    the target element is found or it's determined that the
    element doesn't exist in the array. """
    # Failsafe condition
    if low > high:
        return -1
    # Determine the mid point
    mid = (low + high)//2
    if search_element == input_array[mid]:
        print("Element found")
        return mid
    # Search left array
    elif search_element < input_array[mid]:
        binary_search(input_array, search_element, low, mid-1)
    # Search right array
    else:
        binary_search(input_array, search_element, mid+1, high)


if __name__ == '__main__':
    array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    binary_search(array, 8, 0, len(array)-1)