const arrownext = document.getElementsByClassName('arrownext')
const arrowback = document.getElementsByClassName('arrowback')
const cards = document.getElementsByClassName('cards')
const card = document.getElementsByClassName('card')
const navbar = document.getElementById("navbar");

function showArrow (x){
    var index = x.id
    arrownext[index].style.cssText = `opacity: 1; transform: scale(1);`
    arrowback[index].style.cssText = `opacity: 1; transform: scale(1);`
}

function hideArrow(x){
    var index = x.id
    arrownext[index].style.cssText = `opacity: 0; transform: scale(0);`
    arrowback[index].style.cssText = `opacity: 0; transform: scale(0);`
}

function scrollforward(x){
    var index = x.id
    cards[x.id].scrollBy({
        left: card[0].offsetWidth,
        behavior: 'smooth'
    })
}

function scrollbackward(x){
    var index = x.id
    cards[x.id].scrollBy({
        left: -card[0].offsetWidth,
        behavior: 'smooth'
    })
}

function openmore(x){
    window.open(`./pics/${x.id}/main.png`, "_self")
}