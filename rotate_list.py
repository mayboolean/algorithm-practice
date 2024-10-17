# Add your clarifying questions here

def rotate_list(list, shift_by):
    shift_by_i = len(list) - (shift_by % len(list))
    list = list[shift_by_i::] + list[0:shift_by_i]
    return list
 
print(rotate_list([1,2,3,4,5], 3))
print(rotate_list(["a", "b", "c"], 1))