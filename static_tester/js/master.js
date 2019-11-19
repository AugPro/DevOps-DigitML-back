function upload() {
  document.getElementById('img-upload').click()
}

function predict(file) {
  let f = new FormData()
  f.append('img', file)
  fetch('http://192.168.99.100:8000/api/predict/', { // TODO: change api address in prod
    method: 'POST',
    body: f
  }).then(
    response => response.json() // if the response is a JSON object
  ).then(
    success => {console.log(success); document.getElementById('result').src = 'data:image/jpeg;base64,' + success['data']} // Handle the success response object
  ).catch(
    error => console.log(error) // Handle the error response object
  );
}
