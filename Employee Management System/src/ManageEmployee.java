import java.util.ArrayList;
import java.util.Scanner;

public class ManageEmployee {

    private static ArrayList<Employee> employees = new ArrayList<>();
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {

        while (true) {
            System.out.println("\n==== Employee Management System ====");
            System.out.println("1. Add Employee");
            System.out.println("2. View Employees");
            System.out.println("3. Delete Employee");
            System.out.println("4. Exit");

            System.out.print("Enter choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    addEmployee();
                    break;
                case 2:
                    viewEmployees();
                    break;
                case 3:
                    deleteEmployee();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice!");
            }
        }
    }

    private static void addEmployee() {
        System.out.print("Enter ID: ");
        int id = sc.nextInt();

        sc.nextLine();
        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Salary: ");
        double salary = sc.nextDouble();

        employees.add(new Employee(id, name, salary));
        System.out.println("Employee added successfully!");
    }

    private static void viewEmployees() {
        if (employees.isEmpty()) {
            System.out.println("No employees found.");
            return;
        }

        System.out.println("\nEmployee List:");
        for (Employee emp : employees) {
            emp.display();
        }
    }

    private static void deleteEmployee() {
        System.out.print("Enter Employee ID to delete: ");
        int id = sc.nextInt();

        boolean found = false;

        for (int i = 0; i < employees.size(); i++) {
            if (employees.get(i).getId() == id) {
                employees.remove(i);
                found = true;
                System.out.println("Employee deleted successfully!");
                break;
            }
        }

        if (!found) {
            System.out.println("Employee not found!");
        }
    }
}