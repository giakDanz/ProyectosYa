import React from 'react';
import './App.css';
import Header from './layouts/Header';
import Navigation from './layouts/Navigation';
import Main from './layouts/Main';
import SubContents from './layouts/SubContents';
import Footer from './layouts/Footer';

                
function App() {
  return (
    <div className="app">
        <Header />
        <Navigation />
        <Main>
            <SubContents />
            <SubContents />
            <SubContents />
        <Footer />
        </Main>
    </div>
  );
}
                
export default App;
