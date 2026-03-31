# Dynamic Model Tabs - Git Diff & Push Changes

A React/TypeScript component that dynamically generates tabs for Git Diff and Push Changes based on the number of selected models.

## 📋 Overview

This implementation creates a dynamic tab system where:
- **Tabs are generated automatically** based on selected models
- **Each model gets its own Git Diff tab** for viewing changes
- **Each model gets its own Push Changes tab** for pushing updates
- **Tab count scales dynamically** - select 3 models, get 6 tabs (3 Git Diff + 3 Push Changes)

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Open http://localhost:5173
```

## 📸 How It Works

### No Models Selected
```
┌─────────────┬──────────────────┐
│  Git Diff   │  Push Changes    │
└─────────────┴──────────────────┘
```

### 1 Model Selected (GPT-4)
```
┌──────────────────┬────────────────────────┐
│ Git Diff - GPT-4 │ Push Changes - GPT-4   │
└──────────────────┴────────────────────────┘
```

### 3 Models Selected (GPT-4, Claude, Gemini)
```
┌──────────────────┬────────────────────┬─────────────────────┬────────────────────────┬──────────────────────┬──────────────────────────┐
│ Git Diff - GPT-4 │ Git Diff - Claude  │ Git Diff - Gemini   │ Push Changes - GPT-4   │ Push Changes - Claude│ Push Changes - Gemini    │
└──────────────────┴────────────────────┴─────────────────────┴────────────────────────┴──────────────────────┴──────────────────────────┘
```

## 📁 Project Structure

```
.
├── App.tsx                 # Main demo application
├── App.css                 # Demo app styling
├── ModelTabs.tsx           # Dynamic tabs component ⭐
├── ModelTabs.css           # Tabs styling
├── main.tsx                # React entry point
├── index.html              # HTML template
├── vite.config.ts          # Vite configuration
├── tsconfig.json           # TypeScript config
├── package.json            # Dependencies
├── IMPLEMENTATION.md       # Detailed implementation guide
├── SUMMARY.md              # Technical summary
└── QUICK_START.md          # Quick start guide
```

## 🎯 Key Features

- ✅ **Dynamic Tab Generation** - Tabs created based on selected models array
- ✅ **Model-Specific Operations** - Each model has dedicated Git Diff and Push Changes tabs
- ✅ **Responsive Design** - Works on mobile and desktop
- ✅ **Active State Management** - Tracks currently active tab
- ✅ **Scalable** - Works with any number of models
- ✅ **TypeScript** - Fully typed for type safety
- ✅ **Clean Code** - Well-structured and maintainable

## 💻 Usage

### Basic Usage

```tsx
import ModelTabs from './ModelTabs';
import './ModelTabs.css';

const selectedModels = [
  { id: 'gpt-4', name: 'GPT-4' },
  { id: 'claude', name: 'Claude' }
];

function App() {
  return <ModelTabs selectedModels={selectedModels} />;
}
```

### With Model Selection

```tsx
import { useState } from 'react';
import ModelTabs from './ModelTabs';

function App() {
  const [selectedModels, setSelectedModels] = useState([]);

  const handleModelToggle = (model) => {
    setSelectedModels(prev =>
      prev.some(m => m.id === model.id)
        ? prev.filter(m => m.id !== model.id)
        : [...prev, model]
    );
  };

  return (
    <>
      {/* Model selection UI */}
      <ModelTabs selectedModels={selectedModels} />
    </>
  );
}
```

## 🔧 Customization

### Replace Git Diff Content

In `ModelTabs.tsx`, update the `renderTabContent()` function:

```typescript
if (activeTabData.type === 'git-diff') {
  return <YourGitDiffComponent modelId={activeTabData.modelId} />;
}
```

### Replace Push Changes Content

```typescript
if (activeTabData.type === 'push-changes') {
  return <YourPushComponent modelId={activeTabData.modelId} />;
}
```

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started quickly
- **[IMPLEMENTATION.md](IMPLEMENTATION.md)** - Detailed implementation guide
- **[SUMMARY.md](SUMMARY.md)** - Technical summary and architecture

## 🛠️ Tech Stack

- **React 18** - UI framework
- **TypeScript 5** - Type safety
- **Vite 4** - Build tool and dev server
- **CSS3** - Styling with responsive design

## 📦 Installation

```bash
# Clone or download the project
cd dynamic-model-tabs

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🧪 Testing Scenarios

1. **Zero models**: Verify default tabs appear
2. **Single model**: Verify 2 model-specific tabs
3. **Multiple models**: Verify all tabs generate correctly
4. **Tab switching**: Verify active state updates properly
5. **Responsive**: Test on mobile and desktop viewports

## 🎨 Styling

The component uses clean, modern CSS with:
- Responsive design (mobile-first)
- Smooth transitions
- Active state highlighting
- Horizontal scrolling for many tabs
- Professional color scheme

Customize colors in `ModelTabs.css`:
```css
.tab-header.active {
  background-color: #007bff; /* Change this */
  color: white;
}
```

## 🚧 Future Enhancements

- [ ] Tab grouping/collapse
- [ ] Search/filter for many tabs
- [ ] Keyboard navigation (arrow keys)
- [ ] Drag-and-drop tab reordering
- [ ] Tab close buttons
- [ ] localStorage persistence
- [ ] Animations and transitions
- [ ] Split-view mode

## 🤝 Contributing

This is a demonstration project. Feel free to use and modify as needed.

## 📄 License

MIT License - Use freely

## 🙋 Support

For detailed documentation, see:
- [Implementation Guide](IMPLEMENTATION.md)
- [Quick Start](QUICK_START.md)
- [Technical Summary](SUMMARY.md)

---

Built with ❤️ using React + TypeScript + Vite
