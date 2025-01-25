package edu.utvt.clase2;

import java.util.Scanner;

public class forLoop {
    public static void main(String[] args) {
        int loops = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingresa el número de ciclos requeridos: ");
        loops = sc.nextInt();

        for (int count = 1; count <= loops; count++) {
            System.out.println("Número actual de iteración: " + count);
        }
    }
}
