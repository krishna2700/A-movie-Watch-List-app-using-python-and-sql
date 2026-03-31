import React, { useState } from 'react';

interface Model {
  id: string;
  name: string;
}

interface ModelTabsProps {
  selectedModels: Model[];
}

const ModelTabs: React.FC<ModelTabsProps> = ({ selectedModels }) => {
  const [activeTab, setActiveTab] = useState<string>('git-diff');

  // Generate tabs based on selected models
  const generateTabs = () => {
    const tabs = [];

    // If models are selected, create tabs for each model
    if (selectedModels.length > 0) {
      selectedModels.forEach((model, index) => {
        tabs.push({
          id: `git-diff-${model.id}`,
          label: `Git Diff - ${model.name}`,
          type: 'git-diff',
          modelId: model.id
        });
      });

      selectedModels.forEach((model, index) => {
        tabs.push({
          id: `push-changes-${model.id}`,
          label: `Push Changes - ${model.name}`,
          type: 'push-changes',
          modelId: model.id
        });
      });
    } else {
      // Default tabs when no models are selected
      tabs.push({
        id: 'git-diff',
        label: 'Git Diff',
        type: 'git-diff',
        modelId: null
      });

      tabs.push({
        id: 'push-changes',
        label: 'Push Changes',
        type: 'push-changes',
        modelId: null
      });
    }

    return tabs;
  };

  const tabs = generateTabs();

  // Render tab content based on active tab
  const renderTabContent = () => {
    const activeTabData = tabs.find(tab => tab.id === activeTab);

    if (!activeTabData) return null;

    if (activeTabData.type === 'git-diff') {
      return (
        <div className="tab-content git-diff-content">
          <h3>Git Diff {activeTabData.modelId ? `- ${activeTabData.modelId}` : ''}</h3>
          <div className="diff-container">
            {/* Git diff content for the specific model */}
            <pre>
              {activeTabData.modelId
                ? `Showing git diff for model: ${activeTabData.modelId}`
                : 'Select models to see model-specific git diffs'
              }
            </pre>
          </div>
        </div>
      );
    }

    if (activeTabData.type === 'push-changes') {
      return (
        <div className="tab-content push-changes-content">
          <h3>Push Changes {activeTabData.modelId ? `- ${activeTabData.modelId}` : ''}</h3>
          <div className="push-container">
            {/* Push changes content for the specific model */}
            <div>
              {activeTabData.modelId
                ? `Push changes for model: ${activeTabData.modelId}`
                : 'Select models to enable model-specific push changes'
              }
            </div>
            <button
              className="push-button"
              disabled={!activeTabData.modelId}
            >
              Push Changes
            </button>
          </div>
        </div>
      );
    }

    return null;
  };

  return (
    <div className="model-tabs-container">
      {/* Tab Headers */}
      <div className="tab-headers">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab-header ${activeTab === tab.id ? 'active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="tab-content-container">
        {renderTabContent()}
      </div>

      {/* Model Count Info */}
      <div className="model-info">
        {selectedModels.length > 0
          ? `${selectedModels.length} model${selectedModels.length > 1 ? 's' : ''} selected`
          : 'No models selected'
        }
      </div>
    </div>
  );
};

export default ModelTabs;
