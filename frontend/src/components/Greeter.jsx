import React, {useEffect, useState} from 'react'
import {Col, Container, Row} from 'react-bootstrap'
import HelloWorld from './HelloWorld'
import HelloBob from './HelloBob'
import NameForm from './NameForm'
import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000'
})

const Greeter = () => {
    const [name, setName] = useState('')
    const [greeting, setGreeting] = useState('')

    useEffect(() => {
        if (name) {
            api
                .get(`/greet?name=${name}`)
                .then((response) => {
                    const d = response.data
                    console.log(d)
                    setGreeting(response.data.greeting)
                })
                .catch((error) => {
                    console.error('Error fetching greeting:', error)
                })
        }
    }, [name])

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

export default Greeter
