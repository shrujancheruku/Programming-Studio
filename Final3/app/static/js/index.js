// v3.1.0
//Docs at http://simpleweatherjs.com
$(document).ready(function() {
  $.simpleWeather({
    location: 'Champaign, IL',
    woeid: '2377942',
    unit: 'f',
    success: function(weather) {
      html = '<h2><i class="icon-'+weather.code+'"></i> '+weather.temp+'&deg;'+weather.units.temp+'</h2>';
      html += '<ul><li><b>'+weather.city+', '+weather.region+'</b></li>';
      html += '<li class="currently"><b>'+weather.currently+'</b></li>';

      $("#weather").html(html);
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });
});