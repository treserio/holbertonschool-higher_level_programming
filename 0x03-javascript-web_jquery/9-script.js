$(document).ready(() => {
  jQuery.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (res) => {
    console.log(res);
    $('#hello').text(res.hello);
  });
});
