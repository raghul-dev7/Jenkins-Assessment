# Employee Performance Evaluation

employees = [
    ["Ramesh", "IT", 90, 95, 88],
    ["Suresh", "HR", 75, 80, 78],
    ["Anitha", "IT", 85, 90, 92],
    ["Kiran", "Sales", 65, 70, 68],
    ["Meena", "HR", 95, 98, 96]
]

print("EMPLOYEE PERFORMANCE")
print("-" * 40)

dept_total = {}
dept_count = {}

for emp in employees:
    name = emp[0]
    dept = emp[1]
    productivity = emp[2]
    attendance = emp[3]
    teamwork = emp[4]

    score = productivity * 0.5 + attendance * 0.3 + teamwork * 0.2

    if score >= 90:
        rating = "Excellent"
    elif score >= 75:
        rating = "Good"
    elif score >= 60:
        rating = "Average"
    else:
        rating = "Poor"

    emp.append(score)

    print("Name      :", name)
    print("Department:", dept)
    print("Score     :", round(score, 2))
    print("Rating    :", rating)
    print()

    if dept in dept_total:
        dept_total[dept] += score
        dept_count[dept] += 1
    else:
        dept_total[dept] = score
        dept_count[dept] = 1

# Top Three Employees
employees.sort(key=lambda x: x[5], reverse=True)

print("TOP THREE EMPLOYEES")
for i in range(3):
    print(i + 1, ".", employees[i][0], "-", round(employees[i][5], 2))

# Department-wise Average
print("\nDEPARTMENT-WISE AVERAGE SCORE")
for dept in dept_total:
    average = dept_total[dept] / dept_count[dept]
    print(dept, ":", round(average, 2))
