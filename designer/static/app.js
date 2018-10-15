$(document).ready(function () {
  $('.cword-cell').keyup(function(data) {
    if (data.currentTarget.value == "") { 
      $(this).removeClass('has-content');
      console.log('added');
    } else if (data.currentTarget.value == " ") {
      $(this).addClass('filled');
      console.log('filled');
    } else {
      $(this).addClass('has-content');
      $(this).removeClass('filled');
      console.log('removed');
    }
  })
});

function showAlert(msg) {
  alert('an important message: ' + msg);
};
