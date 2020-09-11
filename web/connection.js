

function make_prediction(){
    // get current written text
    textarea = document.getElementById('reviewArea')
    text = textarea.value;
    // create ajax connection
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // update rating value 
            document.getElementById('ratingText').innerHTML = "Rating: " + this.responseText;
        }
    };
    xhr.open("POST", "http://127.0.0.1:5000/api", true);
    xhr.setRequestHeader("Content-type", "text/plain");
    xhr.send(text);

}
