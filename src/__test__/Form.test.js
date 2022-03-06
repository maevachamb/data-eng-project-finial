import { render, screen } from '@testing-library/react';
import Form from '../Component/Form';

test('renders correctly across screens', () => {
    const tree = render(<Form/>);
    expect(tree).toMatchSnapshot();
  });