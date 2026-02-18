# A-movie-Watch-List-app-using-python-and-sql

## Reset Button

A simple HTML page featuring a pink reset button that changes to white when clicked.

### Features

- Pink background color that changes to white on click
- Centered layout on the page
- Smooth color transition animation
- Responsive hover effect

### Usage

#### Opening the Page

1. Open `reset_button.html` in any modern web browser
2. The reset button will be displayed in the center of the page

#### Interacting with the Button

- **Click**: Click the button to change its background color from pink to white
- **Hover**: Hover over the button to see a slight opacity change

### Technical Details

#### HTML Structure

The page contains a single button element with the ID `resetButton`:
```html
<button id="resetButton">Reset</button>
```

#### Styling

- **Initial state**: Pink background with black text
- **Clicked state**: White background with black text
- **Button dimensions**: 15px vertical padding, 30px horizontal padding
- **Font size**: 16px
- **Border radius**: 5px for rounded corners

#### JavaScript Behavior

The button uses an event listener to detect clicks:
```javascript
resetButton.addEventListener('click', function() {
    this.classList.add('clicked');
    this.style.backgroundColor = 'white';
});
```

When clicked, the button:
1. Adds the `clicked` CSS class
2. Changes the background color to white

### Browser Compatibility

This button works in all modern browsers that support:
- CSS3 transitions
- JavaScript ES5+ event listeners
- HTML5

### File Structure

```
.
├── reset_button.html    # Pink reset button page
└── README.md           # This file
```

### Customization

To customize the button appearance, modify the CSS in the `<style>` section of `reset_button.html`:

- **Initial color**: Change `background-color: pink;` in `#resetButton`
- **Clicked color**: Change `background-color: white;` in `#resetButton.clicked`
- **Button size**: Adjust the `padding` values
- **Font**: Modify the `font-size` and `font-family` properties
- **Animation speed**: Change the `transition` duration (currently 0.3s)