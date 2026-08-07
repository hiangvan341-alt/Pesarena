(function () {
    'use strict';

    const buttons = Array.from(document.querySelectorAll('[data-admin-tab]'));
    const panels = Array.from(document.querySelectorAll('[data-admin-panel]'));
    const allowedTabs = new Set(buttons.map((button) => button.dataset.adminTab));
    let activeTab = null;

    function loadLazyModule(tabName) {
        const panel = document.querySelector('[data-admin-panel="' + tabName + '"]');
        if (!panel) return;
        panel.querySelectorAll('iframe[data-admin-lazy-src]').forEach((frame) => {
            if (!frame.getAttribute('src')) frame.setAttribute('src', frame.dataset.adminLazySrc);
        });
    }

    function activateAdminTab(tabName, options) {
        const config = options || {};
        const selected = allowedTabs.has(tabName) ? tabName : 'overview';
        if (selected === activeTab && !config.force) return;
        activeTab = selected;

        buttons.forEach((button) => {
            const isActive = button.dataset.adminTab === selected;
            button.classList.toggle('active', isActive);
            button.setAttribute('aria-selected', isActive ? 'true' : 'false');
            button.tabIndex = isActive ? 0 : -1;
        });

        panels.forEach((panel) => {
            const isActive = panel.dataset.adminPanel === selected;
            panel.hidden = !isActive;
            panel.classList.toggle('is-active', isActive);
        });

        loadLazyModule(selected);
        if (config.updateHash !== false) history.replaceState(null, '', '#' + selected);
    }

    // Một listener duy nhất. Bản cũ tạo listener pointerdown lặp lại mỗi lần đổi tab,
    // khiến số handler tăng dần và gây cảm giác click ngày càng lag.
    document.addEventListener('click', (event) => {
        const button = event.target.closest('[data-admin-tab]');
        if (!button) return;
        event.preventDefault();
        activateAdminTab(button.dataset.adminTab);
    });

    window.addEventListener('hashchange', () => {
        activateAdminTab(window.location.hash.slice(1), { updateHash: false });
    });

    activateAdminTab(window.location.hash.slice(1), { updateHash: false, force: true });

    const searchInput = document.getElementById('adminUserSearch');
    const duplicateOnly = document.getElementById('adminDuplicateOnly');
    const userRows = Array.from(document.querySelectorAll('[data-user-summary]'));
    const emptyState = document.getElementById('adminUserEmpty');
    let filterFrame = null;

    function applyUserFilters() {
        filterFrame = null;
        const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
        const onlyDuplicate = Boolean(duplicateOnly && duplicateOnly.checked);
        let visible = 0;

        userRows.forEach((row) => {
            const matchesQuery = !query || (row.dataset.userSearch || '').includes(query);
            const matchesDuplicate = !onlyDuplicate || row.dataset.duplicateIp === '1';
            const shouldShow = matchesQuery && matchesDuplicate;
            const toggle = row.querySelector('[data-user-toggle]');
            const detail = toggle ? document.getElementById(toggle.dataset.userToggle) : null;
            row.hidden = !shouldShow;
            if (!shouldShow && detail) {
                detail.hidden = true;
                toggle.setAttribute('aria-expanded', 'false');
                toggle.textContent = 'Quản lý';
            }
            if (shouldShow) visible += 1;
        });
        if (emptyState) emptyState.hidden = visible !== 0;
    }

    function queueUserFilter() {
        if (filterFrame) cancelAnimationFrame(filterFrame);
        filterFrame = requestAnimationFrame(applyUserFilters);
    }

    if (searchInput) searchInput.addEventListener('input', queueUserFilter, { passive: true });
    if (duplicateOnly) duplicateOnly.addEventListener('change', applyUserFilters);

    document.addEventListener('click', (event) => {
        const toggle = event.target.closest('[data-user-toggle]');
        if (!toggle) return;
        const detail = document.getElementById(toggle.dataset.userToggle);
        if (!detail) return;
        const opening = detail.hidden;
        detail.hidden = !opening;
        toggle.setAttribute('aria-expanded', opening ? 'true' : 'false');
        toggle.textContent = opening ? 'Đóng' : 'Quản lý';
        if (opening) requestAnimationFrame(() => detail.scrollIntoView({ block: 'nearest', behavior: 'smooth' }));
    });

    const showPasswords = document.getElementById('showAdminPasswords');
    if (showPasswords) {
        showPasswords.addEventListener('change', () => {
            document.querySelectorAll('.admin-new-password').forEach((input) => {
                input.type = showPasswords.checked ? 'text' : 'password';
            });
        });
    }

    document.querySelectorAll('.temporary-password-input').forEach((input) => {
        input.addEventListener('focus', () => { input.type = 'text'; });
        input.addEventListener('blur', () => { input.type = 'password'; });
    });

    document.querySelectorAll('.admin-report-filter a').forEach((link) => {
        link.addEventListener('click', () => {
            link.classList.add('is-loading');
            link.setAttribute('aria-busy', 'true');
        });
    });
})();
