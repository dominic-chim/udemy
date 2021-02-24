import React from 'react';
import classes from './Person.css'
const persons =(props)=>{

    return(
        <div className = {classes.Persons}>
            <p onClick={props.click}> My name is {props.name}, I am {props.age} years old</p>
            <p>{props.children}</p>
            <input type='text' onChange={props.changed} value={props.name}/>
        </div>
    )
}

export default persons