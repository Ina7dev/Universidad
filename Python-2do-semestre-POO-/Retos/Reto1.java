package Retos;
import java.util.Scanner;

public class Reto1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el primer número: ");
        double numero1 = scanner.nextDouble();

        System.out.print("Ingresa el segundo número: ");
        double numero2 = scanner.nextDouble();

        System.out.println("Elige una operación: ");
        System.out.println("1. Suma");
        System.out.println("2. Resta");
        System.out.println("3. Multiplicación");
        System.out.println("4. División");

        System.out.print("Ingresa el número de la operación deseada: ");
        int opcion = scanner.nextInt();

        double resultado = 0;

        switch (opcion) {
            case 1:
                resultado = numero1 + numero2;
                System.out.println("Resultado de la suma: " + resultado);
                break;
            case 2:
                resultado = numero1 - numero2;
                System.out.println("Resultado de la resta: " + resultado);
                break;
            case 3:
                resultado = numero1 * numero2;
                System.out.println("Resultado de la multiplicación: " + resultado);
                break;
            case 4:
                if (numero2 != 0) {
                    resultado = numero1 / numero2;
                    System.out.println("Resultado de la división: " + resultado);
                }
                else {
                    System.out.println("Error: No se puede dividir por cero.");
                }
                break;
            default:
                System.out.println("Operación no válida.");
                break;
        }

        scanner.close();
    }
}
