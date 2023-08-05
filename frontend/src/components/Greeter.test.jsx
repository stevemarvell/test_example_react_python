import React from 'react'
import {fireEvent, render, screen} from '@testing-library/react'
import Greeter from './Greeter'

describe('Greeter component', () => {

    test('renders HelloWorld component when no name is provided', () => {
        render(<Greeter/>)

        // Expect that the HelloWorld component is initially rendered
        const greetingElement = screen.getByTestId('greeting')
        expect(greetingElement).toHaveTextContent("Hello, World!")
    })

    test('renders HelloBob component when a name is provided', () => {
        render(<Greeter/>)

        // Find the input field and the submit button in the NameForm
        const inputField = screen.getByTestId('name-field')
        const submitButton = screen.getByTestId('submit-button')

        // Simulate user input
        fireEvent.change(inputField, {target: {value: 'Bob'}})
        fireEvent.click(submitButton)

        // Expect that the HelloBob component is rendered with the provided name
        const greetingElement = screen.getByTestId('greeting')
        expect(greetingElement).toBeInTheDocument()
        expect(greetingElement).toHaveTextContent(/Bob/)
    })
})
