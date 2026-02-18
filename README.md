# A-movie-Watch-List-app-using-python-and-sql

---

## Reset Button (`reset_button.html`)

### Overview

A simple, standalone HTML page containing a **dummy Reset button** styled in **pink** that turns **white** when clicked.

### How to Use

1. Open `reset_button.html` in any web browser.
2. You will see a pink **Reset** button centered on the page.
3. **Click** the button — it turns **white**.
4. **Click again** — it toggles back to **pink**.

### Behavior

| State     | Background Color | Text Color |
|-----------|------------------|------------|
| Default   | Pink (`#ff69b4`) | White      |
| Clicked   | White (`#ffffff`) | Dark gray  |

### Technical Details

- **No dependencies** — pure HTML, CSS, and JavaScript.
- Toggle is handled via a single `onclick` that adds/removes a CSS class.
- Smooth color transition using `transition: all 0.3s ease`.