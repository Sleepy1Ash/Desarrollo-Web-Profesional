package edu.utvt.clase2;

public class elseIfStatement {
    public static void main(String[] args) {

        int age = 50;

        if (age < 12)
            System.out.println("Eres un niño");
        else if (age < 17)
            System.out.println("Eres un adolescente");
        else if (age < 35)
            System.out.println("Eres un adulto joven");
        else
            System.out.println("Eres un adulto");

    }
}
