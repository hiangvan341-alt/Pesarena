(() => {
  "use strict";

  const copyText = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const field = document.createElement("textarea");
    field.value = text;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.opacity = "0";
    document.body.appendChild(field);
    field.select();
    const copied = document.execCommand("copy");
    field.remove();
    if (!copied) throw new Error("copy_failed");
  };

  document.addEventListener("click", async (event) => {
    const button = event.target.closest("[data-profile-share]");
    if (!button) return;
    const original = button.dataset.shareLabel || button.textContent.trim();
    try {
      await copyText(window.location.href);
      button.textContent = "✓ Đã sao chép liên kết";
      button.classList.add("is-copied");
      window.setTimeout(() => {
        button.textContent = original;
        button.classList.remove("is-copied");
      }, 2200);
    } catch (_error) {
      button.textContent = "Không thể sao chép";
      window.setTimeout(() => { button.textContent = original; }, 2200);
    }
  });
})();
