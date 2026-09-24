package GuiaEstudio2;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el precio original del producto: ");
        double precioOriginal = scanner.nextDouble();

        System.out.print("Ingresa el porcentaje de descuento: ");
        double porcentajeDescuento = scanner.nextDouble();

        double montoDescuento = precioOriginal * (porcentajeDescuento / 100);

        double precioFinal = precioOriginal - montoDescuento;

        System.out.println("El monto del descuento es: " + montoDescuento);
        System.out.println("El precio final después del descuento es: " + precioFinal);

        if (montoDescuento > precioOriginal * 0.20) {
            System.out.println("El descuento fue mayor al 20% del precio original.");
        } else {
            System.out.println("El descuento fue menor o igual al 20% del precio original.");
        }

        scanner.close();
    }
}
