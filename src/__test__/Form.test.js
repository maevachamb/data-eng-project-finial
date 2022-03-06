import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event' // testing helpers for imitating user 
import { mount, shallow } from 'enzyme';
import Form from '../Component/Form';

Enzyme.configure({ adapter: new Adapter() });

describe('Form', () => {
    test('renders correctly across screens', () => {
        const tree = render(<Form/>);
        expect(tree).toMatchSnapshot();
    });

})
