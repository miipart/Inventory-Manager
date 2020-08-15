import React from 'react'
import ItemForm from './item_form.js'

export class NewItem extends(React.Component) {

  render(){
    return(
      <div>
        <h1>New Item</h1>
        <ItemForm items={this.props.items}/>
      </div>

    )
  }
}


export default NewItem
