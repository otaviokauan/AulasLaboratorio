import java.util.Scanner;

public class RendimentoPoupanca {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o valor depositado:");
        double valorDeposito = leitor.nextDouble();

        double rendimento = valorDeposito * 0.0007;
        double valorFinal = valorDeposito + rendimento;

        System.out.println("Resultado após 1 mês");
        System.out.println("Rendimento do mês: R$ " + rendimento);
        System.out.println("Valor total com juros: R$ " + valorFinal);

        leitor.close();
    }
}