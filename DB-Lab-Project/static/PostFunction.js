function sendPost(formID)
        {
            let form = document.forms[formID];
            let formData = new FormData(form);
            let formDataObject = Object.fromEntries(formData.entries());
            let data = JSON.stringify(formDataObject);

            let xhr = new XMLHttpRequest();
            let url = form.action; 
            xhr.open("POST", url);
            xhr.setRequestHeader("Accept", "application/json");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = () => console.log(xhr.responseText);
            
            
            xhr.send(data);
        }