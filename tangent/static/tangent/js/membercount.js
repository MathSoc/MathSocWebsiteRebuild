buttonLoading = false;

function loadSocMemberCount() {
	if (!buttonLoading) {
	 	buttonLoading = true;
	 	button = document.getElementById("socCountButton")
	 	button.innerHTML = "Loading";
	 	var xhttp = new XMLHttpRequest();
	  	xhttp.onreadystatechange = function() {
	    	if (this.readyState == 4 && this.status == 200) {
	     		document.getElementById("socCount").innerHTML = this.responseText;
	    	} else if (this.readyState == 4) {
	    		button.innerHTML = "Failed to get society member count";
	    		buttonLoading = false;
	    	}
	  	};
	  	url = button.getAttribute("data-ajax-target");
	  	xhttp.open("GET", url, true);
	  	xhttp.send();
	}
};