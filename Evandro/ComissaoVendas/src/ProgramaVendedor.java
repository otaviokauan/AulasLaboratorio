import java.util.Scanner;

public class ProgramaVendedor {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o nome:");
        String nome = leitor.nextLine();

        System.out.println("Digite o salario fixo:");
        double salarioFixo = leitor.nextDouble();

        System.out.println("Digite o total de vendas:");
        double totalVendas = leitor.nextDouble();

        double comissao = totalVendas * 0.15;
        double salarioFinal = salarioFixo + comissao;

        System.out.println("Vendedor: " + nome);
        System.out.println("Salario Fixo: " + salarioFixo);
        System.out.println("Salario Final: " + salarioFinal);
        
        leitor.close();
    }
}