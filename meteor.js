//Elmer Dea
//11/10/16
//window.addEventListener("load",readOut,false);
//function readOut(){document.getElementById("testOut").innerHTML = getData();}

var xhr = false;
//on load, creates new xhr for openWeather api


function getData()
{
	var nloc;
	xhr = new XMLHttpRequest();
	if (xhr) 
	{ 
				try 
				{
					xhr.open("GET", "https://data.nasa.gov/resource/y77d-th95.json");
					xhr.send();
				}
				catch (e) 
				{
					alert("t3");
				}	
	}
	//if ready and okay, parses xhr data via json
	xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        nloc = write(myArr);
    }
};
return nloc;
}

//creates string with text and json data for display



function write(w) 
{
	var loc = "[";
	for (i = 0; i < 50; i++)
	{	
	//{lat: -31.563910, lng: 147.154312}
		var lat = w[i].geolocation.coordinates[0];
		var lng = w[i].geolocation.coordinates[1];
		loc += "{lat: " + lat + ", lng: " + lng + "},"
	}
	loc = loc.substring(0, loc.length - 1);
	loc += "]";
    document.getElementById("testOut").innerHTML = loc;
	return loc;
}
	