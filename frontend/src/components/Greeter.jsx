import React, { useState } from 'react'
import HelloWorld from './HelloWorld'
import NameForm from './NameForm'

function Greeter() {
  const [name, setName] = useState('')

  return (
    <div className="App">
      <header className="App-header">
        {name ? <HelloWorld name={name} /> : <HelloWorld />}
        <hr />
        <NameForm setName={setName} />
      </header>
    </div>
  )
}

export default Greeter
