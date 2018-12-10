<<<<<<< HEAD
import React from 'react'
import './UserIO.css'
import UserInput from'./UserInput'


const charcomponent = (props) => {
    return(
        <div className="CharComponent">
            <UserInput change = {props.change}/>
            <p onClick={props.click}>Output Username:{props.username}</p>
=======
import React from 'react';

const charcomponent = (props) =>{

    const style = {
        display: 'inline-block',
        padding: '16px',
        textAlign: 'center',
        margin: '16px',
        border: '1px solid black'
    }
    
    return(
        <div className="CharComponent" style={style}>
            <p onClick={props.click}>{props.char}</p>
>>>>>>> 535c356d4c86e8061a5709aa19ce50b435c58abf
        </div>
    )
}

export default charcomponent