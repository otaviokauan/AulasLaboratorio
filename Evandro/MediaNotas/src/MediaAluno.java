import java.util.Scanner;

public class MediaAluno {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o nome do aluno:");
        String nome = leitor.nextLine();

        System.out.println("Digite a nota da primeira prova:");
        double nota1 = leitor.nextDouble();

        System.out.println("Digite a nota da segunda prova:");
        double nota2 = leitor.nextDouble();

        System.out.println("Digite a nota da terceira prova:");
        double nota3 = leitor.nextDouble();

        double media = (nota1 + nota2 + nota3) / 3;

        System.out.println("Aluno: " + nome);
        System.out.println("Media Final: " + media);

        leitor.close();
    }
}