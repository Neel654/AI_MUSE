import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import * as Speech from 'expo-speech';

export default function App() {
  const [input, setInput] = useState('');
  const [reply, setReply] = useState('');

  const sendToMuse = async () => {
    const res = await fetch('http://192.168.2.101:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setReply(data.reply);
    Speech.speak(data.reply);
  };

  return (
    <View style={{ padding: 50 }}>
      <TextInput
        value={input}
        onChangeText={setInput}
        placeholder="Speak to Muse…"
        style={{ marginBottom: 20, fontSize: 18, borderWidth: 1, padding:8 }}
      />
      <Button title="Send" onPress={sendToMuse} />
      <Text style={{ marginTop: 30, fontSize: 20 }}>{reply}</Text>
    </View>
  );
}
