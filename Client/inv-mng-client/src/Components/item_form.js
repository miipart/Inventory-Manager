import React from 'react'
import axios from 'axios'
import {Redirect} from 'react-router-dom'

export class ItemForm extends(React.Component) {

  constructor(props) {
    super(props)
    this.state = {name: '', category_id: '', redirect: false}
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }



  handleChange(event) {
    if(event.target.name === "name"){
      this.setState({name: event.target.value})
    }
    else{
        this.setState({category_id: event.target.value})
    }

  }

  handleSubmit(event) {
    event.preventDefault();

    var data = new FormData()
    data.set('name', this.state.name)
    data.set('category_id', this.state.category_id)


    axios.post('http://127.0.0.1:5000/api/item/new', data)
    .then(response => this.props.items.push(response.data))
    .then(() => alert("Item added"))

    this.setState({name: '',category_id: ''})
  }


  render() {
    return(
      <form onSubmit={this.handleSubmit}>
        <div>
          <label for="name">Name</label>
          <input type="text" name="name" onChange={this.handleChange} value={this.state.name} placeholder="name" />
        </div>
        <div>
          <label for="name">Category_ID</label>
          <input type="text" name="category_id" onChange={this.handleChange} value={this.state.category_id} placeholder="category_id" />
        </div>
        <button type="submit">Add</button>
      </form>
    )
  }
}


export default ItemForm
