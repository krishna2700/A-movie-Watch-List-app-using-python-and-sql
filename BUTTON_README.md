# Blue to Red Button

## Overview
This is a simple interactive button that changes color from blue to red when clicked.

## File
- `button.html` - The HTML file containing the button implementation

## How It Works

### HTML Structure
The button is implemented as a simple HTML button element with an ID of `colorButton`:
```html
<button id="colorButton" onclick="changeColor()">Click Me!</button>
```

### Styling
The button is styled with CSS to:
- Display a blue background color initially
- Have white text
- Be centered on the page
- Include rounded corners (8px border-radius)
- Show a slight opacity change on hover for better UX

### Functionality
When the button is clicked:
1. The `changeColor()` JavaScript function is triggered
2. The function retrieves the button element using `document.getElementById('colorButton')`
3. The button's background color is changed from blue to red using inline styles

### Code
```javascript
function changeColor() {
    const button = document.getElementById('colorButton');
    button.style.backgroundColor = 'red';
}
```

## Usage
Simply open `button.html` in any web browser. Click the blue button and watch it turn red!

## Browser Compatibility
This implementation uses basic HTML, CSS, and JavaScript and is compatible with all modern browsers.
