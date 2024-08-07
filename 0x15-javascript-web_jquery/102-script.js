// Fetches and prints how to "Hello" depending on the language entered in the `INPUT#language_code` field when the user clicks the `INPUT#btn_translate` button.

$(document).ready(function() {
  $('#btn_translate').click(function() {
    const langCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
