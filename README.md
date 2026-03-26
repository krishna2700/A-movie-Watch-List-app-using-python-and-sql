# React Movie Watch List App

A modern, responsive movie watch list application built with React that allows users to track movies they want to watch, have watched, and rate their favorites.

## Features

- Add movies to your watch list
- Mark movies as watched/unwatched
- Rate movies with a 5-star rating system
- Search and filter your movie collection
- Responsive design for mobile and desktop
- Local storage persistence

## Tech Stack

- **React** - Frontend library
- **React Hooks** - State management
- **CSS3** - Styling
- **LocalStorage** - Data persistence

## Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (v14.0 or higher)
- npm (v6.0 or higher) or yarn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/react-movie-watchlist.git
cd react-movie-watchlist
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm start
# or
yarn start
```

4. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## Available Scripts

In the project directory, you can run:

### `npm start`
Runs the app in development mode. The page will reload when you make changes.

### `npm test`
Launches the test runner in interactive watch mode.

### `npm run build`
Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance.

### `npm run eject`
**Note: this is a one-way operation. Once you eject, you can't go back!**

## Project Structure

```
react-movie-watchlist/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── MovieCard.js
│   │   ├── MovieList.js
│   │   ├── AddMovie.js
│   │   └── SearchBar.js
│   ├── hooks/
│   │   └── useLocalStorage.js
│   ├── App.js
│   ├── App.css
│   └── index.js
├── package.json
└── README.md
```

## Usage

### Adding a Movie
1. Click on the "Add Movie" button
2. Enter the movie title, year, and other details
3. Click "Save" to add it to your watch list

### Marking as Watched
- Click the "Watched" toggle button on any movie card
- The movie will be moved to the "Watched" section

### Rating Movies
- Click on the stars to rate a movie (1-5 stars)
- Your rating is saved automatically

### Searching
- Use the search bar to filter movies by title
- Results update in real-time as you type

## Component Overview

### `App.js`
Main application component that manages the overall state and routing.

### `MovieCard.js`
Displays individual movie information with controls for marking as watched and rating.

### `MovieList.js`
Renders a list of movie cards based on the current filter/search.

### `AddMovie.js`
Form component for adding new movies to the list.

### `SearchBar.js`
Search input component with filtering functionality.

## State Management

This application uses React Hooks for state management:
- `useState` - For component-level state
- `useEffect` - For side effects and data persistence
- `useContext` - For global state (if implemented)
- Custom `useLocalStorage` hook - For automatic localStorage synchronization

## Styling

The application uses vanilla CSS with a mobile-first approach. Styles are organized by component and follow BEM naming conventions.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Integration with external movie API (TMDB, OMDB)
- [ ] User authentication
- [ ] Backend database integration
- [ ] Movie recommendations
- [ ] Social sharing features
- [ ] Export/Import watch list

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Movie data powered by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Inspiration from various movie tracking applications

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/react-movie-watchlist](https://github.com/yourusername/react-movie-watchlist)

---

Made with ❤️ using React
