import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders learn react link', () => {
  const web = render(<App />);
  expect(web).toMatchSnapshot();
});
