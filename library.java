import java.util.*;

class Book {
    String title;
    String author;
    int availableCopies;
    int borrowedCount;

    Book(String title, String author, int availableCopies, int borrowedCount) {
        this.title = title;
        this.author = author;
        this.availableCopies = availableCopies;
        this.borrowedCount = borrowedCount;
    }
}

public class Library {
    public static void main(String[] args) {

        Book[] books = {
            new Book("Java Programming", "James", 5, 40),
            new Book("Python Basics", "Guido", 0, 55),
            new Book("Data Structures", "Mark", 3, 30),
            new Book("DBMS", "Navathe", 0, 45),
            new Book("Operating Systems", "Silberschatz", 7, 25)
        };

        // Most Borrowed Book
        Book most = books[0];
        for (Book b : books) {
            if (b.borrowedCount > most.borrowedCount) {
                most = b;
            }
        }

        System.out.println("Most Borrowed Book");
        System.out.println("Title : " + most.title);
        System.out.println("Author: " + most.author);
        System.out.println("Borrowed Count: " + most.borrowedCount);

        // Books with Zero Available Copies
        System.out.println("\nBooks with Zero Available Copies");
        for (Book b : books) {
            if (b.availableCopies == 0) {
                System.out.println(b.title);
            }
        }

        // Total Books Available
        int total = 0;
        for (Book b : books) {
            total += b.availableCopies;
        }
        System.out.println("\nTotal Books Available: " + total);

        // Sort by Popularity
        Arrays.sort(books, (a, b) -> b.borrowedCount - a.borrowedCount);

        System.out.println("\nBooks Sorted by Popularity");
        for (Book b : books) {
            System.out.println(b.title + " - Borrowed: " + b.borrowedCount);
        }

        // Summary Report
        System.out.println("\nLibrary Summary Report");
        for (Book b : books) {
            System.out.println("----------------------------");
            System.out.println("Title      : " + b.title);
            System.out.println("Author     : " + b.author);
            System.out.println("Available  : " + b.availableCopies);
            System.out.println("Borrowed   : " + b.borrowedCount);
        }
    }
}
