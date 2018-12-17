import React from 'react';
import classes from '../App.css'
const persons =(prop)=>{

    return(
        <div className = {classes.Persons} onClick={prop.click}>
            <p>My name is {prop.name}, I am {prop.age} years old</p>
            <input type='text' onChange={prop.change} value={prop.name}/>
        </div>
    )
}

export default persons