let addToWishlist = document.getElementById('add-to-wishlist')
let url = `${location.origin}/en/api/wishlist/`
let productId = addToWishlist.dataset.product

window.addEventListener('load', async function (e) {
    let respose = await this.fetch(url)
    let responseData = await respose.json()
    
    for (let i = 0; i < responseData.length; i ++){
        if (productId == responseData[i].product){
            addToWishlist.style.color = 'red'
            break
        }
    }
})

addToWishlist.addEventListener('click', function(e){
    e.preventDefault()
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({'productId' : productId})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) =>{
        location.reload()
    })
    
})