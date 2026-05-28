# 🎵 MUSE - Unified AI Project

**MUSE** is an integrated AI conversation system combining a powerful Python backend with a cross-platform mobile frontend. Experience intelligent interactions anywhere, anytime.

## 📋 Project Structure

MUSE is organized as a monorepo with two key components:

```
AI_MUSE/
├── backend/          # AI backend (Python)
│   ├── AI logic
│   ├── API endpoints
│   └── Model management
│
└── mobile/          # Mobile frontend (React Native/Expo)
    ├── iOS
    ├── Android
    └── Web support
```

## 🚀 Quick Start

### Option A: Backend Only (Python)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The AI backend will start on `http://localhost:8000`

**Available Endpoints:**
- `POST /ask` - Send a message to the AI and get a response

### Option B: Mobile Frontend (React Native)

```bash
cd mobile
npm install
npx expo start
```

Then choose your platform:
- **iOS Simulator:** Press `i`
- **Android Emulator:** Press `a`
- **Expo Go:** Scan QR code with Expo Go app
- **Web:** Press `w`

### Option C: Full Stack (Both)

1. Start the backend (see Option A)
2. Update the API endpoint in `mobile/App.js` if needed
3. Start the mobile app (see Option B)

## 🏗️ Architecture

### Backend (AI_MUSE Python)

- **Framework:** [Your AI framework]
- **Language:** Python 3.x
- **Purpose:** Core AI logic and API endpoints
- **API:** RESTful endpoints for mobile client

**Key Features:**
- Natural language processing
- AI response generation
- Speech synthesis support
- Cross-origin request handling

### Frontend (MuseMobile React Native)

- **Framework:** Expo & React Native
- **Language:** TypeScript/JavaScript
- **Target Platforms:** iOS, Android, Web
- **Purpose:** User-friendly interface for AI interaction

**Key Features:**
- Text input for messages
- Real-time AI responses
- Text-to-speech capabilities
- Cross-platform support
- Navigation and UI components

## 🔌 API Integration

The mobile frontend communicates with the backend via HTTP requests:

```javascript
// Example: Sending a message to the backend
const response = await fetch('http://backend-url:8000/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: userInput }),
});

const data = await response.json();
// Use data.reply in your UI
```

## 📦 Dependencies

### Backend

See `requirements.txt` in the backend directory for Python dependencies.

### Frontend

**Key packages:**
- `react-native` - Cross-platform mobile framework
- `expo` - Development platform and SDK
- `expo-router` - File-based routing
- `expo-speech` - Text-to-speech
- `react-native-voice` - Speech-to-text
- `@react-navigation/*` - Navigation stack

See `mobile/package.json` for complete list.

## 🎯 Development Workflow

### Backend Development

```bash
cd backend
# Make changes to Python code
# Restart the server to see changes
```

### Frontend Development

```bash
cd mobile
npm run lint      # Check code quality
npx expo start    # Hot reload enabled
```

## 🧪 Testing

### Backend
```bash
cd backend
# Add your test commands here
```

### Frontend
```bash
cd mobile
npm test
```

## 📱 Platform-Specific Setup

### iOS (macOS only)
```bash
cd mobile
npx expo prebuild --platform ios
npx expo run:ios
```

### Android
```bash
cd mobile
npx expo prebuild --platform android
npx expo run:android
```

## 🔧 Configuration

### Backend Configuration
- Update API endpoints and settings in the backend configuration files
- Configure CORS for mobile app access

### Frontend Configuration
- Update backend URL in `mobile/App.js` (line 10)
- Configure app metadata in `mobile/app.json`

## 📚 Resources

### Backend Docs
- [AI Framework Documentation]
- [REST API Reference]

### Frontend Docs
- [Expo Documentation](https://docs.expo.dev/)
- [React Native Guide](https://reactnative.dev/)
- [Expo Router Guide](https://docs.expo.dev/router/introduction/)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes (backend and/or frontend)
3. Test both components together
4. Submit a pull request

## 📝 Project Status

- ✅ Backend AI logic
- ✅ REST API endpoints
- ✅ Mobile UI foundation
- ✅ Text-to-speech integration
- 🚧 Voice-to-text integration
- 🚧 Enhanced UI/UX
- 🚧 Production deployment

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ You can use this code for personal, educational, and commercial projects
- ✅ You can modify and distribute the code
- 📝 You must include the license notice and copyright attribution
- ⚠️ The code is provided "as-is" without warranty

**Copyright © 2025 Neel654. All rights reserved.**

## 👨‍💻 Author

**Neel654** - Full Stack MUSE Developer

---

## 🎵 Why MUSE?

MUSE stands for **Multi-User Smart Engine** - a unified AI conversation platform that brings together intelligent backend logic with beautiful, intuitive mobile interfaces.

**Together, the backend and frontend create a seamless AI experience.**
