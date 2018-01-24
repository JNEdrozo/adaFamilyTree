
$(document).ready(function () {
  $('#sidebarCollapse').on('click', function() {
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active')

  });

  $('.member-close-btn').on('click', function() {
    $('.member').toggleClass('hidden');
  });

  $('#night-option').click(function() {
    $('body').toggleClass('night-mode');
    $('.head-nav').toggleClass('night-mode-header');
    // $('#button#sidebarCollapse.navbar-btn').toggleClass('sidebarCollapse-btn-night-mode');

  });


});
