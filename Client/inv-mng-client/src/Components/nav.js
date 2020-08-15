import React from 'react'
import './nav.css'
import {BrowserRouter as Router, Route, Link, Switch}  from 'react-router-dom';


export class Nav extends(React.Component){
  render(){
    return(
      <nav>
        <div>
          <Link to="/">Home</Link>
        </div>
        <div>
          <a>New Category</a>
        </div>
        <div>
          <Link to="/items">Items</Link>
        </div>
        <div>
          <a>Categories</a>
        </div>
      </nav>

    )
  }
}

export default Nav
