import React from 'react'
import {fireEvent, render, screen, waitFor} from '@testing-library/react'
import Greeter from './Greeter'

describe('Greeter component end to end', () => {

  test('renders HelloWorld component when no name is provided', async () => {
    render(<Greeter/>)

    // Expect that the HelloWorld component is initially rendered
    const greetingElement = screen.getByTestId('greeting')
    expect(greetingElement).toHaveTextContent("Hello, World!")

    // Find the input field and the submit button in the NameForm
    const inputField = screen.getByTestId('name-field')
    const submitButton = screen.getByTestId('submit-button')

    // Simulate user input
    fireEvent.change(inputField, {target: {value: 'Bob'}})
    fireEvent.click(submitButton)

    // Wait for the API call and response
    await waitFor(() => {
      const greetingElement = screen.getByTestId('greeting')
      // expect(greetingElement).toBeInTheDocument()
      // keep it to one assertion, so says eslint
      expect(greetingElement).toHaveTextContent(/Bob/)
    })
  })
})
