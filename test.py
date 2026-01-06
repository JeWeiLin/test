# record = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
        
#     record.append([name, score])

# grade_record = sorted(set([score for name, score in record]))
    
# second_lowest_grade = grade_record[1]
    
# second_lowest_students = sorted([name for name, score in record if score == second_lowest_grade])  
    
# for student in second_lowest_students:  # Print each student's name 
#     print(student)


# def detectFirstAnomaly(metrics):
#     if not metrics or len(metrics) < 2:
#         return -1
    
#     max_observed = metrics[0]
    
#     for i in range(1, len(metrics)):
#         current_value = metrics[i]
        
#         if current_value >= 3 * max_observed:
#             return i
        
#         if current_value > max_observed:
#             max_observed = current_value
            
#     return -1

# metrics = [3, 10, 2, 7]
# print(detectFirstAnomaly(metrics))


# squares = []
# for i in range(1, 10):
#     squares.append(i**2)

# print(squares)


def detectFirstAnomaly(metrics):
    if len(metrics) < 2:
        return -1
    
    max_elements = metrics[0]
    
    for i, val in enumerate(metrics[1:], start=1):
        if val >= 3 * max_elements:
            return i
        if val > max_elements:
            max_elements = val
            
    return -1

metrics = [10, 3, 5, 1, 8]

print(detectFirstAnomaly(metrics))