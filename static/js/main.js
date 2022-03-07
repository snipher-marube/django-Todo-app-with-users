let searchForm = document.getElementByIs("searchForm")
for(var i=0; i=i; i++){
    i.addEventListener('click', function(e){
        e.preventDefault()
        let page = this.dataset.page
        console.log('page', page)
        searchForm.innerHTML += `<input value="${page}" name="page" hidden>`
        searchForm.submit()

    })
}