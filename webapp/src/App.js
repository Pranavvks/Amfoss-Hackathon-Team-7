import React,{useState} from 'react' ;
import './App.css' ;
import {BrowserRouter , Route , Switch} from 'react-router-dom';
import Dashboard from './Dashboard' ;
import Preferences from './preferences'
import Login from './Login'
import ProgressBar from './Progress'
function App ()
{
  
  return (
    
    <div className = "wrapper">
      <h1>Application</h1>
      <BrowserRouter>
      <Switch>
        <Route path = "/dashboard">
          <Dashboard />
        </Route>
        <Route path = "/preferences">
          <Preferences />
        </Route>
      </Switch>
      </BrowserRouter>
      <Login />
      <ProgressBar value ={85} />
      </div>
  )
}
export default App ;