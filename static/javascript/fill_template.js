const xhttp = new XMLHttpRequest;

xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const server_response = JSON.parse(xhttp.responseText);
    
    for (var i = 0; i < server_response['initial_answers'].length; i++) {
      const initial_answer_element = document.getElementById("initial_answer_" + (i + 1));
      const meta_error_element = document.getElementById("meta_error_" + (i + 1));
      
      initial_answer_element.innerHTML = server_response["initial_answers"][i];
      
      if (meta_error_element != null) {
        meta_error_element.innerHTML = server_response["meta_errors"][i];
      }
    }
  }
}

xhttp.open("GET", "http://c1.elifast.com/get_responses?question_number=1");
xhttp.send();