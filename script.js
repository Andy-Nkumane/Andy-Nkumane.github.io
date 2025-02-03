// working on a way to not have the api key hidden and still without using modules
const API_KEY = "6c4366d9704b4d6bbd1111224250302";

// get user's location
function getLocation() { 
    if (navigator.geolocation) { 
        navigator.geolocation.getCurrentPosition(showPosition, showError); 
    } else { 
        console.error("Geolocation is not supported by this browser."); 
    } 
} 
 
function showPosition(position) { 
    const latitude = position.coords.latitude; 
    const longitude = position.coords.longitude; 
    console.log("Latitude: " + latitude + ", Longitude: " + longitude); 

    weather(latitude, longitude);
} 
 
function showError(error) { 
    switch(error.code) { 
        case error.PERMISSION_DENIED: 
            console.error("User denied the request for Geolocation."); 
            break; 
        case error.POSITION_UNAVAILABLE: 
            console.error("Location information is unavailable."); 
            break; 
        case error.TIMEOUT: 
            console.error("The request to get user location timed out."); 
            break; 
        case error.UNKNOWN_ERROR: 
            console.error("An unknown error occurred."); 
            break; 
    } 
} 

function weather(latitude, longitude) {
    console.log(`------- weather ${latitude} --------`);
    console.log("Latitude: " + latitude + ", Longitude: " + longitude);



    fetch(`http://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${latitude}, ${longitude}&aqi=no`, {
        "method": "GET",
        "headers": {}
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse the response data as JSON
        } else {
            throw new Error('API request failed');
        }
    })
    .then(data => {
        // Process the response data here
        console.log(data); 
        const weatherSection = document.getElementById("weather");
        const weatherDetailsDiv = document.getElementById("weather-details");
        weatherSection.innerHTML = `<p>Country: ${data.location.country} 
        <br> 
        City/Town: ${data.location.name}
        <br> 
        Region: ${data.location.region}
        <br> 
        Temperature: ${data.current.temp_c}
        <br> 
        Condtion: ${data.current.condition.text}
        <br> 
        Last updated: ${data.current.last_updated}</p>
        <img src=https:${data.current.condition.icon} alt=${data.current.condition.text}>`
        // weatherSection.innerHTML = `<ul>Country: ${data.current.condition.icon}</ul>`
        console.log(data.current.condition.icon);
        // console.log(console.log(data.current.condition.icon.slice(2)));
        console.log(data.current.condition.text);
    })
    .catch(error => {
        // Handle any errors here
        console.error(error); 
    });
}

window.onload = function() { 
    getLocation(); 
}; 