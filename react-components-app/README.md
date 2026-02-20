# React Reusable Components Library

A comprehensive collection of beautiful, reusable React components built with modern best practices.

## Components Included

### 1. **Button**
A versatile button component with multiple variants and sizes.

**Props:**
- `variant`: 'primary' | 'secondary' | 'success' | 'danger' (default: 'primary')
- `size`: 'small' | 'medium' | 'large' (default: 'medium')
- `onClick`: Function to handle click events
- `disabled`: Boolean to disable the button
- `type`: 'button' | 'submit' | 'reset' (default: 'button')
- `fullWidth`: Boolean to make button full width

**Usage:**
```jsx
import { Button } from './components';

<Button variant="primary" size="medium" onClick={handleClick}>
  Click Me
</Button>
```

### 2. **Card**
A flexible card component for displaying content.

**Props:**
- `title`: Card title
- `subtitle`: Card subtitle
- `footer`: Footer content
- `hoverable`: Boolean to enable hover effect
- `className`: Additional CSS classes

**Usage:**
```jsx
import { Card } from './components';

<Card 
  title="Card Title" 
  subtitle="Subtitle"
  hoverable
  footer={<Button>Action</Button>}
>
  Card content goes here
</Card>
```

### 3. **Input**
A form input component with label and error handling.

**Props:**
- `type`: Input type (default: 'text')
- `label`: Input label
- `placeholder`: Placeholder text
- `value`: Input value
- `onChange`: Change handler
- `error`: Error message
- `disabled`: Boolean to disable input
- `required`: Boolean to mark as required
- `name`: Input name
- `id`: Input ID

**Usage:**
```jsx
import { Input } from './components';

<Input
  label="Email"
  type="email"
  name="email"
  value={email}
  onChange={handleChange}
  error={errors.email}
  required
/>
```

### 4. **Modal**
A modal dialog component with overlay.

**Props:**
- `isOpen`: Boolean to control visibility
- `onClose`: Function to handle close
- `title`: Modal title
- `footer`: Footer content
- `size`: 'small' | 'medium' | 'large' (default: 'medium')

**Usage:**
```jsx
import { Modal } from './components';

<Modal
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
  title="Modal Title"
  footer={<Button onClick={handleConfirm}>Confirm</Button>}
>
  Modal content
</Modal>
```

### 5. **Alert**
An alert component for displaying messages.

**Props:**
- `type`: 'info' | 'success' | 'warning' | 'danger' (default: 'info')
- `dismissible`: Boolean to show close button
- `onClose`: Function to handle close

**Usage:**
```jsx
import { Alert } from './components';

<Alert type="success" dismissible onClose={handleClose}>
  Operation successful!
</Alert>
```

### 6. **Badge**
A badge component for labels and counts.

**Props:**
- `variant`: 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info'
- `size`: 'small' | 'medium' | 'large' (default: 'medium')
- `rounded`: Boolean for rounded style

**Usage:**
```jsx
import { Badge } from './components';

<Badge variant="success" rounded>New</Badge>
```

### 7. **Spinner**
A loading spinner component.

**Props:**
- `size`: 'small' | 'medium' | 'large' (default: 'medium')
- `color`: 'primary' | 'secondary' | 'success' | 'danger'
- `centered`: Boolean to center the spinner

**Usage:**
```jsx
import { Spinner } from './components';

<Spinner size="medium" color="primary" centered />
```

## Getting Started

### Installation

```bash
cd react-components-app
npm install
```

### Running the Application

```bash
npm start
```

The application will open at [http://localhost:3000](http://localhost:3000)

### Building for Production

```bash
npm run build
```

## Project Structure

```
react-components-app/
├── src/
│   ├── components/
│   │   ├── Alert/
│   │   │   ├── Alert.js
│   │   │   └── Alert.css
│   │   ├── Badge/
│   │   │   ├── Badge.js
│   │   │   └── Badge.css
│   │   ├── Button/
│   │   │   ├── Button.js
│   │   │   └── Button.css
│   │   ├── Card/
│   │   │   ├── Card.js
│   │   │   └── Card.css
│   │   ├── Input/
│   │   │   ├── Input.js
│   │   │   └── Input.css
│   │   ├── Modal/
│   │   │   ├── Modal.js
│   │   │   └── Modal.css
│   │   ├── Spinner/
│   │   │   ├── Spinner.js
│   │   │   └── Spinner.css
│   │   └── index.js
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
└── package.json
```

## Features

- ✅ **Reusable Components**: All components are modular and reusable
- ✅ **Customizable**: Props-based customization for flexibility
- ✅ **Responsive**: Mobile-friendly design
- ✅ **Modern Styling**: Clean, modern UI with smooth animations
- ✅ **Accessible**: Semantic HTML and proper ARIA attributes
- ✅ **Well-Documented**: Clear documentation and examples

## Best Practices

- Components are organized in separate folders with their own CSS
- Each component is exported through a central index file
- Props are validated and have sensible defaults
- CSS uses BEM-like naming conventions
- Components are functional and use React hooks
- Animations and transitions for better UX

## License

MIT
