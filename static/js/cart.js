let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i ++){
    updateBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        productId = this.dataset.product
        action = this.dataset.action
        
        if (user == 'AnonymousUser'){
            console.log('User not found!')
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function updateUserOrder(productId, action){
    console.log(`The user is ${user}. Sending data...`)

    let url = '/en/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({'productId' : productId, 'action' : action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    })
}