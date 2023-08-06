import React, {useState} from 'react'
import {Button, Form} from 'react-bootstrap'

const NameForm = ({setName}) => {
  const [nameInput, setNameInput] = useState('')

  const handleInputChange = (event) => {
    setNameInput(event.target.value)
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    setName(nameInput)
    setNameInput('') // Clear the input field after submitting
  }

  return (
    <div>
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Name:</Form.Label>
          <Form.Control
            data-testid="name-field"
            type="text"
            value={nameInput}
            onChange={handleInputChange}
            placeholder="Enter your name"
          />
        </Form.Group>
        <Button data-testid="submit-button" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  )
}

export default NameForm
