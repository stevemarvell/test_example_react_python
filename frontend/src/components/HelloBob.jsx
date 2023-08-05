import React from 'react'
import { Card } from 'react-bootstrap'

const HelloBob = ({ name, greeting }) => {
  const getGreeting = () => {
    if (name.toLowerCase() === 'bob') {
      return 'Hello, Bob!'
    } else {
      return `${greeting}, ${name}!`
    }
  }

  return (
    <Card className="my-4">
      <Card.Body>
        <Card.Title data-testid="greeting">{getGreeting()}</Card.Title>
      </Card.Body>
    </Card>
  )
}

export default HelloBob
