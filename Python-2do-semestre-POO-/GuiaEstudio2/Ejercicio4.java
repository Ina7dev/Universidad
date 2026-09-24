package GuiaEstudio2;
import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);


        System.out.print("Ingresa la edad de la persona: ");
        int edad = scanner.nextInt();


        int precioEntrada;


        if (edad < 12) {
            precioEntrada = 2000;
            System.out.println("Categoría: Niños");
        }
        else if (edad >= 12 && edad <= 17) {
            precioEntrada = 3500;
            System.out.println("Categoría: Adolescentes");
        }
        else {
            precioEntrada = 5000;
            System.out.println("Categoría: Adultos");
        }

        System.out.println("El precio de la entrada es: $" + precioEntrada);

        scanner.close();
    }
}
