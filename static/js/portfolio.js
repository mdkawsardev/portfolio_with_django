
// Portfolio page in dashboard, hint show hide
let triger = false;
let hint = document.querySelector('.hint');

hint.addEventListener('click',()=> {
    // document.querySelector('#c_hint').classList.add('d-none');
    console.log("clicked")
})
hint.onmouseenter = () => {
    
}
hint.onmouseleave = () => {
    document.querySelector('.showHint').style.visibility = "hidden";
}