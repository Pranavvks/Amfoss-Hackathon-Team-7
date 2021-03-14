// 1. Show progress
// 2. Show % of completion in text
// 3 . Color,width 4. Use html <progress>
 import React from "react" ;
 import PropTypes from "prop-types" ;
 const ProgressBar = props =>
 {
     const {value , max} = props ;
     return <progress value = {value} max={max} />;

 };
 ProgressBar.propTypes = {
     value : PropTypes.number.isRequired ,
     max : PropTypes.number 
 };
 ProgressBar.defaultProps = {
     max : 100
 }
 export default ProgressBar ;