# Color Changing Button

## Overview
This project contains a simple interactive button that changes color when clicked.

## File
- `button.html` - Standalone HTML file with embedded CSS and JavaScript

## Functionality
The button implements the following behavior:
- **Initial State**: Blue background with white text
- **On Click**: Background changes to red
- **Hover Effect**: Slightly transparent when hovering over the button

## Technical Details

### HTML Structure
- Single button element with ID `colorButton`
- Centered on the page using flexbox

### CSS Styling
- Default blue background (`background-color: blue`)
- Red state using `.red` class (`background-color: red`)
- Smooth color transition (0.3s ease)
- Hover effect with opacity change

### JavaScript
- Event listener attached to the button's click event
- Adds the `red` class to change the background color

## Usage
1. Open `button.html` in any modern web browser
2. Click the button to change its color from blue to red
3. The color change persists after clicking

## Browser Compatibility
Works in all modern browsers that support:
- CSS3 (flexbox, transitions)
- ES5+ JavaScript (addEventListener)
