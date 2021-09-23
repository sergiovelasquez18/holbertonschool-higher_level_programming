const $ = window.$;
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (response) {
    $('DIV#hello').text(response.hello);
  }
});
