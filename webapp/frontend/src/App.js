import React from 'react';
import {BrowserRouter, Route} from 'react-router-dom'
import './App.css';


import Navbar from './components/Navbar'
import Home from './components/screens/Home'
import TestResults from './components/screens/TestResults'
import Login from './components/screens/Login'
// import Signup from './components/screens/Signup'
import Forums from './components/screens/Forums'

function App() {
  return (
    <div>
      <BrowserRouter>
      <Navbar />
      <Route exact path="/">
        <Home />
      </Route>
      <Route path= "/test_results">
        <TestResults />
      </Route >
      <Route path= "/forums">
        <Forums />
      </Route>
      <Route path= "/login">
        <Login />
      </Route>
      <Route path= "/login">
        <Login />
      </Route>
    </BrowserRouter>
    </div>
  );
}

export default App;
