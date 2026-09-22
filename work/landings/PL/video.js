$(document).ready(function () {
    // 1. Защита от многократного подключения.
    // В index.html js/video.js подключён три раза, из-за чего все обработчики
    // навешивались трижды, а таймер тикал втрое быстрее.
    if (window.__videoInit) { return; }
    window.__videoInit = true;

    var $video = $('#video');
    var $play = $('#play');
    var $popup = $('#popup');
    var $close = $('#close');
    var $order = $('#order');
    var $container = $('#container_video');

    if (!$video.length) { return; }

    // 2. Настройки берутся из инлайн-блока в index.html.
    // Раньше здесь стояли свои let start / let duration, которые перекрывали
    // значения из страницы: попап показывался на 1818-й секунде, то есть
    // после конца ролика, и до формы было не дойти.
    var tStart    = (typeof window.start    === 'number') ? window.start    : 120;  // когда показать попап
    var tDuration = (typeof window.duration === 'number') ? window.duration : 10;   // сколько попап висит
    var tShowForm = (typeof window.showForm === 'number') ? window.showForm : 600;  // когда открыть форму под видео

    var showPopup = false;
    var hidePopup = true;
    var showPlay = true;
    var orderShown = false;

    // Форма всегда стартует скрытой, даже если в CSS про неё забыли.
    $order.hide();

    $play.on('click', function () {
        window.scrollTo(0, 0);
        $play.fadeOut('fast', function () {
            $video.prop('muted', false).prop('currentTime', 0).trigger('play');
            $container.addClass('fullscreen');
            document.documentElement.classList.add('is-locked');
            $close.fadeIn();
            showPlay = false;
        });
    });

    $video.on('timeupdate', function () {
        var t = $(this).prop('currentTime');

        if (!orderShown && t >= tShowForm) {
            $order.fadeIn();
            orderShown = true;
        }
        if (!showPlay && !showPopup && t > tStart) {
            $popup.fadeIn('fast');
            showPopup = true;
        }
        if (hidePopup && t > tStart + tDuration) {
            $popup.fadeOut('fast');
            hidePopup = false;
        }
    });

    // 3. Три пути к форме, а был один.
    $video.on('ended', showOrder);   // досмотрел до конца
    $popup.on('click', showOrder);   // кликнул по попапу
    $close.on('click', showOrder);   // закрыл видео крестиком — раньше просто выходил из фуллскрина

    function showOrder() {
        $container.removeClass('fullscreen');
        $play.hide();
        $popup.fadeOut();
        $close.fadeOut();
        document.documentElement.classList.remove('is-locked');
        start_timer();

        $video.fadeOut('fast', function () {
            $(this).trigger('pause');
            $order.stop(true, true).fadeIn('fast', function () {
                $('html, body').animate({ scrollTop: $order.offset().top - 20 }, 200);
            });
        });
        orderShown = true;
    }
});

// 4. Таймер: защита от повторного запуска.
// Раньше при тройном подключении и при повторном вызове showOrder
// заводилось несколько интервалов и обратный отсчёт шёл в разы быстрее.
var time = 600;
var intr = null;

function start_timer() {
    if (intr) { return; }
    intr = setInterval(tick, 1000);
}

function tick() {
    time = time - 1;
    if (time < 0) { time = 0; }
    var mins = Math.floor(time / 60);
    var secs = time - mins * 60;
    if (mins === 0 && secs === 0) {
        clearInterval(intr);
        intr = null;
    }
    secs = secs >= 10 ? secs : "0" + secs;
    mins = mins >= 10 ? mins : "0" + mins;
    $("#min").html(mins);
    $("#sec").html(secs);
}
