import React from 'react';
import Radium from 'radium'

const persons =(prop)=>{

    const style = {
        '@media (min-width:500px)':{
            width:'450px'
        }
    }

    return(
        <div className = "Persons" style={style}onClick={prop.click}>
            <p>My name is {prop.name}, I am {prop.age} years old</p>
            <input type='text' onChange={prop.change} value={prop.name}/>
        </div>
    )
}

export default Radium(persons)