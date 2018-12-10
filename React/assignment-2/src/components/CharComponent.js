import React from 'react'
import './UserIO.css'
import UserInput from'./UserInput'


const charcomponent = (props) => {
    return(
        <div className="CharComponent">
            <UserInput change = {props.change}/>
            <p onClick={props.click}>Output Username:{props.username}</p>
        </div>
    )
}

export default charcomponent