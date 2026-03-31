# Dynamic Model Tabs Implementation

## Overview

This implementation creates dynamic tabs for Git Diff and Push Changes that adjust based on the number of selected models.

## Features

### 1. Dynamic Tab Generation
- **No Models Selected**: Shows 2 default tabs
  - Git Diff (generic)
  - Push Changes (generic)

- **Models Selected**: Shows tabs for each model
  - Git Diff - Model 1
  - Git Diff - Model 2
  - ...
  - Push Changes - Model 1
  - Push Changes - Model 2
  - ...

### 2. Component Structure

#### `ModelTabs.tsx`
Main component that:
- Accepts `selectedModels` as props
- Dynamically generates tabs based on selected models
- Manages active tab state
- Renders appropriate content for each tab type

#### `App.tsx`
Demo application that:
- Provides model selection interface
- Passes selected models to `ModelTabs` component
- Demonstrates the dynamic tab behavior

## How It Works

### Tab Generation Logic

```typescript
const generateTabs = () => {
  const tabs = [];

  if (selectedModels.length > 0) {
    // Create Git Diff tabs for each model
    selectedModels.forEach((model) => {
      tabs.push({
        id: `git-diff-${model.id}`,
        label: `Git Diff - ${model.name}`,
        type: 'git-diff',
        modelId: model.id
      });
    });

    // Create Push Changes tabs for each model
    selectedModels.forEach((model) => {
      tabs.push({
        id: `push-changes-${model.id}`,
        label: `Push Changes - ${model.name}`,
        type: 'push-changes',
        modelId: model.id
      });
    });
  } else {
    // Default tabs
    // ...
  }

  return tabs;
};
```

### Key Behaviors

1. **When 0 models selected**:
   - Shows 2 tabs (Git Diff, Push Changes)
   - Content indicates models need to be selected

2. **When 1 model selected**:
   - Shows 2 tabs (Git Diff - Model, Push Changes - Model)
   - Each tab shows model-specific content

3. **When multiple models selected**:
   - Shows N × 2 tabs (where N = number of models)
   - All Git Diff tabs appear first, then all Push Changes tabs
   - Each tab is model-specific

## Usage Example

```tsx
import React, { useState } from 'react';
import ModelTabs from './ModelTabs';

const MyApp = () => {
  const [selectedModels, setSelectedModels] = useState([
    { id: 'gpt-4', name: 'GPT-4' },
    { id: 'claude', name: 'Claude' }
  ]);

  return <ModelTabs selectedModels={selectedModels} />;
};
```

## Customization

### Adding Model-Specific Git Diff

Replace the placeholder in `renderTabContent`:

```typescript
if (activeTabData.type === 'git-diff') {
  return (
    <div className="tab-content git-diff-content">
      <GitDiffViewer modelId={activeTabData.modelId} />
    </div>
  );
}
```

### Adding Model-Specific Push Changes

Replace the placeholder in `renderTabContent`:

```typescript
if (activeTabData.type === 'push-changes') {
  return (
    <div className="tab-content push-changes-content">
      <PushChangesForm
        modelId={activeTabData.modelId}
        onPush={handlePush}
      />
    </div>
  );
}
```

## Styling

The component uses CSS for styling with support for:
- Responsive design (mobile-friendly)
- Active tab highlighting
- Smooth transitions
- Scrollable tab headers when many models are selected

## Integration Points

To integrate this into your existing application:

1. **Import the component**:
   ```tsx
   import ModelTabs from './ModelTabs';
   import './ModelTabs.css';
   ```

2. **Pass selected models**:
   ```tsx
   <ModelTabs selectedModels={yourSelectedModels} />
   ```

3. **Customize content renderers**:
   - Modify `renderTabContent()` to show your actual git diff and push changes UI
   - Connect to your git operations backend
   - Add loading states, error handling, etc.

## Benefits

- **Scalable**: Works with any number of models
- **User-friendly**: Clear organization of model-specific operations
- **Responsive**: Adapts to different screen sizes
- **Maintainable**: Clean separation of concerns

## Future Enhancements

Potential improvements:
1. Add tab grouping (collapse/expand)
2. Add search/filter for tabs when many models selected
3. Add keyboard navigation between tabs
4. Add tab close buttons
5. Persist tab selection in localStorage
6. Add drag-and-drop to reorder tabs
