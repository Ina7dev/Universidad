package GuiaEstudio2;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner keyword = new Scanner(System.in);
        
        System.out.println("Ingrese la cantidad de dinero en pesos chileno con la que desea realizar la conversion:");
        double cantidadPesoChileno = keyword.nextInt();
        
        System.out.println("Escoja el tipo de moneda de conversion");
        
        System.out.println("1: Dólares (tipo de cambio = 0.0011)");
        System.out.println("2: Euros (tipo de cambio = 0.00095");
        System.out.println("3: Yenes (tipo de cambio = 0.15)");
        System.out.println("4: Libras Esterlinas (tipo de cambio = 0.00084)");
        System.out.println("5: Yuanes (tipo de cambio = 0.0073)");
        
        int opcion = keyword.nextInt();
        
        double conversion = 0;
        
        
        switch (opcion){
                case 1: conversion = cantidadPesoChileno * 0.0011;
                    System.out.println("La conversion de peso chileno a dolares es de " + conversion);
                    break;
                case 2: conversion = cantidadPesoChileno * 0.00095;
                System.out.println("La conversion de peso chileno a euros es de " + conversion);
                break;
                case 3: conversion = cantidadPesoChileno * 0.15;
                System.out.println("La conversion de peso chileno a yenes es de " + conversion);
                break;
                case 4: conversion = cantidadPesoChileno * 0.00084;
                System.out.println("La conversion de peso chileno a libras es de " + conversion);
                break;
                case 5: conversion = cantidadPesoChileno * 0.0073;
                System.out.println("La conversion de peso chileno a yuanes es de " + conversion);
                break;
                default:
                    System.out.println("Error: Ingrese una opcion valida");
                    break;
        }
        keyword.close();
    }
    
}