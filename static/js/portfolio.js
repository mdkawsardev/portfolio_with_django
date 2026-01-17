
// Portfolio page in dashboard, hint show hide
let triger = false;
let hint = document.querySelector('.hint');

hint.onmouseenter = () => {
    document.querySelector('.showHint').style.visibility = "visible";
}
hint.onmouseleave = () => {
    document.querySelector('.showHint').style.visibility = "hidden";
}