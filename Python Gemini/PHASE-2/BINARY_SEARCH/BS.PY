def binary_search(sorted_list, target):
    low = 0
    # Fix A: Initialize high on a separate line or use proper tuple unpacking
    high = len(sorted_list) - 1 

    # Fix B: Must be <= to check the single element where low meets high
    while low <= high: 
        # Fix C: Use integer division (//) for array indices
        mid = (low + high) // 2 

        if sorted_list[mid] == target:
            # Fix D: Return the index 'mid' directly
            return mid 
        
        elif sorted_list[mid] < target:
            # Target is in the right half
            low = mid + 1 
            
        else: # sorted_list[mid] > target
            # Target is in the left half
            high = mid - 1 

    # If the loop finishes without finding the target
    return -1

# Fix E: The sorted list must be passed or assigned correctly
print(f"Index of 3: {binary_search([1, 3, 4, 5], 3)}") 
# Output: Index of 3: 1 (which is the correct index)