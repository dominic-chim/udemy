import React from 'react'
import './UserIO.css'

const validateinput = (props) => {
    return(
        <div className="ValidateInput">
            {props.userLength<5? <p>String too short</p>:""}
            {props.userLength>12? <p>String too long</p>:""}
        </div>
    )
}

export default validateinput