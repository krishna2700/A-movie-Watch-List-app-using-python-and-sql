# Blue to Red Button

## Overview
This is a simple interactive web button that demonstrates basic HTML, CSS, and JavaScript functionality.

## Features
- **Initial State**: The button starts with a blue background color
- **Interactive**: When clicked, the button changes from blue to red
- **Responsive Design**: Centered on the page with hover effects

## Files
- `button.html` - Main HTML file containing the button implementation

## How It Works

### HTML Structure
The button is created using a standard HTML `<button>` element with an `onclick` event handler.

### CSS Styling
- **Background Color**: Initially set to blue
- **Padding**: 20px vertical, 40px horizontal for a comfortable click area
- **Border Radius**: 8px for rounded corners
- **Transition**: Smooth 0.3s transition effect for color changes
- **Hover Effect**: Slight opacity change on hover for better user feedback

### JavaScript Functionality
The `changeColor()` function is triggered when the button is clicked:
```javascript
function changeColor() {
    const button = document.getElementById('colorButton');
    button.style.backgroundColor = 'red';
}
```

This function:
1. Gets a reference to the button element by its ID
2. Changes the background color from blue to red

## Usage

### Opening the Button
Simply open the `button.html` file in any modern web browser:
- Double-click the file, or
- Right-click and select "Open with" your preferred browser, or
- Use a local development server

### Interaction
1. The page loads with a blue button centered on the screen
2. Click the button
3. The button instantly changes to red
4. The color change persists until the page is refreshed

## Technical Details
- **No Dependencies**: Pure HTML, CSS, and JavaScript - no external libraries required
- **Browser Compatibility**: Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- **Responsive**: Centered layout adapts to different screen sizes

## Customization
You can easily customize the button by modifying:
- **Colors**: Change the initial `background-color: blue` or the target color `'red'` in the JavaScript
- **Size**: Adjust the `padding` and `font-size` values
- **Text**: Modify the button text "Click Me!" to anything you prefer
- **Animation**: Adjust the `transition` duration for faster/slower color changes

## Future Enhancements
Possible improvements could include:
- Toggle functionality (click again to turn back to blue)
- Multiple color options
- Animation effects
- Sound effects on click
- Click counter
