import React, { Component } from 'react';
import './App.css';
import UserInput from './components/UserInput'
import ValidateInput from './components/ValidateInput'
import CharComponent from './components/CharComponent'

class App extends Component {

  state = {
      details:{
        userName:'default',
        userLength:0,
      },
    showForm: false
  }

  changeUsernameHandler = (event) =>{
    const detail = {...this.state.details}

    detail.userName = event.target.value
    detail.userLength = detail.userName.length
    
    this.setState({
      userName:detail.userName,
      userLength:detail.userLength
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
      const string = this.state.details.userName.split("")
      console.log(string)
      form=(
        <div >
          <UserInput change={this.changeUsernameHandler} userLength={this.state.userLength} />
          <ValidateInput userLength={this.state.userLength}/>
          {
            string.map((char,index)=>{
              return(
                <CharComponent 
                  character= {char}
                  
                />
              )
            })
          }
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
