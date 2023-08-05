import React from 'react'

const HelloBob = ({ name }) => {
  const getGreeting = () => {
    if (name.toLowerCase() === 'bob') {
      return 'Hello, Bob!'
    } else {
      return `Hi, ${name}!`
    }
  }

  return (
    <div>
      <h1 data-testid="greeting">{getGreeting()}</h1>
    </div>
  )
}

export default HelloBob
