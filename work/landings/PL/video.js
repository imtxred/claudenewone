/* video.js — v3
   Форма заказа открывается модальным окном по центру экрана,
   фон затемняется. Три входа: конец ролика, клик по попапу, крестик.
   Диагностика: открыть страницу с ?debug=1 — внизу чёрная плашка с логом. */

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

    if (window.__videoInit) { window.__vlog('повторное подключение video.js — пропущено'); return; }
    window.__videoInit = true;
    window.__vlog('video.js v3 запущен');

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

    // Настройки читаются из инлайн-блока index.html.
    var tStart    = (typeof window.start    === 'number') ? window.start    : 120;
    var tDuration = (typeof window.duration === 'number') ? window.duration : 10;
    var tShowForm = (typeof window.showForm === 'number') ? window.showForm : 600;
    // Крестик в углу модального окна. Поставьте false — окно станет без выхода.
    var MODAL_CLOSABLE = (typeof window.modalClosable === 'boolean') ? window.modalClosable : true;
    window.__vlog('настройки: start=' + tStart + ' duration=' + tDuration + ' showForm=' + tShowForm);

    var showPopup = false;
    var hidePopup = true;
    var showPlay = true;
    var orderShown = false;

    hideOrder();

    /* ---------- модальное окно ---------- */

    var STYLE_ID = 'orderModalStyle';
    if (!document.getElementById(STYLE_ID)) {
        var st = document.createElement('style');
        st.id = STYLE_ID;
        st.textContent =
            '#orderModal{position:fixed!important;inset:0!important;z-index:2147483000!important;' +
            'display:none;align-items:center;justify-content:center;padding:16px;' +
            'background:rgba(0,0,0,.65)!important;-webkit-backdrop-filter:blur(2px);backdrop-filter:blur(2px);' +
            'overflow-y:auto;-webkit-overflow-scrolling:touch}' +
            '#orderModal.is-open{display:flex!important}' +
            '#orderModal>.orderModal__box{position:relative;width:100%;max-width:440px;margin:auto;' +
            'max-height:92vh;overflow-y:auto;background:#fff;border-radius:14px;' +
            'padding:26px 16px 18px;box-sizing:border-box;' +
            'box-shadow:0 18px 60px rgba(0,0,0,.45);animation:orderModalIn .22s ease-out}' +
            '#orderModal #order{width:100%!important;max-width:100%!important;margin:0!important;' +
            'box-sizing:border-box;overflow-wrap:break-word}' +
            '#orderModal .orderModal__x{position:absolute;top:6px;right:10px;z-index:2;cursor:pointer;' +
            'width:32px;height:32px;line-height:30px;text-align:center;font:22px/30px Arial,sans-serif;' +
            'color:#9aa0a6;background:transparent;border:0}' +
            '#orderModal .orderModal__x:hover{color:#444}' +
            '@keyframes orderModalIn{from{transform:translateY(14px);opacity:0}to{transform:none;opacity:1}}' +
            'html.is-modal-open,body.is-modal-open{overflow:hidden!important}';
        document.head.appendChild(st);
    }

    var modal = document.createElement('div');
    modal.id = 'orderModal';
    var modalBox = document.createElement('div');
    modalBox.className = 'orderModal__box';
    modal.appendChild(modalBox);
    document.body.appendChild(modal);

    if (MODAL_CLOSABLE) {
        var xBtn = document.createElement('button');
        xBtn.type = 'button';
        xBtn.className = 'orderModal__x';
        xBtn.setAttribute('aria-label', 'Zamknij');
        xBtn.innerHTML = '&times;';
        modalBox.appendChild(xBtn);
        xBtn.addEventListener('click', closeModal);
    }

    // Запоминаем, где форма лежала изначально, чтобы вернуть её при закрытии.
    var orderHome = document.createElement('span');
    orderHome.style.display = 'none';
    $order.get(0).parentNode.insertBefore(orderHome, $order.get(0));

    function forceShow(el, display) {
        if (!el) { return; }
        el.style.setProperty('display', display, 'important');
        el.style.setProperty('visibility', 'visible', 'important');
        el.style.setProperty('opacity', '1', 'important');
        el.removeAttribute('hidden');
    }

    function unhideInside(root) {
        $(root).find('*').each(function () {
            if (window.getComputedStyle(this).display === 'none') { forceShow(this, 'block'); }
        });
    }

    function openModal() {
        var order = $order.get(0);
        modalBox.appendChild(order);           // переносим саму форму внутрь окна
        forceShow(order, 'block');
        unhideInside(order);
        modal.classList.add('is-open');
        document.documentElement.classList.add('is-modal-open');
        document.body.classList.add('is-modal-open');
        orderShown = true;
        var h = order.getBoundingClientRect().height;
        window.__vlog('модальное окно открыто, высота формы = ' + Math.round(h) + 'px');
        if (h < 10) { window.__vlog('ВНИМАНИЕ: высота почти ноль — смотрите CSS формы'); }
        var firstInput = order.querySelector('input[name="name"]');
        if (firstInput && window.innerWidth > 760) { try { firstInput.focus(); } catch (e) {} }
    }

    function closeModal() {
        modal.classList.remove('is-open');
        document.documentElement.classList.remove('is-modal-open');
        document.body.classList.remove('is-modal-open');
        // Возвращаем форму на место под видео, чтобы она оставалась доступной.
        var order = $order.get(0);
        orderHome.parentNode.insertBefore(order, orderHome);
        forceShow(order, 'block');
        window.__vlog('окно закрыто, форма вернулась под видео');
    }

    function showOrderInline() {
        var order = $order.get(0);
        forceShow(order, 'block');
        unhideInside(order);
        var node = order.parentNode;
        while (node && node.nodeType === 1 && node !== document.body) {
            if (window.getComputedStyle(node).display === 'none') { forceShow(node, 'block'); }
            node = node.parentNode;
        }
    }

    function hideOrder() {
        var order = $order.get(0);
        if (order) { order.style.setProperty('display', 'none', 'important'); }
    }

    /* ---------- плеер ---------- */

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
            window.__vlog('секунда ' + Math.round(t) + ' — форма открыта под видео');
            showOrderInline();
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

    // Три входа в модальное окно.
    $video.on('ended', function () { window.__vlog('событие ended'); showOrder(); });
    $popup.on('click', function () { window.__vlog('клик по попапу'); showOrder(); });
    $close.on('click', function () { window.__vlog('клик по крестику'); showOrder(); });

    // Подстраховка: человек не стал смотреть и пролистал ниже плеера.
    $(window).on('scroll.orderfallback', function () {
        if (orderShown) { return; }
        if ($(window).scrollTop() > $container.offset().top + $container.outerHeight() - 100) {
            window.__vlog('скролл ниже видео — форма открыта под видео');
            showOrderInline();
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
            openModal();
        });
    }
});

/* ---------- таймер ---------- */

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
