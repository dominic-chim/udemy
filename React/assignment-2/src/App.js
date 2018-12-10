import React, { Component } from 'react';
import './App.css';
<<<<<<< HEAD
import UserInput from './components/UserInput'
import ValidateInput from './components/ValidateInput'
=======
import ValidationComponent from './components/ValidationComponent'
>>>>>>> 535c356d4c86e8061a5709aa19ce50b435c58abf
import CharComponent from './components/CharComponent'

class App extends Component {

  state = {
<<<<<<< HEAD
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

=======
    string:""
  }

  changeStringHandler = (event) =>{
    this.setState({
      string:event.target.value,
    })
  }

  deleteCharHandler = (index) =>{
    let text = [...this.state.string]
    text.splice(index,1);
    text = text.join('')
    this.setState({
      string:text
    })
  }

 

  render() {

    let Text = this.state.string
    const char =(
      Text.split('').map((char,index)=>{
        return <CharComponent 
          char={char}
          key={index}
          click={()=>this.deleteCharHandler(index)}
        />
        })
    )
    
    return (
      <div className="App">
        <ol>
          <li>Create an input field (in App component) with a change listener which outputs the length of the entered text below it (e.g. in a paragraph).</li>
          <li>Create a new component (=> ValidationComponent) which receives the text length as a prop</li>
          <li>Inside the ValidationComponent, either output "Text too short" or "Text long enough" depending on the text length (e.g. take 5 as a minimum length)</li>
          <li>Create another component (=> CharComponent) and style it as an inline box (=> display: inline-block, padding: 16px, text-align: center, margin: 16px, border: 1px solid black).</li>
          <li>Render a list of CharComponents where each CharComponent receives a different letter of the entered text (in the initial input field) as a prop.</li>
          <li>When you click a CharComponent, it should be removed from the entered text.</li>
        </ol>
        <p>Hint: Keep in mind that JavaScript strings are basically arrays!</p>
      <input type='text' onChange={this.changeStringHandler} value={this.state.string}/>
      <p>Text length is {this.state.string.length}</p>
      <ValidationComponent textLength={this.state.string.length}/>
      {char}
>>>>>>> 535c356d4c86e8061a5709aa19ce50b435c58abf
      </div>
    );
  }
}

export default App;
