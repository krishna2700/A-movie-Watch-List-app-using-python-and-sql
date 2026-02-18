# Blue to Red Button

## Overview
This is a simple interactive web button that demonstrates basic HTML, CSS, and JavaScript functionality.

## Features
- **Initial State**: The button starts with a blue background color
- **Interactive**: When clicked, the button changes from blue to red
- **Responsive Design**: Centered on the page with hover effects

## Files
- `button.html` - Contains the complete implementation

## How It Works

### HTML Structure
The button is created using a standard HTML `<button>` element with an `onclick` event handler:
```html
<button id="colorButton" onclick="changeColor()">Click Me!</button>
```

### CSS Styling
- Initial background color: `blue`
- White text color for contrast
- Rounded corners (8px border-radius)
- Padding: 20px vertical, 40px horizontal
- Smooth transition effect for color changes
- Hover effect with opacity change

### JavaScript Functionality
The `changeColor()` function is triggered when the button is clicked:
```javascript
function changeColor() {
    const button = document.getElementById('colorButton');
    button.style.backgroundColor = 'red';
}
```

This function:
1. Gets the button element by its ID
2. Changes the background color from blue to red

## Usage
1. Open `button.html` in any modern web browser
2. Click the blue button
3. Watch it turn red!

## Technical Details
- Pure vanilla JavaScript (no frameworks required)
- CSS3 for styling and transitions
- HTML5 compliant
- Works in all modern browsers

## Browser Compatibility
- Chrome ✓
- Firefox ✓
- Safari ✓
- Edge ✓
- Opera ✓
