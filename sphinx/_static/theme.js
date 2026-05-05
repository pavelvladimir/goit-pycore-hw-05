(function () {
  function getPreferredTheme() {
    try {
      var storedTheme = window.localStorage.getItem("theme");
      if (storedTheme === "light" || storedTheme === "dark") {
        return storedTheme;
      }
    } catch (error) {
      // Ignore localStorage errors and fall back to system preference.
    }

    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try {
      window.localStorage.setItem("theme", theme);
    } catch (error) {
      // Ignore localStorage errors.
    }
  }

  function updateToggleLabel(button, theme) {
    var nextTheme = theme === "dark" ? "light" : "dark";
    button.dataset.theme = theme;
    button.innerHTML =
      '<span class="theme-toggle__label">Theme</span>' +
      '<span class="theme-toggle__value">' + (theme === "dark" ? "Dark" : "Light") + "</span>";
    button.setAttribute("aria-label", "Switch to " + nextTheme + " mode");
    button.setAttribute("title", "Switch to " + nextTheme + " mode");
  }

  function ensureThemeToggle() {
    var existingButton = document.querySelector(".theme-toggle");
    if (existingButton) {
      return existingButton;
    }

    var button = document.createElement("button");
    button.className = "theme-toggle";
    button.type = "button";
    document.body.appendChild(button);
    return button;
  }

  function initializeTheme() {
    var currentTheme = getPreferredTheme();
    applyTheme(currentTheme);

    var toggleButton = ensureThemeToggle();
    updateToggleLabel(toggleButton, currentTheme);

    toggleButton.addEventListener("click", function () {
      currentTheme = currentTheme === "dark" ? "light" : "dark";
      applyTheme(currentTheme);
      updateToggleLabel(toggleButton, currentTheme);
    });

    window.addEventListener("storage", function (event) {
      if (event.key === "theme" && (event.newValue === "light" || event.newValue === "dark")) {
        currentTheme = event.newValue;
        applyTheme(currentTheme);
        updateToggleLabel(toggleButton, currentTheme);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeTheme);
  } else {
    initializeTheme();
  }
})();
