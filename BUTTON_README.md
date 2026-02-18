# Blue Button - Click to Turn Red

## Overview
This project demonstrates a simple interactive button that changes color from blue to red when clicked.

## Features
- **Initial State**: The button starts as blue (#007bff)
- **On Click**: The button toggles to red (#dc3545)
- **Smooth Transition**: Includes a CSS transition for smooth color change
- **Hover Effect**: Button opacity changes on hover for better user feedback

## Files
- `button.html` - Contains the complete HTML, CSS, and JavaScript implementation

## How It Works

### HTML Structure
The button is created using a standard HTML `<button>` element with an `id` of `colorButton`.

### CSS Styling
- The button is styled with a blue background color (`#007bff`)
- A CSS class `.red` is defined to change the background to red (`#dc3545`)
- A transition effect is applied for smooth color changes
- The button includes padding, border-radius, and a box-shadow for a modern appearance

### JavaScript Functionality
The `toggleColor()` function:
1. Gets a reference to the button element
2. Toggles the `red` CSS class on the button
3. This causes the button to switch between blue and red states

## Usage
1. Open `button.html` in a web browser
2. Click the button to toggle between blue and red
3. Click again to toggle back to blue

## Browser Compatibility
Works in all modern browsers that support:
- CSS transitions
- JavaScript ES5+
- CSS classList API

## Customization
You can customize the colors by modifying the CSS:
- Change `#007bff` to any blue shade for the initial color
- Change `#dc3545` to any red shade for the clicked state
- Adjust the transition duration by modifying `transition: background-color 0.3s ease;`
