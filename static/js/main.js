document.addEventListener('DOMContentLoaded', function () {
  // Theme handling
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');

  function applyTheme(t) {
    if (t === 'dark') root.classList.add('theme-dark'); else root.classList.remove('theme-dark');
    localStorage.setItem('theme', t);
  }

  const saved = localStorage.getItem('theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyTheme(saved);

  if (toggle) {
    toggle.addEventListener('click', function () {
      const cur = root.classList.contains('theme-dark') ? 'dark' : 'light';
      applyTheme(cur === 'dark' ? 'light' : 'dark');
    });
  }

  // Alerts: auto-dismiss and manual dismiss
  document.querySelectorAll('#alerts .alert').forEach(function (el) {
    const dismiss = el.querySelector('.dismiss');
    if (dismiss) dismiss.addEventListener('click', function () { el.remove(); });
    // Auto hide after 5 seconds
    setTimeout(function () { if (el.parentNode) el.remove(); }, 5000);
  });
});
