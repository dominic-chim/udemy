import React from 'react';
import classes from './Cockpit.css'
import logo from '../../assets/logo.svg';

const cockpit = (props) => {
    let btnClass = '';

    if (props.showPerson)
    {
        btnClass = classes.red;
    }
    
    const assignedClasses =[]
    if(props.persons.length <=2){
      assignedClasses.push(classes.red);
    }
    if(props.persons.length<=1){
      assignedClasses.push(classes.bold);
    }

    return (
        <div className={classes.Cockpit}>
            <header className="header">
                <img src={logo} className="Cockpit-logo" alt="logo" />
                <h1 className={assignedClasses.join(' ')}>React App Workbook</h1>
            </header>
            <button 
            className={btnClass} 
            onClick={props.clicked}>Show/Hide Persons</button>
           
        </div>
    );
};

export default cockpit;