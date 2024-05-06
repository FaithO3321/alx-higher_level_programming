$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      success: function(response) {
        response.results.forEach(function(movie) {
          $('<li>').text(movie.title).appendTo('#list_movies');
        });
      },
      error: function(xhr, status, error) {
        console.error('Error fetching movies:', error);
      }
    });
  });
  
