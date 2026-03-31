# Quick Start Guide

## Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
npm install
# or
yarn install
```

### Step 2: Run the Development Server

```bash
npm run dev
# or
yarn dev
```

### Step 3: Open in Browser

Navigate to `http://localhost:5173` (or the port shown in terminal)

## What You'll See

1. **Model Selection Area**: Checkboxes for GPT-4, Claude, Gemini, and LLaMA
2. **Dynamic Tabs**: Tabs that change based on your model selection
3. **Tab Content**: Placeholder content for Git Diff and Push Changes

## Try This

### Scenario 1: No Models Selected
- **Result**: 2 default tabs (Git Diff, Push Changes)
- **Behavior**: Generic content, no model-specific operations

### Scenario 2: Select One Model (e.g., GPT-4)
- **Action**: Check the GPT-4 checkbox
- **Result**: 2 tabs (Git Diff - GPT-4, Push Changes - GPT-4)
- **Behavior**: Model-specific content and operations enabled

### Scenario 3: Select Multiple Models
- **Action**: Check GPT-4, Claude, and Gemini
- **Result**: 6 tabs
  - Git Diff - GPT-4
  - Git Diff - Claude
  - Git Diff - Gemini
  - Push Changes - GPT-4
  - Push Changes - Claude
  - Push Changes - Gemini
- **Behavior**: Each model gets its own tabs for both operations

## Key Interactions

1. **Select/Deselect Models**: Click checkboxes to add or remove models
2. **Switch Tabs**: Click on any tab to view its content
3. **View Count**: See how many models are selected at the bottom

## Next Steps

### Customize for Your Project

1. **Replace Placeholder Models**: Edit `availableModels` in `App.tsx`
   ```typescript
   const availableModels: Model[] = [
     { id: 'your-model-1', name: 'Your Model 1' },
     { id: 'your-model-2', name: 'Your Model 2' },
   ];
   ```

2. **Add Real Git Diff**: Replace the placeholder in `ModelTabs.tsx`
   ```typescript
   // In renderTabContent(), replace the git diff section with:
   <GitDiffViewer modelId={activeTabData.modelId} />
   ```

3. **Add Real Push Changes**: Replace the placeholder push button
   ```typescript
   // Add your push logic:
   const handlePush = async (modelId: string) => {
     await yourPushFunction(modelId);
   };
   ```

### Integrate with Your Backend

```typescript
// Example: Fetch git diff for a model
const fetchGitDiff = async (modelId: string) => {
  const response = await fetch(`/api/git-diff/${modelId}`);
  return await response.json();
};

// Example: Push changes for a model
const pushChanges = async (modelId: string) => {
  const response = await fetch(`/api/push-changes/${modelId}`, {
    method: 'POST'
  });
  return await response.json();
};
```

## Troubleshooting

### Port Already in Use
```bash
# Try a different port
npm run dev -- --port 3000
```

### Module Not Found
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### TypeScript Errors
```bash
# Check TypeScript configuration
npx tsc --noEmit
```

## Project Structure

```
.
├── App.tsx              # Main demo application
├── App.css              # Demo app styling
├── ModelTabs.tsx        # Dynamic tabs component
├── ModelTabs.css        # Tabs styling
├── main.tsx             # React entry point
├── index.html           # HTML template
├── package.json         # Dependencies
├── tsconfig.json        # TypeScript config
└── README files         # Documentation
```

## Support

For questions or issues:
1. Check IMPLEMENTATION.md for detailed documentation
2. Review SUMMARY.md for technical details
3. Check the code comments for inline explanations

## License

This code is provided as-is for demonstration purposes.
