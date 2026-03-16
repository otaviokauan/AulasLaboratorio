// AQUI VOCÊ DEVE COLAR AS CREDENCIAIS DO SEU PROJETO FIREBASE
// Para obter, vá no seu console do Firebase -> Configurações do Projeto -> Seção "Configurações gerais"
const firebaseConfig = {
  apiKey: "AIzaSyD6Mq43dpbgFkQXUDuWMDRAM2FvepxIpZI",
  authDomain: "hotel-e5548.firebaseapp.com",
  projectId: "hotel-e5548",
  storageBucket: "hotel-e5548.firebasestorage.app",
  messagingSenderId: "541560082134",
  appId: "1:541560082134:web:2e1da75406f738ef9f8377"
};

// Inicialize o Firebase
firebase.initializeApp(firebaseConfig);

// Obtenha uma referência para o serviço Firestore
const db = firebase.firestore();
const hospedesRef = db.collection('hospedes');

// Obtenha as referências dos elementos HTML
const hospedeForm = document.getElementById('hospede-form');
const hospedeList = document.getElementById('hospede-list');

// Função para adicionar um novo hóspede
hospedeForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nome = document.getElementById('nome').value;
    const quarto = document.getElementById('quarto').value;
    const data = document.getElementById('data').value;

    try {
        await hospedesRef.add({
            nome: nome,
            quarto: quarto,
            dataEntrada: data,
            timestamp: firebase.firestore.FieldValue.serverTimestamp() // Salva a data e hora do registro
        });

        alert('Hóspede adicionado com sucesso!');
        hospedeForm.reset();
    } catch (error) {
        console.error("Erro ao adicionar hóspede: ", error);
        alert('Ocorreu um erro. Verifique o console para mais detalhes.');
    }
});

// Função para carregar e exibir os hóspedes
const loadHospedes = () => {
    // Carrega os dados em tempo real (onSnapshot)
    hospedesRef.orderBy('timestamp', 'desc').onSnapshot((snapshot) => {
        hospedeList.innerHTML = ''; // Limpa a lista antes de adicionar os novos dados
        snapshot.forEach((doc) => {
            const hospede = doc.data();
            const row = document.createElement('tr');
            
            row.innerHTML = `
                <td>${hospede.nome}</td>
                <td>${hospede.quarto}</td>
                <td>${hospede.dataEntrada}</td>
            `;
            hospedeList.appendChild(row);
        });
    }, (error) => {
        console.error("Erro ao carregar os dados: ", error);
    });
};

// Chama a função para carregar os hóspedes quando a página é carregada
window.addEventListener('load', loadHospedes);