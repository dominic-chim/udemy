import React, { Component } from 'react';
import logo from './logo.svg';
import classes from './App.css';

import Persons from './components/Person';


class App extends Component {
  state = {
    persons:[
      {id:'123',name:'david',age:21},
      {id:'234',name:'bob',age:18},
      {id:'345',name:'mary',age:23},
      {id:'567',name:'zack',age:30}
    ],
    showForm:true
  }

  handleChangeHandler =(event,index) =>{
    const personsIndex = this.state.persons.findIndex(p =>{
      return p.id === index
    })

    const person = {
      ...this.state.persons[personsIndex]
    }
    
    person.name = event.target.value

    const persons = [...this.state.persons]
    persons[personsIndex] = person

    this.setState({
       persons:persons
    })
  }

  toggleFormHandler = () =>{
    this.setState({
      showForm: !this.state.showForm
    })
  }

  deleteDetailHandler = (personIndex) =>{
    const persons = [...this.state.persons]
    persons.splice(personIndex,1)
    this.setState({
      persons:persons
    })
  }

  render() {

    let form = null
    
    if(this.state.showForm){
      form = (
        <div>
        {this.state.persons.map((person,index)=>{
          return <Persons 
            name = {person.name}
            age = {person.age}
            key = {person.id}
            change = {(event)=>this.handleChangeHandler(event,person.id)}
            click={()=>this.deleteDetailHandler(index)}
          />
        })}
        </div>
      )
    }

    const assignedClasses =[]
    if(this.state.persons.length <=2){
      assignedClasses.push(classes.red);
    }
    if(this.state.persons.length<=1){
      assignedClasses.push(classes.larger);
    }
    
    return (
      <div className={classes.App}>
        <header className="header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className={assignedClasses.join(' ')}>React App Workbook</h1>
        </header>
        <button onClick={this.toggleFormHandler}>Show/Hide Form</button>
        {form}
      </div>
    );
  }
}

export default App;
