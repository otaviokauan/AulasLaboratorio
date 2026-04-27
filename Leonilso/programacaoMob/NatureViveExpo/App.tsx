import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View, ScrollView } from 'react-native';
import { CartaoNatureza } from './components/CartaoNatureza';

const cartoes = [
  {
    titulo: "Floresta Amazônica",
    paragrafo: "A maior floresta tropical do mundo, lar de milhões de espécies e essencial para o equilíbrio climático global.",
    imagemSrc: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=400&h=280&fit=crop",
    imagemAlt: "Floresta Amazônica densa com árvores altas",
    badge: "Biodiversidade",
  },
  {
    titulo: "Recifes de Coral",
    paragrafo: "Ecossistemas marinhos vibrantes que abrigam uma diversidade incrível de vida aquática.",
    imagemSrc: "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=280&fit=crop",
    imagemAlt: "Recifes de coral coloridos sob a água",
    badge: "Marinho",
  },
  {
    titulo: "Montanhas Rochosas",
    paragrafo: "Picos majestosos que oferecem habitats únicos para fauna e flora adaptadas às altitudes elevadas.",
    imagemSrc: "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=280&fit=crop",
    imagemAlt: "Montanhas rochosas com neve no topo",
    badge: "Altitude",
  },
  {
    titulo: "Savana Africana",
    paragrafo: "Planícies vastas onde leões, elefantes e zebras coexistem em harmonia com a natureza.",
    imagemSrc: "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=400&h=280&fit=crop",
    imagemAlt: "Savana com animais selvagens",
    badge: "Fauna",
  },
];

export default function App() {
  return (
    <View style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.scrollContainer}
        showsVerticalScrollIndicator={false}
      >
        {cartoes.map((cartao, index) => (
          <CartaoNatureza
            key={index}
            titulo={cartao.titulo}
            paragrafo={cartao.paragrafo}
            imagemSrc={cartao.imagemSrc}
            imagemAlt={cartao.imagemAlt}
            badge={cartao.badge}
          />
        ))}
      </ScrollView>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFF8F0',
  },
  scrollContainer: {
    padding: 10,
    paddingBottom: 30,
  },
});
