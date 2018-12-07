import React, { Component } from 'react';
import './App.css';
import UserInput from './components/UserInput'
import UserOutput from './components/UserOutput'

class App extends Component {

  state = {
    details: [
      {id:1,username:'Billy'},
      {id:2,username:'Bob'},
      {id:3,username:'Sarah'},
      {id:4,username:'Max'}
    ],
    showForm: false
  }

  changeUsernameHandler = (event,index) =>{
    const detailIndex = this.state.details.findIndex(p =>{
      return p.id === index
    })

    const detail = {
      ...this.state.details[detailIndex]
    }
    
    detail.username = event.target.value

    const details = [...this.state.details]
    details[detailIndex] = detail

    this.setState({
       details:details
    })
  }

  toggleFormHandler = () =>{
    this.setState({
      showForm: !this.state.showForm
    })
  }

  deleteDetailHandler = (detailIndex) =>{
    //const details = this.state.details.slice()
    const details = [...this.state.details]
    if(details.length >1){
      details.splice(detailIndex,1)
      this.setState({
        details:details
      })
    }
  }

  render() {

    let form=null
    if(this.state.showForm){
      form=(
        <div >
          {this.state.details.map((detail,index)=>{
            return (
              <UserOutput
                change={(event)=> this.changeUsernameHandler(event,detail.id)}
                key={detail.id} 
                username={detail.username} 
                click={()=>this.deleteDetailHandler(index)}
              />
            )
          })}
        </div>
      )
    }

    return (
      <div className="App">
        <h1>This is a React App</h1>
        <button onClick={()=>{this.toggleFormHandler()}}>Toggle Form</button>
        {form}

      </div>
    );
  }
}

export default App;
