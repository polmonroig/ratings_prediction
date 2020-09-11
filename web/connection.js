

function make_prediction(){

    textarea = document.getElementById('reviewArea')
    text = textarea.value;
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('ratingText').innerHTML = "Rating: " + this.responseText;

        }
    };
    xhr.open("POST", "http://127.0.0.1:5000/api", true);

    xhr.setRequestHeader("Content-type", "text/plain");
    xhr.send(text);

}
