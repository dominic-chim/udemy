import React from 'react'
import './UserIO.css'

const userinput = (props) => {
    return(
        <div className="UserInput">
            <input type="text" onChange={props.change} value = {props.username}></input>
        </div>   
    )
}

export default userinput