import React from 'react';
import {BrowserRouter as Router, Route, Link, Switch}  from 'react-router-dom';

export class Items extends(React.Component){
  render(){
    return(
      <div>
        <table>
          <tr>
            <th>Item name</th>
            <th>Cateogry_id</th>
            <th>Item_id</th>
          </tr>
          {this.props.item_list.map(
              function (item){
                return (
                  <tr>
                    <td><p>{item["name"]}</p></td>
                    <td><p>{item["category_id"]}</p></td>
                    <td><p>{item["_id"]}</p></td>
                    <td><Link to={function(){return "/item/edit/"+item['_id']}}>Edit</Link></td>
                  </tr>)
                })}
        </table>
      </div>
    )
  }
}

export default Items;
