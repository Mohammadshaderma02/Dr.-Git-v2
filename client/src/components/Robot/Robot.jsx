import { Button, Row,Col,Dropdown } from 'react-bootstrap'
import React from 'react'

import Container from 'react-bootstrap/esm/Container'
import Logo from '../../assets/robot.gif'
import {useState} from 'react'
import Typewriter from "typewriter-effect";
import Styles from './Robot.module.css'
import Model from '../ModelResult/Model'
import ModelCancer from '../ModelResult/ModelCancer'
function Robot() {
    const [modalShow, setModalShow] = React.useState(false);
    const [modalShow2, setModalShow2] = React.useState(false);

  return (
    <>
    
   <Container className='mt-5'>
    <ModelCancer show={modalShow2}
        onHide={() => setModalShow2(false)}/>
    <Model  show={modalShow}
        onHide={() => setModalShow(false)}/>
<Row>
<Dropdown>
  <Dropdown.Toggle variant="primary" id="dropdown-basic">
   Upload Image
  </Dropdown.Toggle>

  <Dropdown.Menu>
    <Dropdown.Item onClick={() => setModalShow(true)}>Examination for pneumonia</Dropdown.Item>
    <Dropdown.Item onClick={() => setModalShow2(true)}>Examination of cancer cells</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>
</Row>
<Row><Col className='d-flex'><img src={Logo} alt="Logo Dr Git"/>
<div className={Styles.Text}>

<Typewriter
  className={{backGround:'blue'}}
  onInit={(typewriter)=> {

  typewriter
   
  .typeString(`<h3 variant={'dark'}>Hello, I am Dr. Git V1. I was developed by Mohammad Shaderma to analyze x-ray images and indicate whether there is pneumonia in the patient or not ِAnd Examination of cancer cells.</h3>`)
    
//   .pauseFor(500)
//   .deleteAll()
//   .typeString(`<h6>Dr. Git</h6>`)

  .start();
  }}
  />
  </div>
</Col>

</Row>
   </Container>
    </>
  )
}

export default Robot