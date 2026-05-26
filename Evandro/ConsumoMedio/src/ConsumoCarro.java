import java.util.Scanner;

public class ConsumoCarro {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a distância percorrida (em km): ");
        double distancia = scanner.nextDouble();

        System.out.print("Digite o combustível gasto (em litros): ");
        double combustivelGasto = scanner.nextDouble();

        double consumoMedio = distancia / combustivelGasto;

        System.out.printf("Consumo médio: " + consumoMedio + " km/litro");

    }
}