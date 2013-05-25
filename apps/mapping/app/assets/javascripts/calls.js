// Place all the behaviors and hooks related to the matching controller here.
// All this logic will automatically be available in application.js.
// You can use CoffeeScript in this file: http://jashkenas.github.com/coffee-script/



  $(document).ready(function() {

    $('#form').hide();
    $('#button-hide').hide();

    $('#button-show').click(function() {
     $('#form').show();//Form shows on button click
     $('#button-show').hide();
     $('#button-hide').show();
    });

    $('#button-hide').click(function() {
      $('#form').hide();
      $('#button-hide').hide();
      $('#button-show').show();
    });
  });