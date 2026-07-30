# Employee Performance Evaluation

employees = [
    {"name": "Ravi", "department": "HR", "productivity": 85, "attendance": 90, "teamwork": 80},
    {"name": "Priya", "department": "IT", "productivity": 95, "attendance": 88, "teamwork": 92},
    {"name": "Arun", "department": "HR", "productivity": 75, "attendance": 80, "teamwork": 78}
]

# Weightages
wp = 0.5      # Productivity - 50%
wa = 0.3      # Attendance - 30%
wt = 0.2      # Teamwork - 20%

# Calculate score and rating
for emp in employees:
    score = (emp["productivity"] * wp +
             emp["attendance"] * wa +
             emp["teamwork"] * wt)

    emp["score"] = score

    if score >= 90:
        emp["rating"] = "Excellent"
    elif score >= 75:
        emp["rating"] = "Good"
    elif score >= 60:
        emp["rating"] = "Average"
    else:
        emp["rating"] = "Poor"

# Display employee details
print("Employee Details")
for emp in employees:
    print("----------------------------")
    print("Name       :", emp["name"])
    print("Department :", emp["department"])
    print("Score      :", round(emp["score"], 2))
    print("Rating     :", emp["rating"])

# Display top three employees
print("\nTop Three Employees")
top = sorted(employees, key=lambda x: x["score"], reverse=True)

for i in range(3):
    print(i + 1, ".", top[i]["name"], "-", round(top[i]["score"], 2))

# Department-wise average score
print("\nDepartment-wise Average Score")

dept = {}

for emp in employees:
    d = emp["department"]
    if d not in dept:
        dept[d] = []
    dept[d].append(emp["score"])

for d in dept:
    avg = sum(dept[d]) / len(dept[d])
    print(d, ":", round(avg, 2))
