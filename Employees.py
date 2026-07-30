employees = [
    ["Alice", "Sales", 90, 95, 85],
    ["Bob", "IT", 60, 70, 65],
    ["Charlie", "Sales", 45, 50, 40],
    ["Diana", "HR", 85, 90, 92],
    ["Evan", "IT", 95, 80, 88],
    ["Fiona", "HR", 70, 75, 80]
]

W_PRODUCTIVITY = 0.4
W_ATTENDANCE = 0.3
W_TEAMWORK = 0.3

def get_rating(score):
    if score >= 85: return "Excellent"
    elif score >= 70: return "Good"
    elif score >= 50: return "Average"
    else: return "Poor"

processed_employees = []
dept_scores = {}

for name, dept, prod, att, team in employees:
    weighted_score = (prod * W_PRODUCTIVITY) + (att * W_ATTENDANCE) + (team * W_TEAMWORK)
    rating = get_rating(weighted_score)
    processed_employees.append({"name": name, "dept": dept, "score": weighted_score, "rating": rating})
    
    if dept not in dept_scores:
        dept_scores[dept] = []
    dept_scores[dept].append(weighted_score)

print("--- TOP 3 EMPLOYEES ---")
top_three = sorted(processed_employees, key=lambda x: x["score"], reverse=True)[:3]
for idx, emp in enumerate(top_three, 1):
    print(f"{idx}. {emp['name']} ({emp['dept']}) - Score: {emp['score']:.1f} [{emp['rating']}]")

print("\n--- DEPARTMENT-WISE AVERAGE SCORE ---")
for dept, scores in dept_scores.items():
    avg_score = sum(scores) / len(scores)
    print(f"Department: {dept} | Average Score: {avg_score:.1f}")
