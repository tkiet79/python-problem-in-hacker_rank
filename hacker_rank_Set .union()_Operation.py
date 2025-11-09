
n1 = int(input())
student_number_1 = set(map(int,input().split()))
n2 = int(input())
student_number_2 = set(map(int,input().split()))

# cách 1: dùng toán tử & nghĩa là gộp giá trị của 2 tập hợp lại thành 1
common_part = student_number_1 & student_number_2
total = len(student_number_1) + len(student_number_2) - len(common_part)
print(total)

# cách 2: dùng union() cũng giống như toán tử &
total_subscribers = student_number_1.union(student_number_2)

print(len(total_subscribers))

