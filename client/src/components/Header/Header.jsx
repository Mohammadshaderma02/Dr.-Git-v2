import React from 'react'
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
function Header() {
  return (
  <>
  <Navbar expand="lg" variant="light" bg="light">
      <Container>
        <Navbar.Brand href="#home">Doctor Git</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          
        </Navbar.Collapse>
      </Container>
    </Navbar>
  </>
  )
}

export default Header