import React from 'react'
import {render, screen} from '@testing-library/react'
import HelloWorld from './HelloWorld'

describe('HelloWorld component', () => {
  test('renders "Hello, World!"', () => {
    render(<HelloWorld/>)
    const greetingElement = screen.getByTestId('greeting')
    expect(greetingElement).toHaveTextContent('Hello, World!')
  })
})
