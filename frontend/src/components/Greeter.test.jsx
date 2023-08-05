import React from 'react'
import {fireEvent, render, screen} from '@testing-library/react'
import Greeter from './Greeter'

describe('Greeter component', () => {
    test('typing in the input field updates the name', () => {
        render(<Greeter/>)
        const inputField = screen.getByLabelText('Name:')
        const name = 'Alice'
        fireEvent.change(inputField, {target: {value: name}})
        expect(inputField.value).toBe(name)
    })

    test('renders HelloBob component when a name is provided', () => {
        render(<Greeter/>)

        // Find the input field and the submit button in the NameForm
        const inputField = screen.getByPlaceholderText('Enter your name')
        const submitButton = screen.getByRole('button', {name: 'Submit'})

        // Simulate user input
        fireEvent.change(inputField, {target: {value: 'Bob'}})
        fireEvent.click(submitButton)

        // Expect that the HelloBob component is rendered with the provided name
        const helloBobElement = screen.getByText('Hello, Bob!')
        expect(helloBobElement).toBeInTheDocument()

        // Expect that the HelloWorld component is not present in the document anymore
        const helloWorldElement = screen.queryByText('Hello, World!')
        expect(helloWorldElement).not.toBeInTheDocument()
    })

    test('renders HelloWorld component when no name is provided', () => {
        render(<Greeter/>)

        // Expect that the HelloWorld component is initially rendered
        const helloWorldElement = screen.getByText('Hello, World!')
        expect(helloWorldElement).toBeInTheDocument()

        // Expect that the HelloBob component is not present in the document
        const helloBobElement = screen.queryByText('Hello, Bob!')
        expect(helloBobElement).not.toBeInTheDocument()
    })
})
