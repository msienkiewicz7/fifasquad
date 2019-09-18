"use strict";

var format_input_value = function(event){
  var value = document.querySelector(".input-div input").value;
  if (!value) {
    return;
  }
  // remove dots from input
  value = value.replace(/\./g, '')
  // format dot output
  value = format_value(value)
  // replace input value with dot output
  document.querySelector(".input-div input").value = value;
}

var format_value = function(value){
  var f = new Intl.NumberFormat();
  return f.format(value)
}

var format_submit_value = function() {
  var value = document.querySelector(".input-div input").value;
  // remove dots from input
  value = value.replace(/\./g, '')
  document.querySelector(".input-div input").value = value;
  return true;
}

function test() {
  console.log("test");
}

const value_input = document.querySelector(".input-div input")
value_input.addEventListener('input', format_input_value)

const form = document.querySelector(".search-div form")
form.addEventListener('submit', format_submit_value)
