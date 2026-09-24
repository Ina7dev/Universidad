package Retos;

import java.util.Scanner;

public class Reto2 {

    public static void main(String[] args) {
        
        Scanner keyword = new Scanner(System.in);
        
        //1.- solicitar cantidad
        System.out.println("Ingrese la cantidad de animales que desea agregar: ");
        int cantidadAnimales = keyword.nextInt();
       
        //contadores
        int cuentaGratis = 0;
        int cuentaPagar = 0;
        
        //2.- Bucle
        for (int i = 0; i < cantidadAnimales; i++) {
            System.out.print("Ingrese la edad del animal " + (i + 1) + ": ");
            int edad = keyword.nextInt();
            
            //3 y 4.- edades
            System.out.print("Ingrese el estado de salud del animal " + (i + 1) + " (bueno/malo): ");
            String estadoSalud = keyword.next().toLowerCase(); // Convertimos a minúsculas para evitar problemas
            
            //4.- gratis o pago
            if (edad >= 10 && estadoSalud.equals("malo")) {
                cuentaGratis++;
            } else if (edad < 1) {
                cuentaGratis++;
            } else {
                cuentaPagar++;
            }
        }
        
        //5._ resultados
        System.out.println("\nResultados:");
        System.out.println("La cantidad de animales que recibirán revisión gratuita son: " + cuentaGratis);
        System.out.println("La cantidad denimales que deben pagar por el servicio son: " + cuentaPagar);
        
        //cierre
        keyword.close();      
        
    }
    
}
