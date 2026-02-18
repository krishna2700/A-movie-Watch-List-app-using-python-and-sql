# Blue to Red Button

A simple interactive web page featuring a button that changes color from blue to red when clicked.

## Description

This project demonstrates a basic HTML page with a button that:
- Starts with a **blue** background color
- Changes to **red** when clicked
- Uses vanilla JavaScript for the color change functionality

## Files

- `button.html` - The main HTML file containing the button and functionality

## Features

- Clean, centered layout with responsive design
- Smooth color transition effect
- Hover and active states for better user interaction
- Modern styling with shadows and rounded corners

## How to Use

1. Open `button.html` in any modern web browser
2. Click the blue button
3. The button will change to red

## Technical Details

### HTML Structure
- Single button element with an onclick event handler
- Semantic HTML5 structure

### CSS Styling
- Flexbox for centering
- Custom button styling with:
  - Blue initial background color
  - White text
  - Rounded corners (8px border-radius)
  - Box shadow for depth
  - Smooth transition effects
  - Hover and active states

### JavaScript Functionality
- `changeColor()` function triggered on button click
- Direct DOM manipulation using `getElementById()`
- Changes background color from blue to red

## Browser Compatibility

Works in all modern browsers including:
- Chrome
- Firefox
- Safari
- Edge

## Code Example

```javascript
function changeColor() {
    const button = document.getElementById('colorButton');
    button.style.backgroundColor = 'red';
}
```

## License

This is a demonstration project for educational purposes.
