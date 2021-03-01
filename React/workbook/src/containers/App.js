import React, { Component } from 'react';
import Cockpit from '../components/Cockpit/Cockpit';
import Persons from '../components/Persons/Persons';
import classes from './App.css'

class App extends Component {

  constructor(props) {
    super(props);
    console.log("'[App.js] constructor")
  }

  state = {
    persons:[
      {id:'123',name:'david',age:21},
      {id:'234',name:'bob',age:18},
      {id:'345',name:'mary',age:23},
      {id:'567',name:'zack',age:30}
    ],
    otherState:'some other value',
    showPersons:false
  }

  static getDerivedStateFromProps(props, state) {
    console.log("'[App.js] getDerivedStateFromProps",props);
    return state;
  }

  componentDidMount(){
    console.log("'[App.js] componentDidMount");
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

    this.setState( { persons:persons } )
  }

  deletePersonHandler = (personIndex) =>{
    const persons = [...this.state.persons]
    persons.splice( personIndex, 1 );
    this.setState({ persons:persons } );
  }

  togglePersonsHandler = () =>{
    const doeShow = this.state.showPersons;
    this.setState( { showPersons: !doeShow } )
  }

  render() {
    console.log("'[App.js] render");
    let persons = null;
    
    
    if (this.state.showPersons ){
      persons = (
          <Persons persons={this.state.persons}
          clicked = {this.deletePersonHandler}
          changed = {this.handleChangeHandler} />
      );

    }
    return (
      <div className = {classes.App}>
        <Cockpit 
        persons = {this.state.persons}
        showPersons = {this.showPersons}
        clicked = {this.togglePersonsHandler}/>
        {persons}
      </div>
    )
  }
}

export default App;
