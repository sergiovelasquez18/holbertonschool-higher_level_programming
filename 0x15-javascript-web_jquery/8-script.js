const $ = window.$;
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (response) {
    for (const i in response.results) { $('#list_movies').append('<li>' + response.results[i].title + '</li>'); }
  }
});
