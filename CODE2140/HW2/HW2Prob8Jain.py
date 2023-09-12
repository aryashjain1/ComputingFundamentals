def num_stats(in_list):
    in_list.sort()
    num_freqs = {}
    num_list = []
    for i in range(len(in_list)):
        if in_list[i] not in num_freqs:
            num_freqs[in_list[i]] = 1
            num_list.append(in_list[i])
        else:
            num_freqs[in_list[i]] += 1
    num_list.sort(reverse=True)
    return (num_freqs, num_list)

nums = [1,3,5,6,8,9,10,15,1,4,3,6,8,8,17]
nums_dict, nums_list = num_stats(nums)
print("Number\t\tFrequency")
for num in nums_list:
    print(f'{num}\t\t{nums_dict[num]}')

all_nums_set = set()
for i in range(nums_list[0]):
    all_nums_set.update([i+1])
left_out_set = all_nums_set.difference(set(nums_list))
print("Left out numbers:",left_out_set)
