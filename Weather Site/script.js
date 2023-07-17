
async function fetchWeather() {
    
    var city = document.querySelector(".search-bar").value

    const endpoint = new URL(`https://api.weatherapi.com/v1/current.json?`);
    endpoint.searchParams.set("key", "b7e3e6f838ac4b89a46185045230905");
    endpoint.searchParams.set("q", city|| "New York");
    const response = await fetch(endpoint);
    const data = await response.json();

    const { name, region } = data.location;
    const { icon } = data.current.condition;
    const { temp_c: temp } = data.current;
    const { text: description } = data.current.condition;
    const { humidity } = data.current;
    const { wind_kph: wind } = data.current;

    if (region != "") {
        document.querySelector(".city").innerHTML = "Weather in " + name + ", " + region
    }
    else {
        document.querySelector(".city").innerHTML = "Weather in " + name
    }
    document.querySelector(".temperature").innerHTML = temp + "°C";
    document.querySelector(".icon").src = icon;
    document.querySelector(".description").innerHTML = description;
    document.querySelector(".humidity").innerHTML = "Humididty: " + humidity + "%";
    document.querySelector(".wind").innerHTML = "Wind speed: " + wind + " km/h";
    document.querySelector(".weather").style.display = "block";
};


document.querySelector(".search-button").addEventListener("click", function() {
    fetchWeather();
});

document.querySelector(".search-bar").addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
    fetchWeather();
    }
});

fetchWeather();