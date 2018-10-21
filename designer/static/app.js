//var $ = require('jquery');

$(document).ready(function () {
  $('.cword-cell').keyup(function(data) {
    if (data.currentTarget.value == "") { 
      $(this).removeClass('has-content');
      console.log('empty');
    } else if (data.currentTarget.value == " ") {
      $(this).addClass('filled');
      console.log('space');
    } else {
      $(this).addClass('has-content');
      $(this).removeClass('filled');
      console.log('content');
    }
    console.log(data.which);

    if (true) {  //if (data.currentTarget.value != "") {
      console.log('motion');
      var coords = $(this).attr('id').split('-');
      
      var newX = parseInt(coords[0]) + (data.which == "8" ? -1 : 1);
      var newY = parseInt(coords[1]);
      console.log(coords + " " + newX + " " + newY);
      $('input#' + newX + "-" + newY).focus();
    }
  })


});

function showAlert(msg) {
  alert('an important message: ' + msg);
};
