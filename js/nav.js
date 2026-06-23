// Mobile navigation toggle. Progressive enhancement only:
// the menu is visible by default when JS is off (CSS handles desktop).
//
// Listeners are delegated on `document` rather than bound to the toggle
// button. The shell navigates via hx-boost + idiomorph (morph:innerHTML),
// which swaps the <body> in place on every link click. A handler bound
// directly to the button would be lost in that swap (the menu then stops
// responding until a full reload). A delegated handler on the persistent
// `document` survives every navigation. The init guard keeps exactly one
// set of listeners even if this script is re-executed after a swap.
(function () {
  "use strict";
  if (window.__navInit) return;
  window.__navInit = true;

  function setOpen(nav, open) {
    nav.setAttribute("data-open", open ? "true" : "false");
    var toggle = nav.querySelector(".nav__toggle");
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  document.addEventListener("click", function (e) {
    var toggle = e.target.closest(".nav__toggle");
    if (!toggle) return;
    var nav = toggle.closest("[data-nav]");
    if (!nav) return;
    setOpen(nav, nav.getAttribute("data-open") !== "true");
  });

  // Close the menu on Escape for keyboard users.
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var nav = document.querySelector("[data-nav]");
    if (nav) setOpen(nav, false);
  });
})();
