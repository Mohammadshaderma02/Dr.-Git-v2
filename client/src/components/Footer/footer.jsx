import React from 'react'
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
function footer() {
  return (
  <>
  <Navbar fixed="bottom" variant="light" bg="light">
      <Container>
        
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-center">
          <Navbar.Text>
          Copyright © Mohammad Shaderma
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  </>
  )
}

export default footer