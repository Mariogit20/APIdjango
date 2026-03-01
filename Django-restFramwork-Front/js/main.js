let apiProduit = async ()=>{
    try {
        let dataApi = await fetch('http://127.0.0.1:8000/produits/');       //         let dataApi = await fetch('http://127.0.0.1:8000/api/produits/');
        let dataJson = await dataApi.json()
        return dataJson
    } catch (error) {
        console.log(error)
    }
}


apiProduit().then(e =>{
    console.log(e);
    let card_containt = document.querySelector('.card-content')

    html_str = ''

    e.forEach((element,index) => {
        html_str +=`
            <div class="col-md-3">
                <div class="card" style="width: 18rem;">
                    <img src="${element.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${element.nom}</h5>
                      <p class="card-text">${element.description}</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
        `
    });
    card_containt.innerHTML = html_str
    
})

//////////////////////// apiSlider

let apiSlider = async ()=>{
    try {
        let dataApi = await fetch('http://127.0.0.1:8000/sliders/');       //         let dataApi = await fetch('http://127.0.0.1:8000/api/produits/');
        let dataJson = await dataApi.json()
        return dataJson
    } catch (error) {
        console.log(error)
    }
}


apiSlider().then(e =>{
    console.log(e);
    let slider_containt = document.querySelector('.slider-content')

    html_str = ''

    // e.forEach((element,index) => {
    //     html_str +=`
    //         <div class="col-md-3">
    //             <div class="card" style="width: 18rem;">
    //                 <img src="${element.image}" class="card-img-top" alt="...">
    //                 <div class="card-body">
    //                   <h5 class="card-title">${element.titre}</h5>
    //                   <p class="card-text">${element.description}</p>
    //                   <a href="#" class="btn btn-primary">Go somewhere</a>
    //                 </div>
    //               </div>
    //         </div>
    //     `
    // });

    e.forEach((element,index) => {    
        html_str +=`
              <div class="carousel-item">
                <img src="${element.image}" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                  <h5 class="text-dark">${element.titre}</h5>
                  <p>${element.description}</p>
                </div>
              </div>
        `
    });    

    slider_containt.innerHTML = html_str
    document.querySelectorAll('.carousel-item')[0].classList.add('active')
    
})

