import React, { useState } from 'react'
import HelloWorld from './HelloWorld'
import NameForm from './NameForm'
import HelloBob from "./HelloBob"
import { Container, Row, Col } from 'react-bootstrap'

function Greeter() {
  const [name, setName] = useState('')

  return (
    <Container className="App">
      <Row>
        <Col>
          {name ? <HelloBob name={name} /> : <HelloWorld />}
        </Col>
      </Row>
      <hr />
      <Row>
        <Col>
          <NameForm setName={setName} />
        </Col>
      </Row>
    </Container>
  )
}

export default Greeter
