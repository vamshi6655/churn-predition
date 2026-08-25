// ======================================================
// CUSTOMER CHURN AI DASHBOARD
// ======================================================

document.addEventListener("DOMContentLoaded", () => {

    // -------------------------------
    // Form Submit Animation
    // -------------------------------

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", () => {

            const button = document.querySelector("button");

            button.disabled = true;

            button.innerHTML =
                '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

        });

    }

    // -------------------------------
    // Smooth Card Hover
    // -------------------------------

    const sections = document.querySelectorAll(".section");

    sections.forEach(section => {

        section.addEventListener("mouseenter", () => {

            section.style.transform = "translateY(-5px)";

        });

        section.addEventListener("mouseleave", () => {

            section.style.transform = "translateY(0px)";

        });

    });

    // -------------------------------
    // Fade-in Animation
    // -------------------------------

    const dashboard =
        document.querySelector(".dashboard") ||
        document.querySelector(".result-card");

    if (dashboard) {

        dashboard.style.opacity = "0";
        dashboard.style.transform = "translateY(20px)";

        setTimeout(() => {

            dashboard.style.transition = "all .8s ease";

            dashboard.style.opacity = "1";

            dashboard.style.transform = "translateY(0px)";

        }, 100);

    }

    // -------------------------------
    // Progress Bar Animation
    // -------------------------------

    const progressBar = document.querySelector(".progress-bar");

    if (progressBar) {

        const targetWidth = progressBar.style.width;

        progressBar.style.width = "0%";

        setTimeout(() => {

            progressBar.style.transition = "width 1.5s ease";

            progressBar.style.width = targetWidth;

        }, 300);

    }

    // -------------------------------
    // Input Focus Glow
    // -------------------------------

    const fields = document.querySelectorAll("input, select");

    fields.forEach(field => {

        field.addEventListener("focus", () => {

            field.parentElement.style.transform = "scale(1.02)";

        });

        field.addEventListener("blur", () => {

            field.parentElement.style.transform = "scale(1)";

        });

    });

});