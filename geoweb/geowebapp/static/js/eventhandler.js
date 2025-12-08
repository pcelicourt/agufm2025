function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken'); 

function getSensor(e) {
     console.log(e.target);           
     var coords = e.target.getLatLng();
     var popup = e.target.getPopup();
     var data = popup.getContent().innerHTML.trim();                           

    // POST request using fetch()
    fetch("/", {

        // Adding method type
        method: "POST",
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        // Adding body or contents to send
        body: JSON.stringify({
            lat: coords.lat,
            lon: coords.lng,
            sensor_name: data
        }),

        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })

    // Converting to JSON
    .then(response => response.json())

    // Displaying results to console
    .then(json => {
        var serverData =  JSON.stringify(json); 
        //Here a placeholder plot is created based off data 
        //to be replaced with those from the server.... 
        var trace1 = {
           x: ['Category A', 'Category B', 'Category C'],
           y: [20, 14, 23],
           type: 'bar'
       };
       var data = [trace1];
       var layout = {
           title: 'Bar Chart using Plotly.js',
       }; 

        popup.setContent(
        //JSON.stringify(json)
            //'<iframe width=\"250\" height=\"150\"  frameborder=\"0\">'
           "<div id='sampleplot'></div>"
        );
        Plotly.newPlot('sampleplot', data, layout);   
      });                                              
}