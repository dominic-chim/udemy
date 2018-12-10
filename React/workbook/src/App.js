import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Radium, { StyleRoot } from 'radium';
import Persons from './components/Person';
import styled from 'styled-components';

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
    const style={
      backgroundColor:'green',
      color:'white',
      font: 'inherit',
      border: '1px solid blue',
      padding: '8px',
      cursor: 'pointer',
    }

    const Title = styled.h1`
      font-size: 1.5em;
      text-align: center;
      color: palevioletred;
    `;

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
      style[':hover']={
        backgroundColor: 'red',
        color: 'white'
      }
    }

    return (
      <StyleRoot>
        <div className="App">
          <header className="header">
            <img src={logo} className="App-logo" alt="logo" />
            <Title>React App Workbook</Title>
          </header>
          <button style={style} onClick={this.toggleFormHandler}>Show/Hide Form</button>
          {form}
        </div>
      </StyleRoot>
    );
  }
}

export default Radium(App);
