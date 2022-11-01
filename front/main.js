var glass, w, h, bw;
let flag = true;
let flag_res = true;
glass = document.createElement("DIV");

async function loupe() {

    document.getElementById("photo").src = "images/photo.jpg";
    img = document.getElementById("photo");
    flag_res = true;
    magnify(img, 5)

}

async function camera() {

    await eel.click(Number(0))();
    document.getElementById("photo").src = "images/photo.jpg";

    document.getElementById('text_change').innerHTML = 'Сыыыр!';
    if (flag_res) {
        location.reload();
        glass.remove();
        flag = !flag;
        flag_res = !flag_res;
    }
}

async function pars() {



    document.getElementById('text_change').innerHTML = 'Думкаю';
    await eel.go()();
    document.getElementById("photo").src = "images/photo.jpg";
    document.getElementById("gcode").src = "comand/gcode.txt";
    if (flag_res) {
        location.reload();
        glass.remove();
        flag = !flag;
        flag_res = !flag_res;
    }
}

async function start() {

    location.reload();
    glass.remove();
    flag = !flag;


    document.getElementById('text_change').innerHTML = 'Запускаю';

}


async function stop() {

    await eel.apdate()();

    document.getElementById("photo").src = "images/photo.jpg";
    document.getElementById("gcode").src = "comand/gcode.txt";
    document.getElementById('text_change').innerHTML = 'Торможу всё';
    if (flag_res) {
        location.reload();
        glass.remove();
        flag = !flag;
        flag_res = !flag_res;
    }
}

setInterval(function() {
    var cd = new Date();
    var clockdat = document.getElementById("clockdat");
    clockdat.innerHTML = cd.toLocaleTimeString();
}, 1000);

function magnify(img, zoom) {


    glass.setAttribute("class", "img-magnifier-glass");
    if (flag) {

        glass.style.backgroundImage = "url('images/lupe_0.jpg')";
    } else {

        glass.style.backgroundImage.removeChild = "url('images/lupe_1.jpg')";
        glass.style.backgroundImage = "url('images/lupe_1.jpg')";
    }


    /*создать увеличительное стекло:*/

    /*вставить увеличительное стекло:*/
    img.parentElement.insertBefore(glass, img);
    /*установите свойства фона для увеличительного стекла:*/

    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;
    /*выполните функцию, когда кто-то перемещает лупу по изображению:*/
    glass.addEventListener("mousemove", moveMagnifier);
    img.addEventListener("mousemove", moveMagnifier);
    /*а также для сенсорных экранов:*/
    glass.addEventListener("touchmove", moveMagnifier);
    img.addEventListener("touchmove", moveMagnifier);

    function moveMagnifier(e) {
        var pos, x, y;

        /*предотвратите любые другие действия, которые могут произойти при перемещении по изображению*/
        e.preventDefault();
        /*получить позиции курсора x и y:*/
        pos = getCursorPos(e);
        x = pos.x;
        y = pos.y;
        /*не допускайте размещения увеличительного стекла вне изображения:*/
        if (x > img.width - (w / zoom)) {
            x = img.width - (w / zoom);
        }
        if (x < w / zoom) {
            x = w / zoom;
        }
        if (y > img.height - (h / zoom)) {
            y = img.height - (h / zoom);
        }
        if (y < h / zoom) {
            y = h / zoom;
        }
        /*установите положение увеличительного стекла:*/
        glass.style.left = (x - w) + "px";
        glass.style.top = (y - h) + "px";
        /*покажите что такое лупа:*/
        glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
    }

    function getCursorPos(e) {

        var a, x = 0,
            y = 0;
        e = e || window.event;
        /*получить x и y позиции изображения:*/
        a = img.getBoundingClientRect();
        /*вычислите координаты курсора x и y относительно изображения:*/
        x = e.pageX - a.left;
        y = e.pageY - a.top;
        /*рассмотрим любую прокрутку страницы:*/
        x = x - window.pageXOffset;
        y = y - window.pageYOffset;
        return {
            x: x,
            y: y
        };
    }
}