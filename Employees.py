import java.util.*;

class Employee {
    String name, department;
    int productivity, attendance, teamwork;
    double score;
    String rating;

    Employee(String name, String department, int productivity, int attendance, int teamwork) {
        this.name = name;
        this.department = department;
        this.productivity = productivity;
        this.attendance = attendance;
        this.teamwork = teamwork;

        score = productivity * 0.5 + attendance * 0.3 + teamwork * 0.2;

        if (score >= 90)
            rating = "Excellent";
        else if (score >= 75)
            rating = "Good";
        else if (score >= 60)
            rating = "Average";
        else
            rating = "Poor";
    }
}

public class Employees {
    public static void main(String[] args) {

        Employee[] emp = {
            new Employee("Ravi", "IT", 90, 95, 85),
            new Employee("Priya", "HR", 80, 88, 90),
            new Employee("Karthik", "IT", 70, 75, 72),
            new Employee("Meena", "Sales", 95, 96, 94),
            new Employee("Arun", "HR", 65, 70, 68)
        };

        System.out.println("Employee Details");
        System.out.println("------------------------------");

        for (Employee e : emp) {
            System.out.println("Name       : " + e.name);
            System.out.println("Department : " + e.department);
            System.out.println("Score      : " + String.format("%.2f", e.score));
            System.out.println("Rating     : " + e.rating);
            System.out.println();
        }

        Arrays.sort(emp, (a, b) -> Double.compare(b.score, a.score));

        System.out.println("Top Three Employees");
        for (int i = 0; i < 3; i++) {
            System.out.println((i + 1) + ". " + emp[i].name + " - " + String.format("%.2f", emp[i].score));
        }

        HashMap<String, Double> total = new HashMap<>();
        HashMap<String, Integer> count = new HashMap<>();

        for (Employee e : emp) {
            total.put(e.department, total.getOrDefault(e.department, 0.0) + e.score);
            count.put(e.department, count.getOrDefault(e.department, 0) + 1);
        }

        System.out.println("\nDepartment-wise Average Score");
        for (String dept : total.keySet()) {
            double avg = total.get(dept) / count.get(dept);
            System.out.println(dept + " : " + String.format("%.2f", avg));
        }
    }
}
