import React, { useState } from 'react'

const NameForm = ({ setName }) => {
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
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            data-testid="name-field"
            type="text"
            value={nameInput}
            onChange={handleInputChange}
            placeholder="Enter your name"
          />
        </label>
        <button data-testid="submit-button" type="submit">Submit</button>
      </form>
    </div>
  )
}

export default NameForm
