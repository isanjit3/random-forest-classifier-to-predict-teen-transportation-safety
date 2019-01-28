function riskRequest(){
  $.ajax(){
    url: "C:\Users\ronoy\Documents\Hackathon\python.py"
    success: function(response){
      handleResponse(response);
      alert("The code is running!");

    }
    return response;
  }
  alert(response);
}
