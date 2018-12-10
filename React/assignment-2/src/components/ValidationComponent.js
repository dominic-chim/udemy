import React from 'react';

const validationcomponent = (props) =>{
    let ValidationMsg= "Text long enough"

    if(props.textLength<5){
        ValidationMsg = "Text too short"
    }else if(props.textLength>12){
        ValidationMsg = "Text too long"
    }

    return(
        <div className="ValidationComponent" >
            {ValidationMsg}
        </div>
    )
}

export default validationcomponent