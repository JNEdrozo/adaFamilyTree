
$(document).ready(function () {
  $('#sidebarCollapse').on('click', function() {
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
  });

  $('#member-close-btn').on('click', function() {
    $('#member').toggleClass('hidden');
  });
});
