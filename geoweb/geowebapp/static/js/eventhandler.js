function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
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

function getSensorByName() {
    var dropdown = document.getElementById('dropdwn');
    if (!dropdown) return;
    var sensorCode = dropdown.value;
    console.log("Selected sensor from dropdown:", sensorCode);
    fetch("sensor/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: `sensor_name=${sensorCode}`
    })
        .then(response => response.json())
        .then(json => {
            console.log("Response from server:", json);
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

function getSensorByClick(e) {
    console.log(e.target);
    var coords = e.target.getLatLng();
    var tooltip = e.target.getTooltip();
    var popup = e.target.getPopup();

    var sensorName = '';
    if (tooltip) {
        var content = tooltip.getContent();
        if (typeof content === 'string') {
            // Parse HTML string to extract text content only
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = content;
            sensorName = tempDiv.textContent.trim();
        } else if (content && content.textContent) {
            sensorName = content.textContent.trim();
        } else if (content && content.innerHTML) {
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = content.innerHTML;
            sensorName = tempDiv.textContent.trim();
        }
    }
    console.log("Clicked sensor:", sensorName, "at", coords);
    fetch("sensor/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: `latitude=${coords.lat}&longitude=${coords.lng}&sensor_name=${sensorName}`
    })
        .then(response => response.json())
        .then(json => {
            var serverData = JSON.stringify(json);
            console.log("Response from server:", serverData);
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


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                // Update the coordinates display
                const coordinatesDiv = document.getElementById('coordinates');
                if (coordinatesDiv) {
                    coordinatesDiv.textContent = `Lat: ${position.coords.latitude.toFixed(3)}, Lng: ${position.coords.longitude.toFixed(3)}`;
                }

                // Send precise client-side coordinates to the server
                const csrftoken = getCookie('csrftoken');
                console.log('position:', position);
                console.log('Sending location:', position.coords.latitude, position.coords.longitude, csrftoken);

                fetch("user-location/", {
                    method: 'POST',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrftoken
                    },
                    body: `latitude=${position.coords.latitude}&longitude=${position.coords.longitude}&timestamp=${position.timestamp}`
                })
                    .then(response => response.json())
                    .then(data => console.log('Location stored:', data))
                    .catch(error => console.error('Error storing location:', error));
            },
            function (error) {
                // On error, fallback to IP-based location
                fetch("location-from-ip/")
                    .then(response => response.json())
                    .then(data => {
                        console.log('Fallback location (IP-based):', data.location);
                    });
            }
        );
    } else {
        // Browser doesn't support geolocation – fallback immediately
        fetch("location-from-ip/")
            .then(response => response.json())
            .then(data => {
                console.log('Fallback location (IP-based):', data.location);
            });
    }
}