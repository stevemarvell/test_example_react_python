import React from 'react'
import {Card} from 'react-bootstrap'

const HelloWorld = () => {
  return (
    <Card className="my-4">
      <Card.Body>
        <Card.Title data-testid="greeting">Hello, World!</Card.Title>
      </Card.Body>
    </Card>
  )
}

export default HelloWorld
