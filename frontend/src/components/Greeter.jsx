import React, {useEffect, useState} from 'react'
import {Col, Container, Row} from 'react-bootstrap'
import HelloWorld from './HelloWorld'
import HelloBob from './HelloBob'
import NameForm from './NameForm'
import defaultAxios from 'axios'

defaultAxios.defaults.baseURL = 'http://127.0.0.1:8000'

const Greeter = ({apiClient}) => {

  const [name, setName] = useState('')
  const [greeting, setGreeting] = useState('')

  useEffect(() => {
    if (name) {
      apiClient
        .get(`/greet?name=${name}`)
        .then((response) => {
          setGreeting(response.data.greeting)
        })
        .catch((error) => {
          console.error('Error fetching greeting:', error)
        })
    }
  }, [name, apiClient])

  return (
    <Container className="Greeter">
      <Row>
        <Col>
          {name ? <HelloBob name={name} greeting={greeting}/> : <HelloWorld/>}
        </Col>
      </Row>
      <hr/>
      <Row>
        <Col>
          <NameForm setName={setName}/>
        </Col>
      </Row>
    </Container>
  )
}

// Set the default prop value for apiClient
Greeter.defaultProps = {
  apiClient: defaultAxios,
}

export default Greeter