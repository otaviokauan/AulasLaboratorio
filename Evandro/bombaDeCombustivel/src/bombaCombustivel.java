public class bombaCombustivel {
    private  String tipoCombustivel;
    private double valorLitro;
    private double quantidadeCombustivel;

    public bombaCombustivel(String tipoCombustivel, double valorLitro, double quantidadeCombustivel){
        this.tipoCombustivel  = tipoCombustivel;
        this.valorLitro  = valorLitro;
        this.quantidadeCombustivel  = quantidadeCombustivel;
    }

    public void abastecerPorValor (double valor){
        double litrosParaAbastecer = valor / valorLitro;

        if (litrosParaAbastecer <= quantidadeCombustivel){
            quantidadeCombustivel -= litrosParaAbastecer;
            System.out.println("abastecido" + litrosParaAbastecer);
        }else {
            System.out.println("erro: não a combustivel sufuciente na bomba");
        }
    }
    public void abastecerPorLitro (double litro){
        if(litro <= quantidadeCombustivel){
            double valorParaPagar = litro *valorLitro;
            quantidadeCombustivel -= litro;
            System.out.println("valor a pagar é" + valorParaPagar);
        } else {
            System.out.println("erro: não a combustivel suficiente na bomba");
        }
    }
    public void alterarValor(double novoValor) {
        this.valorLitro = novoValor;
        System.out.println("valor do litro atualizado para "+novoValor+" R$");
    }
    public void alterarCombstivel(String novoCombustivel){
        this.tipoCombustivel = novoCombustivel;
        System.out.println("tipo de combustivel alterado para "+ novoCombustivel);
    }
    public void alterarQuantidadeCombustivel(double novaQuantidade){
        this.quantidadeCombustivel = novaQuantidade;
        System.out.println("quantidade da bomba atualizada para: "+ novaQuantidade +" litros");
    }
    public void exibirStatus(){
        System.out.println("-----------------------");
        System.out.println("combustivel " + tipoCombustivel);
        System.out.println("valor/litro " + valorLitro + "R$");
        System.out.println("quantidade da bomba: " + quantidadeCombustivel + " L");
        System.out.println("-----------------------");
    }
}

