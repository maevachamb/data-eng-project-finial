import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders learn react link', () => {
  web = render(<App />);
  expect(web).toMatchSnapshot();
});
