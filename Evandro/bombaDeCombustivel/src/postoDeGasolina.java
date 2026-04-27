public class postoDeGasolina {
    static void main(String[] args) {
        bombaCombustivel bomba = new bombaCombustivel ("gasolina", 5.50, 1000.0);
        System.out.println("Status Inicial");
        bomba.exibirStatus();

        System.out.println("ação: Abastecer R$110,0");
        bomba.abastecerPorValor(110.0);

        System.out.println("\nAção: abastecer 20 litros");
        bomba.abastecerPorLitro(20.0);

        System.out.println("\n Atualizando bomba");
        bomba.alterarCombstivel("etanol");
        bomba.alterarValor(3.89);
        bomba.alterarQuantidadeCombustivel(500.00);

        System.out.println("Status Final");
        bomba.exibirStatus();
    }
}
