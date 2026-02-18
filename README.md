# Blue to Red Button

A simple interactive web page featuring a button that changes color from blue to red when clicked.

## Features

- **Initial State**: The button starts with a blue background color
- **Interactive**: Clicking the button changes its background color to red
- **Responsive Design**: Centered layout that works on different screen sizes
- **Smooth Transition**: 0.3s ease transition for visual polish

## Files

- `index.html` - Main HTML file containing the button, styling, and JavaScript functionality

## How It Works

The implementation uses:

1. **HTML**: A button element with an `onclick` event handler
2. **CSS**: 
   - Blue background color (`background-color: blue`)
   - Centered layout using flexbox
   - Hover effect for better user experience
   - Smooth transition animation
3. **JavaScript**: 
   - `changeColor()` function that changes the button's background to red
   - Uses `document.getElementById()` to target the button
   - Modifies the `backgroundColor` style property

## Usage

1. Open `index.html` in any modern web browser
2. Click the blue button
3. The button will change to red

## Code Structure

```html
<button id="colorButton" onclick="changeColor()">Click Me!</button>
```

```javascript
function changeColor() {
    const button = document.getElementById('colorButton');
    button.style.backgroundColor = 'red';
}
```

## Browser Compatibility

Works in all modern browsers including:
- Chrome
- Firefox
- Safari
- Edge

## License

Free to use and modify.
