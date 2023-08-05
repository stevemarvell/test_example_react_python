import React from 'react'
import {render, screen} from '@testing-library/react'
import HelloBob from './HelloBob'

describe('HelloBob component', () => {
    test('renders Hello, Bob! in the correct place', () => {
        render(<HelloBob name="Bob"/>)
        const greetingElement = screen.getByTestId('greeting')
        expect(greetingElement).toHaveTextContent('Hello, Bob!')
    })

    test('renders Hi, {name}! in the correct place', () => {
        render(<HelloBob name="Alice"/>)
        const greetingElement = screen.getByTestId('greeting')
        expect(greetingElement).toHaveTextContent(/^Hi, Alice!$/i)
    })
})
