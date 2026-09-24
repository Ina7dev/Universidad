package Laboratorio2;
import java.util.Scanner;

public class lab2ejer2 {
    public static void main(String[] args) {
        Scanner keyword = new Scanner(System.in);
        
        
        System.out.print("Ingrese su edad: ");
        int edad = keyword.nextInt();
        
        
        if (edad < 5 && edad > 0) {
            System.out.println("Niños: Entrada gratuita.");
        }
        else if (edad >= 5 && edad <= 12) {
            System.out.println("Niños mayores: Valor de entrada de $1500");
        }
        else if (edad >= 13 && edad <= 17) {
            System.out.println("Jovenes: Valor de entrada de $3000");
        }
        else if (edad >= 18 && edad <= 64) {
            System.out.println("Adultos: Valor de entrada de $5000");
        }
        else if (edad >= 65 && edad < 100) {
            System.out.println("Adulto mayor: Valor de entrada de $2000");
        }
        else {
            System.out.println("Error: ingrese una edad válida.");
        }
        
        keyword.close();
    }
}
