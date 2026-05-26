import java.util.Scanner;

public class TrocaValores {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o valor da variável A:");
        int a = leitor.nextInt();

        System.out.println("Digite o valor da variável B:");
        int b = leitor.nextInt();

        System.out.println("Antes da troca: A = " + a + " e B = " + b);

        int aux = a;
        a = b;       
        b = aux;     

        System.out.println("--- Valores Trocados ---");
        System.out.println("Variável A agora vale: " + a);
        System.out.println("Variável B agora vale: " + b);

        leitor.close();
    }
}