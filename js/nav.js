// Mobile navigation toggle. Progressive enhancement only:
// the menu is visible by default when JS is off (CSS handles desktop).
(function () {
  "use strict";
  var nav = document.querySelector("[data-nav]");
  if (!nav) return;
  var toggle = nav.querySelector(".nav__toggle");
  var menu = nav.querySelector(".nav__menu");
  if (!toggle || !menu) return;

  function setOpen(open) {
    nav.setAttribute("data-open", open ? "true" : "false");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  setOpen(false);

  toggle.addEventListener("click", function () {
    setOpen(nav.getAttribute("data-open") !== "true");
  });

  // Close the menu on Escape for keyboard users.
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setOpen(false);
  });
})();
