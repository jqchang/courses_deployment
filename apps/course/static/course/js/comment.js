$(document).ready(function() {
  // Add listener for "delete" button click
  // Append a form to parent td to allow for comment deletion
  $(document).on("click", "button", function() {
    if($(this).attr("active") == "false") {
      var csrf = $(this).parent().children("input[name='csrfmiddlewaretoken']").val()
      $(this).parent().html("Deletion pw:<input type='password' name='password'><input type='hidden' name='csrfmiddlewaretoken' value='"+csrf+"'><input type='submit' value='Delete'>");
      $(this).attr("active", "true");
    }
  });
});
