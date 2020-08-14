import React from 'react'
import './nav.css'

export class Nav extends(React.Component){
  render(){
    return(
      <nav>
        <div>
          <a href="#">New Item</a>
        </div>
        <div>
          <a>New Category</a>
        </div>
        <div>
          <a>Items</a>
        </div>
        <div>
          <a>Categories</a>
        </div>
      </nav>

    )
  }
}

export default Nav
