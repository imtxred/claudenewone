/* video.js — v2
   Три пути к форме: конец ролика, клик по попапу, крестик.
   Диагностика: открыть страницу с ?debug=1 — внизу появится чёрная плашка
   с логом, её видно без консоли разработчика. */

(function () {
    var DEBUG = /[?&]debug=1/.test(location.search);
    var box = null;

    function log(msg) {
        if (!DEBUG) { return; }
        if (!box) {
            box = document.createElement('div');
            box.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:2147483647;' +
                'background:#000;color:#0f0;font:12px/1.4 monospace;padding:6px;max-height:45vh;overflow:auto';
            (document.body || document.documentElement).appendChild(box);
        }
        box.innerHTML += msg + '<br>';
        if (window.console) { console.log('[video.js] ' + msg); }
    }
    window.__vlog = log;
})();

$(document).ready(function () {

    // 1. Защита от многократного подключения: в index.html js/video.js
    // подключён трижды, обработчики навешивались по несколько раз.
    if (window.__videoInit) { window.__vlog('повторное подключение video.js — пропущено'); return; }
    window.__videoInit = true;
    window.__vlog('video.js v2 запущен');

    var $video = $('#video');
    var $play = $('#play');
    var $popup = $('#popup');
    var $close = $('#close');
    var $order = $('#order');
    var $container = $('#container_video');

    window.__vlog('найдено: video=' + $video.length + ' play=' + $play.length +
        ' popup=' + $popup.length + ' close=' + $close.length + ' order=' + $order.length);

    if (!$video.length || !$order.length) {
        window.__vlog('НЕТ #video или #order — дальше идти некуда');
        return;
    }

    // 2. Настройки читаются из инлайн-блока index.html.
    // Раньше здесь стояли свои let start = 1818 и let duration = 5,
    // которые перекрывали значения со страницы.
    var tStart    = (typeof window.start    === 'number') ? window.start    : 120;
    var tDuration = (typeof window.duration === 'number') ? window.duration : 10;
    var tShowForm = (typeof window.showForm === 'number') ? window.showForm : 600;
    window.__vlog('настройки: start=' + tStart + ' duration=' + tDuration + ' showForm=' + tShowForm);

    var showPopup = false;
    var hidePopup = true;
    var showPlay = true;
    var orderShown = false;

    hideOrder();

    // 3. Принудительный показ формы поверх любых CSS-правил, включая !important.
    // На стенде форма не появлялась, если в style_3.css стояло
    // #order{display:none !important} или было скрыто .formFb.
    function forceShow(el, display) {
        if (!el) { return; }
        el.style.setProperty('display', display, 'important');
        el.style.setProperty('visibility', 'visible', 'important');
        el.style.setProperty('opacity', '1', 'important');
        el.removeAttribute('hidden');
    }

    function showOrderNow() {
        var order = $order.get(0);
        forceShow(order, 'block');

        // Поднимаемся по родителям и снимаем всё, что могло бы спрятать форму.
        var node = order.parentNode;
        while (node && node.nodeType === 1 && node !== document.body) {
            var cs = window.getComputedStyle(node);
            if (cs.display === 'none') { forceShow(node, 'block'); }
            if (cs.visibility === 'hidden') { node.style.setProperty('visibility', 'visible', 'important'); }
            node = node.parentNode;
        }
        // И по детям формы — .formFb и его контейнер.
        $order.find('*').each(function () {
            if (window.getComputedStyle(this).display === 'none') { forceShow(this, 'block'); }
        });

        var h = order.getBoundingClientRect().height;
        window.__vlog('форма показана, высота = ' + Math.round(h) + 'px');
        if (h < 10) { window.__vlog('ВНИМАНИЕ: высота почти ноль — смотрите CSS формы'); }
    }

    function hideOrder() {
        var order = $order.get(0);
        if (order) { order.style.setProperty('display', 'none', 'important'); }
    }

    $play.on('click', function () {
        window.__vlog('клик по #play');
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
            window.__vlog('достигнута секунда ' + Math.round(t) + ' — открываю форму');
            showOrderNow();
            orderShown = true;
        }
        if (!showPlay && !showPopup && t > tStart) {
            $popup.fadeIn('fast');
            showPopup = true;
            window.__vlog('показан попап на ' + Math.round(t) + ' с');
        }
        if (hidePopup && t > tStart + tDuration) {
            $popup.fadeOut('fast');
            hidePopup = false;
        }
    });

    // 4. Три входа в форму. В старой версии крестик её не открывал.
    $video.on('ended', function () { window.__vlog('событие ended'); showOrder(); });
    $popup.on('click', function () { window.__vlog('клик по попапу'); showOrder(); });
    $close.on('click', function () { window.__vlog('клик по крестику'); showOrder(); });

    // Подстраховка: если видео вообще не стартовало и человек просто
    // проскроллил страницу вниз, форму всё равно надо показать.
    $(window).on('scroll.orderfallback', function () {
        if (orderShown) { return; }
        if ($(window).scrollTop() > $container.offset().top + $container.outerHeight() - 100) {
            window.__vlog('скролл ниже видео — открываю форму');
            showOrderNow();
            orderShown = true;
            $(window).off('scroll.orderfallback');
        }
    });

    function showOrder() {
        $container.removeClass('fullscreen');
        $play.hide();
        $popup.fadeOut();
        $close.fadeOut();
        document.documentElement.classList.remove('is-locked');
        start_timer();

        $video.fadeOut('fast', function () {
            $(this).trigger('pause');
            showOrderNow();
            orderShown = true;
            $('html, body').animate({ scrollTop: $order.offset().top - 20 }, 200);
        });
    }
});

// 5. Таймер: защита от повторного запуска.
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
