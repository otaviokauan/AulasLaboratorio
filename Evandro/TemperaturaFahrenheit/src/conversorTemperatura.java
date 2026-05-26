import java.util.Scanner;

public class conversorTemperatura {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite a temperatura em Celsius:");
        double C = leitor.nextDouble();

        double F = (9 * C + 160) / 5;


        System.out.println("A temperatura em Fahrenheit é: " + F);

        leitor.close();
    }
}