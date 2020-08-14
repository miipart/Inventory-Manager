import React from 'react';

export class Item extends(React.Component){

  render(){
    return (
      <div>
        <h1>{this.props.name}</h1>
        <p>{this.props.category}</p>
      </div>
    )
  }

}

export default Item
