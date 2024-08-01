document.getElementById('customForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const jobTitle = document.getElementById('jobTitle').value;
  });
  const subbutton = document.querySelector('#submit-Button');
  subbutton.addEventListener('click', function() {
    document.getElementById('first-page').style.display = 'none';
    document.getElementById('result').innerHTML = '';
    console.log('button has been clicked');
    console.log(document.getElementById('file-name').innerHTML)
    if (document.getElementById('file-name').innerHTML.trim() !== '') {
      document.getElementById('infoBox').style.display = 'block';
      this.disabled = true;
      console.log('file found')
      submitButton();
    }});
  function submitButton()
  {
    var fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function() {
      let base64data = reader.result.split(',')[1];
      sendDataToAPI(base64data);
    };
    reader.onerror = function(error) {
      console.log('Error: ', error);
    };}
  function sendDataToAPI(base64data) {
    let periodCount = 1;
    const updateCalculatingText = () => {
      if (document.getElementById('result').innerHTML.trim() === '') {
        let text = 'Calculating ';
        for (let i = 0; i < periodCount; i++) {
          text += '.';
        }
        document.getElementById('calculatingText').innerHTML = text;
        periodCount = (periodCount % 3) + 1;
      } else {
        document.getElementById('calculatingText').innerHTML = '';}};
    let intervalID = setInterval(updateCalculatingText, 500);
    console.log('about to fetch');
    fetch('https://z96gyadf7b.execute-api.us-east-1.amazonaws.com/fee-disclosure-stage/information', {
      method: 'POST',
      body: JSON.stringify({ file: base64data }),
      headers: {
        'Content-Type': 'application/json'}})
      .then(response => response.json())
      .then(data => {
      clearInterval(intervalID);
      document.getElementById('calculatingText').innerHTML = '';
      const amount = data['eventData']
      if(amount === 'Scanned PDF'){
        document.getElementById('first-page').style.display = 'block';
        document.getElementById('result').innerText = 'Error: Scanned PDF';  
        subbutton.disabled = false;}
      else{
          document.getElementById('customForm').style.display = 'block';
        const num = Number(amount)
        const formattedAmount = `$${num.toLocaleString('en-US', { minimumFractionDigits: 2 })}`;
        document.getElementById('result').innerText = formattedAmount;  
        subbutton.disabled = false;
      }})
      .catch(error => {
      document.getElementById('first-page').style.display = 'block';
      clearInterval(intervalID);
      document.getElementById('calculatingText').innerHTML = '';
      document.getElementById('result').innerText = 'Error';
      subbutton.disabled = false;});}
  function showFileName() {
    document.getElementById('infoBox').style.display = 'none';
    document.getElementById('result').innerHTML = '';
    var fileInput = document.getElementById('file');
    var fileNameDiv = document.getElementById('file-name');
    if (fileInput.files.length > 0) {
      var fileName = fileInput.files[0].name;
      fileNameDiv.innerHTML = '<strong>Selected file:</strong> ' + fileName;
    } else {
      fileNameDiv.innerHTML = 'No file selected';}}
  var dropArea = document.getElementById('drop-area');
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);});
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();}
  ['dragenter', 'dragover'].forEach(eventName => {dropArea.addEventListener(eventName, highlight, false);});
  ['dragleave', 'drop'].forEach(eventName => {dropArea.addEventListener(eventName, unhighlight, false);});
  function highlight() {dropArea.style.backgroundColor = '#f9f9f9';}
  function unhighlight() {dropArea.style.backgroundColor = '';}
  dropArea.addEventListener('drop', handleDrop, false);
  function handleDrop(e) {var dt = e.dataTransfer;
    var files = dt.files;
         document.getElementById('file').files = files;
    showFileName();}