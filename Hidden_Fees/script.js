document.getElementById('pdfForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('pdfInput');
    const file = fileInput.files[0];
    const messageDiv = document.getElementById('message');
    console.log('I was called')
    
    if (file && file.type === 'application/pdf') {
        const formData = new FormData();
        formData.append('file', file);
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Append the new message to the existing content
            messageDiv.innerHTML += '<p>' + data.message + '</p>';
            fileInput.value = ''; // Clear the file input
        })
        .catch(error => {
            messageDiv.innerHTML += '<p>Error: ' + error + '</p>';
        });
    } else {
        alert('Please select a PDF file');
    }
});
//         try {
//             const response = await fetch('/upload', {
//                 method: 'POST',
//                 body: formData
//             });
//             const data = await response.json();
//             if (response.ok) {
//                 // Display success message
//                 messageDiv.textContent = 'File uploaded successfully: ' + data.message;
//             } else {
//                 // Display error message
//                 messageDiv.textContent = 'Error uploading file: ' + data.message;
//             }
//         } catch (error) {
//             // Display network error
//             messageDiv.textContent = 'Network error: ' + error;
//         }

//         // Clear the file input so another file can be selected
//         fileInput.value = '';
//     } else {
//         alert('Please select a PDF file');
//     }
// });




// function handlePDFUpload(event) {
//     const file = event.target.files[0];
//     console.log(file)
//     if (file) {
//         // Create a FormData object to hold the file
//         const formData = new FormData();
//         formData.append('file', file);
//         console.log(formData)
//         // Send the file to the Flask backend
//         fetch('/upload', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 console.log(data.message);
                
//                 // Display a preview of the uploaded PDF
//                 const objectURL = URL.createObjectURL(file);
//                 const iframe = document.createElement('iframe');
//                 iframe.src = objectURL;
//                 iframe.width = '100%';
//                 iframe.height = '500px';
//                 document.body.appendChild(iframe);
//             } else {
//                 console.error(data.error);
//             }
//         })
//         .catch(error => {
//             console.error("Error uploading the file:", error);
//         });
//     }
// }