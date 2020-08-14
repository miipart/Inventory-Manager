import React from 'react';
import logo from './logo.svg';
import './App.css';
import Item from './Components/item.js'
import Nav from './Components/nav.js'

function App() {
  return (
    <div className="App">
      <Nav />
      <Item name="heööp" category="Rocks"/>
    </div>
  );
}

export default App;
