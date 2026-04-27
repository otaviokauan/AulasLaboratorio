import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double saldo = 1000.00;
        int opcao = 0;

        System.out.println("Bem-vindo ao Banco Java!");

        do {
            System.out.println("\n--- MENU DO CAIXA ---");
            System.out.println("[1] Consultar Saldo");
            System.out.println("[2] Realizar Depósito");
            System.out.println("[3] Realizar Saque");
            System.out.println("[4] Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.printf("Seu saldo atual é: R$ %.2f\n", saldo);
                    break;
                case 2:
                    System.out.print("Digite o valor para depósito: R$ ");
                    double valorDeposito = scanner.nextDouble();
                    if (valorDeposito > 0) {
                        saldo += valorDeposito;
                        System.out.println("Depósito realizado com sucesso!");
                    } else {
                        System.out.println("Valor de depósito inválido.");
                    }
                    break;
                case 3:
                    System.out.print("Digite o valor para saque: R$ ");
                    double valorSaque = scanner.nextDouble();
                    if (valorSaque > 0 && valorSaque <= saldo) {
                        saldo -= valorSaque;
                        System.out.println("Saque realizado com sucesso!");
                    } else if (valorSaque > saldo) {
                        System.out.println("Saldo insuficiente.");
                    } else {
                        System.out.println("Valor de saque inválido.");
                    }
                    break;
                case 4:
                    System.out.println("Obrigado por usar o Banco Java. Até logo!");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while (opcao != 4);

        scanner.close();
    }
}