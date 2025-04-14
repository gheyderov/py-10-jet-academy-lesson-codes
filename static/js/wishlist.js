let deleteBtns = document.getElementsByClassName('delete-from-wishlist')

for (let i = 0; i < deleteBtns.length; i ++){
    deleteBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        let item = deleteBtns[i].dataset.item
        let url = `${location.origin}/en/api/wishlist/${item}/`
        console.log('item deleted')
        console.log(item)
        fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : csrftoken
            }
        })
        // .then((data) => {
        //     location.reload()
        // })

    })
}