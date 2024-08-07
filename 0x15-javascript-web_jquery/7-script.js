// Fetches and replaces the name of the API data then replaces the name
// of the character in the DIV#character tag text

$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
  });
});

