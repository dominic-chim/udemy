import React from 'react'
import './UserIO.css'
import UserInput from'./UserInput'


const useroutput = (props) => {
    return(
        <div className="UserOutput">
            <UserInput change = {props.change}/>
            <p onClick={props.click}>Output Username:{props.username}</p>
        </div>
    )
}

export default useroutput