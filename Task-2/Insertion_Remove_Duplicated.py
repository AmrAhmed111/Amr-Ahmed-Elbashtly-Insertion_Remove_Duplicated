# Solve the problem of deleting duplicate elements using the insertion algorithm
def remove_duplicates(arr):
    if not arr:
        return arr
    
    # We sort the matrix first.
    arr.sort()
    
    # We start from the second element
    i = 1
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            # If the current item is a duplicate, we remove it.
            arr.pop(i)
        else:
            i += 1
    return arr


def get_array_from_user():
    # We ask the user to enter the elements of the array.
    user_input = input("Enter the elements of the array separated by space: ")
    
    # Convert the input to a list of integers.
    try:
        arr = list(map(int, user_input.split()))
        return arr
    except ValueError:
        print("Error: Make sure to enter only valid numbers.")
        return None
    
# We receive the array from the user
arr = get_array_from_user()
if arr is not None:
    # Remove duplicate items
    result = remove_duplicates(arr)
    print("Matrix after removing duplicates: ", result)