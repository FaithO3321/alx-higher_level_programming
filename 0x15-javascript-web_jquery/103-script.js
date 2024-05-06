$(document).ready(function() {
    // Function to fetch and display translation
    function fetchTranslation() {
      var languageCode = $('#language_code').val();
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        data: { lang: languageCode },
        method: 'GET',
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function(xhr, status, error) {
          console.error('Error fetching translation:', error);
        }
      });
    }
  
    // Event handler for button click
    $('#btn_translate').click(fetchTranslation);
  
    // Event handler for Enter key press in input field
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // Enter key code
        fetchTranslation();
      }
    });
  });

