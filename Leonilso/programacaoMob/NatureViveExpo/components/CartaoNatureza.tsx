import React, { useState } from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet, Dimensions } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const { width } = Dimensions.get('window');

interface CartaoNaturezaProps {
  titulo: string;
  paragrafo: string;
  imagemSrc: string;
  imagemAlt: string;
  badge?: string;
}

export function CartaoNatureza({
  titulo,
  paragrafo,
  imagemSrc,
  imagemAlt,
  badge = "Destaque",
}: CartaoNaturezaProps) {
  const [isPressed, setIsPressed] = useState(false);

  return (
    <TouchableOpacity
      style={[styles.container, isPressed && styles.pressed]}
      onPressIn={() => setIsPressed(true)}
      onPressOut={() => setIsPressed(false)}
      activeOpacity={0.9}
    >
      {/* Container da imagem */}
      <View style={styles.imageContainer}>
        <Image
          source={{ uri: imagemSrc }}
          style={styles.image}
          accessibilityLabel={imagemAlt}
        />

        {/* Overlay com gradiente */}
        <LinearGradient
          colors={['rgba(230, 81, 0, 0)', 'rgba(230, 81, 0, 0.3)', 'rgba(230, 81, 0, 0.6)']}
          style={[styles.overlay, { opacity: isPressed ? 0.8 : 0.5 }]}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 1 }}
        />

        {/* Badge */}
        <View style={[styles.badge, isPressed && styles.badgePressed]}>
          <Text style={styles.badgeText}>{badge}</Text>
        </View>
      </View>

      {/* Conteúdo */}
      <LinearGradient
        colors={['#FFFFFF', '#FAFCFB']}
        style={styles.content}
        start={{ x: 0, y: 0 }}
        end={{ x: 0, y: 1 }}
      >
        {/* Linha decorativa */}
        <View style={[styles.decorativeLine, { width: isPressed ? 60 : 40 }]} />

        {/* Título */}
        <Text style={[styles.title, isPressed && styles.titlePressed]}>
          {titulo}
        </Text>

        {/* Parágrafo */}
        <Text style={styles.paragraph}>
          {paragrafo}
        </Text>

        {/* Botão */}
        <TouchableOpacity style={[styles.button, isPressed && styles.buttonPressed]}>
          <Text style={styles.buttonText}>Explorar Agora →</Text>
        </TouchableOpacity>
      </LinearGradient>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#f8f9fa',
    borderRadius: 16,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 5,
    maxWidth: 420,
    width: width * 0.9,
    margin: 10,
    borderWidth: 1,
    borderColor: 'rgba(149, 213, 178, 0.1)',
  },
  pressed: {
    transform: [{ translateY: -8 }],
  },
  imageContainer: {
    position: 'relative',
    width: '100%',
    height: 280,
    backgroundColor: '#e9ecef',
  },
  image: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
  overlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
  },
  badge: {
    position: 'absolute',
    top: 16,
    left: 16,
    backgroundColor: '#FF6D00',
    paddingHorizontal: 14,
    paddingVertical: 7,
    borderRadius: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 3,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.15)',
  },
  badgePressed: {
    transform: [{ translateY: -4 }, { scale: 1.05 }],
  },
  badgeText: {
    color: '#FFFFFF',
    fontSize: 11,
    fontWeight: '700',
    letterSpacing: 1,
    textTransform: 'uppercase',
  },
  content: {
    padding: 28,
  },
  decorativeLine: {
    height: 4,
    backgroundColor: '#1976D2',
    borderRadius: 2,
    marginBottom: 16,
    shadowColor: '#1976D2',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.3,
    shadowRadius: 2,
    elevation: 2,
  },
  title: {
    fontSize: 24,
    fontWeight: '800',
    color: '#E65100',
    lineHeight: 30,
    marginBottom: 14,
    letterSpacing: -0.5,
  },
  titlePressed: {
    color: '#BF360C',
  },
  paragraph: {
    fontSize: 15,
    color: '#666',
    lineHeight: 25.5,
    marginBottom: 26,
    fontWeight: '400',
    letterSpacing: 0.2,
  },
  button: {
    width: '100%',
    padding: 14,
    backgroundColor: '#FF6D00',
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 4,
    elevation: 3,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
  },
  buttonPressed: {
    backgroundColor: '#E65100',
    transform: [{ translateY: -2 }],
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
    letterSpacing: 0.5,
    textTransform: 'uppercase',
  },
});