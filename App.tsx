import React, { useState } from 'react';
import ModelTabs from './ModelTabs';
import './ModelTabs.css';

interface Model {
  id: string;
  name: string;
}

const App: React.FC = () => {
  // Available models to select from
  const availableModels: Model[] = [
    { id: 'model-1', name: 'GPT-4' },
    { id: 'model-2', name: 'Claude' },
    { id: 'model-3', name: 'Gemini' },
    { id: 'model-4', name: 'LLaMA' },
  ];

  const [selectedModels, setSelectedModels] = useState<Model[]>([]);

  const handleModelToggle = (model: Model) => {
    setSelectedModels(prev => {
      const isSelected = prev.some(m => m.id === model.id);
      if (isSelected) {
        return prev.filter(m => m.id !== model.id);
      } else {
        return [...prev, model];
      }
    });
  };

  const isModelSelected = (model: Model) => {
    return selectedModels.some(m => m.id === model.id);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Model Comparison Tool</h1>
        <p>Select models to see dynamic tabs for Git Diff and Push Changes</p>
      </header>

      <div className="model-selection">
        <h2>Select Models</h2>
        <div className="model-checkboxes">
          {availableModels.map(model => (
            <label key={model.id} className="model-checkbox">
              <input
                type="checkbox"
                checked={isModelSelected(model)}
                onChange={() => handleModelToggle(model)}
              />
              <span>{model.name}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="tabs-section">
        <ModelTabs selectedModels={selectedModels} />
      </div>
    </div>
  );
};

export default App;
