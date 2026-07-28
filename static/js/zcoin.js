document.addEventListener("DOMContentLoaded", function () {
    const search = document.getElementById("zcoinPlayerSearch");
    if (!search) return;

    search.addEventListener("input", function () {
        const query = search.value.trim().toLowerCase();
        document.querySelectorAll("[data-zcoin-player]").forEach(function (row) {
            row.hidden = Boolean(query) && !(row.dataset.search || "").includes(query);
        });
    });
});
