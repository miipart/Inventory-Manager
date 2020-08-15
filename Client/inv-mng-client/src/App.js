import React from 'react';
import logo from './logo.svg';
import './App.css';
import Item from './Components/item.js'
import Nav from './Components/nav.js'
import Items from './Components/items.js'
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';
import NewItem from './Components/new_item.js'

class App extends(React.Component) {

  state = {
    items:[]
  }

  componentDidMount(){
    fetch('http://127.0.0.1:5000/api/item/get')
    .then(res => res.json())
    .then((data) => {
      this.setState({ items: data })
      console.log(this.state.todos)
    })
    .catch(console.log)
  }

  render(){
    return (
      <div className="App">
        <Router>
          <Nav />
          <Switch>
            <Route path="/" exact render={() => (<Item name="Rock" />)} />
            <Route path="/items" render={() => (<Items item_list={this.state.items}  />)} />
            <Route path="/item/new" render={() => (<NewItem items={this.state.items} />)} />
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
