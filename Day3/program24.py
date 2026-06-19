import copy
original_list = ["Coding", ["Python", "Java"], 2024]
copied_list = copy.deepcopy(original_list)
copied_list[1][1] = "C++"
copied_list[2] = 2028
print("--- Deep Copy Verification ---")
print("Original List: ", original_list)
print("Copied List:   ", copied_list)
