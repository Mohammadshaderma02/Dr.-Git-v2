import React,{useState} from 'react'
import { Form } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import {useFormik} from 'formik'
import { ToastContainer, toast } from 'react-toastify';
import axios from 'axios';
function Model(props) {
    const[image,setImage]=useState('')
    const[message,setMessage]=useState("")

    const handleImage=(event)=>{
        console.log(event.target.files);
    setImage(event.target.files[0])
    }
    const formik=useFormik({
        initialValues:{
            file:''
        },
        onSubmit:values=>{
            const formData=new FormData();
  formData.append('files',image)
  axios.post('/api/cancer', formData).then(res=>{
   
   if(res.data.result[1]==0){
    setMessage("Adenocarcinoma");
    console.log(0);
   }
    if(res.data.result[1]==1){
    setMessage("Large cell carcinoma");
    toast.success(message, {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: false,
        draggable: true,
        progress: undefined,
        theme: "light",
        })
   }
    if(res.data.result[1]==2){
    console.log(2);
    setMessage("Normal");
    toast.success(message, {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: false,
        draggable: true,
        progress: undefined,
        theme: "light",
        })
   }
    if(res.data.result[1]==3){
    setMessage("Squamous");
    console.log(3);
   }
   else{
    setMessage(res.data.resul)
    console.log(4);
   }
   

  
  }).catch(error=>{
    console.log(error);
    toast.error("File type is not allowed", {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: false,
        draggable: true,
        progress: undefined,
        theme: "light",
        })
  })
          
            
        },
        
        
    })
  return (
    <>
   
   {message}
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Upload File
        </Modal.Title>
      </Modal.Header>
       <Form onSubmit={formik.handleSubmit}>
      <Modal.Body>
       <Form.Group className="position-relative mb-3">
            <Form.Label>File</Form.Label>
            <Form.Control
              type="file"
              required
              name="file"
              onChange={handleImage}
              
            />
            <Form.Control.Feedback type="invalid" tooltip>
         
            </Form.Control.Feedback>
          </Form.Group>

      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide} variant='danger'>Close</Button>
        <Button onClick={props.onHide} type='submit'>Show Result</Button>
      </Modal.Footer>
       </Form>
    </Modal>
    </>
  )
}

export default Model