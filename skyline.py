# Add your clarifying questions here
# input: [-1, 1, 3, 7, 7, 3] output:[1,3,7]
# input: [-1, 5, 3, 7, 7, 3] output:[5,7]
# [7,7,7]
def skyline(building_list):
    output = []
    for i in range(len(building_list)):
        if i == 0 and building_list[0]>0:
            output.append(building_list[0])
            continue
        elif i == 0 and building_list[0]<0:
            continue
        # 
        check_list = building_list[0:i]
        if building_list[i] > max(check_list):
            output.append(building_list[i])
        elif building_list[i] == max(check_list):
            if max(check_list) not in output:
                output.append(building_list[i])
        
    return output

print(skyline([-1, 1, 3, 7, 7, 3]))
print(skyline([-1, 5, 3, 7, 7, 3]))
print(skyline([5, 3, 7, 7, 3]))
print(skyline([6,7,6,7,7]))