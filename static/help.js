(function () {
  var root = document.documentElement;
  var features = window.HELP_FEATURES, presets = window.HELP_PRESETS;
  function holds(list) {
    return list.split(',').every(function (c) {
      return c.charAt(0) === '!' ? !features[c.slice(1)] : !!features[c];
    });
  }
  function apply() {
    root.dataset.mode = features.tablet ? 'tablet' : 'phone';
    document.querySelectorAll('[data-if]').forEach(function (e) { e.hidden = !holds(e.dataset.if); });
    document.querySelectorAll('[data-unless]').forEach(function (e) { e.hidden = holds(e.dataset.unless); });
    // A section heading or topic with nothing left under it goes too.
    document.querySelectorAll('.rail h3, .topic-list h3').forEach(function (h) {
      var e = h.nextElementSibling, any = false;
      while (e && e.tagName !== 'H3') { if (!e.hidden) any = true; e = e.nextElementSibling; }
      h.hidden = !any;
    });
    var fitting = {};
    (window.HELP_INDEX || []).forEach(function (x) { if (!x.r || holds(x.r)) fitting[x.u.split('/')[0]] = true; });
    document.querySelectorAll('[data-topic]').forEach(function (e) { e.hidden = !fitting[e.dataset.topic]; });
    var list = document.querySelector('.topic-list');
    if (list) {
      var left = Array.prototype.some.call(list.children, function (e) { return !e.hidden; });
      document.querySelector('.topic-empty').hidden = left;
    }
    document.querySelectorAll('[data-set]').forEach(function (b) {
      var p = presets[b.dataset.set], on = Object.keys(p).every(function (k) { return !p[k] === !features[k]; });
      b.setAttribute('aria-checked', on ? 'true' : 'false');
    });
    document.querySelectorAll('[data-feature]').forEach(function (c) { c.checked = !!features[c.dataset.feature]; });
  }
  function save() {
    try { localStorage.setItem('help-features', JSON.stringify(features)); } catch (e) {}
    apply();
    if (window.HELP_REFRESH) window.HELP_REFRESH();
  }
  document.querySelectorAll('[data-set]').forEach(function (b) {
    b.addEventListener('click', function () {
      features = Object.assign({}, presets[b.dataset.set]);
      save();
    });
  });
  document.querySelectorAll('[data-feature]').forEach(function (c) {
    c.addEventListener('change', function () {
      features = Object.assign({}, features);
      features[c.dataset.feature] = c.checked ? 1 : 0;
      save();
    });
  });
  if (root.dataset.onDevice) document.body.classList.add('app-device');
  apply();

  var menu = document.querySelector('.appmenu');
  document.addEventListener('click', function (e) { if (menu && !menu.contains(e.target)) menu.open = false; });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu) menu.open = false; });

  var q = document.getElementById('q');
  if (!q) return;
  var results = document.getElementById('results');
  var browse = document.getElementById('browse');
  var data = window.HELP_INDEX || [];
  function fits(a) { return !a.r || holds(a.r); }
  function esc(s) { var e = document.createElement('i'); e.textContent = s; return e.innerHTML; }
  function find(terms) {
    return data.map(function (a) {
      var t = a.t.toLowerCase(), x = a.x.toLowerCase(), c = a.c.toLowerCase(), s = 0;
      for (var i = 0; i < terms.length; i++) {
        var w = terms[i];
        var hit = (t.indexOf(w) >= 0 ? 10 : 0) + (c.indexOf(w) >= 0 ? 4 : 0) + (x.indexOf(w) >= 0 ? 1 : 0);
        if (!hit) return null;
        s += hit;
      }
      return { a: a, s: s };
    }).filter(function (m) { return m && fits(m.a); }).sort(function (m, n) { return n.s - m.s; }).slice(0, 30);
  }
  function show() {
    var v = q.value.trim().toLowerCase();
    if (v.length < 2) { results.hidden = true; browse.hidden = false; return; }
    var hits = find(v.split(/\s+/));
    browse.hidden = true; results.hidden = false;
    results.innerHTML = hits.length ? hits.map(function (h) {
      return '<a href="' + h.a.u + '"><strong>' + esc(h.a.t) + '</strong><span>' + esc(h.a.c) + '</span></a>';
    }).join('') : '<p class="none">Nothing matches &ldquo;' + esc(q.value.trim()) + '&rdquo;. Try fewer words, or <a href="get-help.html">get help</a>.</p>';
  }
  window.HELP_REFRESH = show;
  q.addEventListener('input', show);
  var start = new URLSearchParams(location.search).get('q');
  if (start) { q.value = start; show(); }
})();
