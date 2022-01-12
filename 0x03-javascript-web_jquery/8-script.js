$(document).ready(() => {
  jQuery.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (res) => {
    console.log(res);
    for (mv of res.results) {
      $('#list_movies').append('<li>' + mv.title + '</li>');
    }
  });
});
