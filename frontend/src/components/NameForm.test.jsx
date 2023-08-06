import React from 'react'
import {fireEvent, render, screen} from '@testing-library/react'
import NameForm from './NameForm'

describe('NameForm component', () => {
  test('captures user input correctly and clears the input field after submission', () => {
    const setNameMock = jest.fn() // Create a mock function to simulate setName prop

    render(<NameForm setName={setNameMock}/>)

    const inputField = screen.getByTestId('name-field')
    const submitButton = screen.getByTestId('submit-button')

    fireEvent.change(inputField, {target: {value: 'Alice'}})
    fireEvent.click(submitButton)

    // Expect that setNameMock was called with 'Alice' as an argument
    expect(setNameMock).toHaveBeenCalledWith('Alice')

    // Expect that the input field is cleared after submission
    expect(inputField.value).toBe('')
  })
})

