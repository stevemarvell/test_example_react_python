import React from 'react'
import {render, screen} from '@testing-library/react'
import HelloBob from './HelloBob'

describe('HelloBob component', () => {
  test('renders Hello, Bob! in the correct place', () => {
    render(<HelloBob name="Bob" greeting="Bob"/>)
    const greetingElement = screen.getByTestId('greeting')
    expect(greetingElement).toHaveTextContent('Hello, Bob!')
  })
})
