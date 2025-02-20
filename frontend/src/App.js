import './App.css';
import { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [key, setKey] = useState(0);
  const [encryptedText, setEncryptedText] = useState('');
  const [decryptedText, setDecryptedText] = useState('');

  const handleEncrypt = async () => {
    try {
      const response = await fetch('http://localhost:8000/encrypt/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, key }),
      });
      const data = await response.json();
      setEncryptedText(data.encrypted_text);
    } catch (error) {
      console.error('Error encrypting:', error);
    }
  };

  const handleDecrypt = async () => {
    try {
      const response = await fetch('http://localhost:8000/decrypt/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ encrypted_text: encryptedText, key }),
      });
      const data = await response.json();
      setDecryptedText(data.decrypted_text);
    } catch (error) {
      console.error('Error decrypting:', error);
    }
  };

  return (
    <div className="App" style={{ backgroundColor: 'white' }}>
      <header className="App-header">
        <h1>Encryption and Decryption Tool</h1>
        <input
          type="text"
          placeholder="Enter text to encrypt/decrypt"
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="input-field"
        />
        <input
          type="number"
          placeholder="Enter encryption key (integer)"
          value={key}
          onChange={(e) => setKey(Number(e.target.value))}
          className="input-field"
        />
        <button onClick={handleEncrypt} className="action-button">Encrypt</button>
        <button onClick={handleDecrypt} className="action-button">Decrypt</button>
        {encryptedText && <p>Encrypted Text: {encryptedText}</p>}
        {decryptedText && <p>Decrypted Text: {decryptedText}</p>}
      </header>
    </div>
  );
}

export default App;
