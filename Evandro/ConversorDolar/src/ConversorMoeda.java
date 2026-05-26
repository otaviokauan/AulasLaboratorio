import java.util.Scanner;

public class ConversorMoeda {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite a cotação do dólar hoje (ex: 5,00):");
        double cotacaoDolar = leitor.nextDouble();

        System.out.println("Digite a quantidade de dólares que você possui:");
        double quantidadeDolares = leitor.nextDouble();

        double valorReal = quantidadeDolares * cotacaoDolar;

        System.out.println("Resultado da Conversão");
        System.out.println("O valor equivalente em Reais é: R$ " + valorReal);

        leitor.close();
    }
}