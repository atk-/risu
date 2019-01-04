var move = function (focused, dx, dy) {
  var coords = focused.attr('id').split('-');
  var newX = parseInt(coords[0]) + dx 
  var newY = parseInt(coords[1]) + dy;
  $('input#' + newX + '-' + newY).focus();
}

$.across = function () {
  return $('select#id_direction').val() == 0;
}

$.down = function () {
  return !$.across();
}

$.moveToNext = function () {
  var focused = $('input:focus');
  if ($.across()) {
    move(focused, 1, 0);
  } else {
    move(focused, 0, 1);
  }
}

$.moveToPrevious = function () {
  var focused = $('input:focus');
  if ($.across()) {
    move(focused, -1, 0);
  } else {
    move(focused, 0, -1);
  }
}

$.selectCell = function (x, y) {
  var coord = "" + x + "-" + y;
  $('input#' + coord).focus();
}

$.where = function () {
  var ret = $('input:focus').attr('id').split('-');
  return [parseInt(ret[0]), parseInt(ret[1])];
}

$.serialize = function () {
  return "foobar";
}

var keyhandler = function(event) {
  var key = event.which;
  console.log('wrapper caught key ' + event.which);
  var focused = $('input:focus');
  switch (event.which) {
    case 8:     // BACKSPACE
      focused.val('');
      focused.removeClass('filled');
      focused.removeClass('has-content');
      $.moveToPrevious();
      break;

    case 9:     // TAB -- change input direction
      var dirselect = $('select#id_direction');
      dirselect.val(parseInt(dirselect.val()) ^ 1);
      focused.focus();
      event.preventDefault();
      event.stopPropagation();
      break;

    case 13:    // ENTER -- move to beginning of next row/column
      event.preventDefault();
      if ($.across()) {
        var now = $.where();
        console.log(now);
        $.selectCell(1, now[1] + 1);
      } else {
        var now = $.where();
        console.log(now);
        $.selectCell(now[0] + 1, 1);
      }

      $.ajax({
        url: '/designer/ajax/collect_words/',
        data: $(this).serialize(),
        success: function(data) {
          console.log('ajax ' + data);
        }
      });
      break;

    case 35:    // END
      // TODO this goes to end of column/row depending on direction
      break;

    case 36:    // HOME
      // TODO go to beginning of column/row depending on direction
      $.selectCell(1, 1);
      break;

    case 37:    // LEFT
      move(focused, -1, 0);
      break;
      
    case 38:    // UP
      move(focused, 0, -1);
      break;

    case 39:    // RIGHT
      move(focused, 1, 0);
      break;

    case 40:    // DOWN
      move(focused, 0, 1);
      break;

    case 46:    // DELETE
      focused.val('');
      focused.removeClass('filled');
      focused.removeClass('has-content');
      break;

    case 75:    // ALT-K
      if (event.altKey) {
        if (focused.hasClass('picture-word')) {
          focused.removeClass('picture-word');
        } else {
          focused.addClass('picture-word');
        }
      }
  }
}

$(document).ready(function () {
  $('div#wordgrid').keydown(keyhandler);

  $('.cword-cell').on('input', function(data) {
    if (data.currentTarget.value == "") { 
      $(this).removeClass('has-content');
    } else if (data.currentTarget.value == " ") {
      $(this).addClass('filled');
      $.moveToNext();
    } else {
      $(this).addClass('has-content');
      $(this).removeClass('filled');
      $.moveToNext();
    }
  })
});

function showAlert(msg) {
  alert('an important message: ' + msg);
};
