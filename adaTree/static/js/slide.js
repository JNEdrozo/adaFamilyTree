
$(document).ready(function () {
  $('#sidebarCollapse').on('click', function() {
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active')
    // $('.head-nav').toggleClass('head-nav-slide');

  });

  // $('.member-header').on('click', '.member-close-btn', function() {
  //   $('.member').toggleClass('hidden');
  // });

  $('.member-close-btn').on('click', function() {
    $('.member').toggleClass('hidden');
  });

  $('#night-option').click(function() {
    $('body').toggleClass('night-mode');
    // $('.head-nav').toggleClass('night-mode-header');
  });
  
});
