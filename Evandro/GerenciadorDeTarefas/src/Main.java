import java.util.Scanner;
import java.util.ArrayList;

public class Main {

    static ArrayList<String> tarefas = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int opcao = -1;

        System.out.println("Bem vindo ao nosso aplicativo!");

        while (opcao != 0){
            exibirMenu();
            opcao = scanner.nextInt();
            scanner.nextLine();

            processarOpcao(opcao);
        }

        System.out.println("Aplicativo encerado");

    }

    static void exibirMenu(){
        System.out.println("\ndigite 1 para adicionar tarefa");
        System.out.println("digite 2 para listar tarefas");
        System.out.println("digite 3 para remover tarefa");
        System.out.println("digite 0 para fechar o sistema");
        System.out.println("escolha a opção");
    }

    static void processarOpcao(int opcao) {
        switch (opcao){
            case 1:
                adicionarTarefa();
                break;
            case 2:
                listarTarefa();
                break;
            case 3:
                removerTarefa();
                break;
            case 0:
                break;

            default:
                System.out.println("opção invalida");

        }
    }

    static void adicionarTarefa(){
        System.out.println("digite o nome da tarefa");
        String tarefa = scanner.nextLine();
        tarefas.add(tarefa);
        System.out.println("a tarefa " + tarefa + "foi adicionada com sucesso!");
    }

    static void listarTarefa() {
        System.out.println("\n Suas tarefas");
        if (tarefas.isEmpty()){
            System.out.println("nenhuma tarefa cadastrada");
        } else {
            for (int i = 0;  i < tarefas.size(); i++ ){
                System.out.println((i+1)+ "." + tarefas.get(i));
            }
        }

    }

    static void removerTarefa(){
        listarTarefa();
        if (!tarefas.isEmpty()){
            System.out.println("digite número tarefa que quer remover: ");
            int index = scanner.nextInt();
            scanner.nextLine();
            if(index > 0 && index <= tarefas.size()){
                tarefas.remove(index -1);
                System.out.println("tarefa removida");
            } else{
                System.out.println("numero inválido");
            }
        }

    }

}