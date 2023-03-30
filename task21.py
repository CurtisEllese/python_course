# Напишите программу для печати всех уникальных значений в словаре. 

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

output = set()
for dict in input:
    val_set = set(dict.values())
    output |= val_set
print(output)

# output = set()
# for dict in input:
#     for val in dict.values():
#         output.add(val)
# print(output)

# print(set(v for d in input for v in d.values()))
