length_list1 = int(input())
input1 = input()
input_set1 = set(list(map(int, input1.split())))

length_list2 = int(input())
input2 = input()
input_set2 = set(list(map(int, input2.split())))

special_list = sorted(input_set1.difference(input_set2).union(input_set2.difference(input_set1)))

print("\n".join(map(str,special_list)))