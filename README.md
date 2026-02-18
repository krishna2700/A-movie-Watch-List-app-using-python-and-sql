# A-movie-Watch-List-app-using-python-and-sql

## Blue Button Feature

This project includes an interactive HTML button that changes color on click.

### Blue Button Component

**File:** `button.html`

A simple web page featuring a blue button that turns red when clicked. The button can be toggled back and forth between blue and red with each click.

#### Features:
- **Initial State:** Button is blue (#007bff)
- **On Click:** Button changes to red (#dc3545)
- **Toggle Behavior:** Clicking again switches it back to blue
- **Smooth Transitions:** CSS transitions provide smooth color changes
- **Hover Effects:** Button darkens slightly on hover for better user feedback

#### How to Use:
1. Open `button.html` in a web browser
2. Click the button to change its color from blue to red
3. Click again to toggle back to blue

#### Technical Implementation:
- **HTML:** Semantic structure with a button element
- **CSS:** Styling with hover effects and smooth transitions
- **JavaScript:** Event handler that toggles a CSS class on click
- Uses CSS classes for state management (`.red` class)

#### Code Structure:
- The button starts with `background-color: #007bff` (blue)
- On click, the `changeColor()` function toggles the `red` class
- The `.red` class applies `background-color: #dc3545` (red)
- CSS transitions provide smooth color changes