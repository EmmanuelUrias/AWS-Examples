console.log("Bucket request works")

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

postData('https://hoqksv3pfa.execute-api.us-east-1.amazonaws.com/test/hello', { answer: 42 })
.then(data => {
  console.log(data); // JSON data parsed by `response.json()` call
})
.catch(error => {
  console.error('Error:', error);
});