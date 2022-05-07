import React from 'react';
import './App.css';
import Header from './layouts/Header';
import Navigation from './layouts/Navigation';
import TableElements from './layouts/TableElements';
import ModalElement from './layouts/ModalElement';
/*
import Main from './layouts/Main';
import SubContents from './layouts/SubContents';*/
import Footer from './layouts/Footer';


function App() {
  return (
    <div className="app">
        <Header />
        <Navigation />
        <TableElements>
            <ModalElement/>
        </TableElements>
        <Footer />
    </div>
  );
}

export default App;
