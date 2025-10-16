def linear_search(data_list,target):
    for i in data_list:
        if i == target:
            return True
    return False
print(linear_search([1,2,3,4,5],5))