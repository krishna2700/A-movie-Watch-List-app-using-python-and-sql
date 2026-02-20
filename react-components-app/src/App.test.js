import { render, screen } from '@testing-library/react';
import App from './App';

test('renders React Reusable Components Library', () => {
  render(<App />);
  const heading = screen.getByText(/React Reusable Components Library/i);
  expect(heading).toBeInTheDocument();
});
