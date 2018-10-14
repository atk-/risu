$(function() {
  $('h4').onclick = function() {
    console.log('clicked!');
  }

  $('h4').hidden = true;

  clickme = function () {
    console.log('I tickle!');
  }
});

function showAlert(msg) {
  alert('an important message: ' + msg);
};

$(":button").onclick = function () { showAlert('clicked'); };
