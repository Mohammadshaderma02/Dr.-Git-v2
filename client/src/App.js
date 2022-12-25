import React,{useState,useEffect} from 'react'
import { ChangeEvent} from 'react';
import axios from 'axios'
import Header from './components/Header/Header';
import 'react-toastify/dist/ReactToastify.css';
import Robot from './components/Robot/Robot';
import Footer from './components/Footer/footer';
function App() {


  return (
 <>

 <Header/>

 <Robot/>
 <Footer/>
 </>
  )
}

export default App