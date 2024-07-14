const minus = document.querySelector(".infoHead");
const text = document.querySelector(".mentor");
const minusImg = document.getElementById("minus");
const minus2 = document.querySelector(".priceHead");
const text2 = document.querySelector(".offers");
const minusImg2 = document.getElementById("minus2");

let open = true;
minus.addEventListener("click", function() {
    if (open) {
        text.classList.add('hidden');
        minus2.classList.add('down');
        text2.classList.add('downText');
        minusImg.src = 'assets/images/icon-plus.svg';
    } else {
        text.classList.remove('hidden');
        minus2.classList.remove('down');
        text2.classList.remove('downText');
        minusImg.src = 'assets/images/icon-minus.svg';
    }
    open = !open;
});

let open2 = false;
minus2.addEventListener("click", function() {
        if (open2) {
            text2.classList.remove('open2');
            text2.classList.remove('open');
            minusImg2.src = 'assets/images/icon-plus.svg';
        } else {
            if (open) {
                text2.classList.add('open2');
            } else {
                text2.classList.add('open');
            }
            minusImg2.src = 'assets/images/icon-minus.svg';
        }
        open2 = !open2;
});


