let form = document.getElementById('login-form')

form.addEventListener('submit',(e) => {
    e.preventDefault()
    //console.log("form was submitted")
    let formdata = {
        'username':form.username.value,
        'password':form.password.value
    }

    //console.log("Form Data :",formdata)
    fetch('http://127.0.0.1:8000/api/users/token/',{
        method:'POST',
        headers:{
            'Content_Type':'application/json',
        },
        body:JSON.stringify(formdata)
    })
    .then(response => response.json())
    .then(data => {
        console.log('DATA :',data)
        if(data.access){
            localStorage.setItem('token',data.access)
            window.loacation = 'file:///C:/Users/Sumit/Desktop/FRONTEND/projects-list.html'
        }
        else{
            alert("Username or Password didnt work")
        }
    })
})