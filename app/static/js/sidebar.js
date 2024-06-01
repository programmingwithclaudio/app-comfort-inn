document.addEventListener('DOMContentLoaded', () => {
  const expand_btn = document.querySelector(".expand-btn");
  console.log("Expand button found:", expand_btn);

  if (expand_btn) {
    expand_btn.addEventListener("click", () => {
      document.body.classList.toggle("collapsed");
      console.log("Expand button clicked");
    });
  }

  const current = window.location.href;

  const allLinks = document.querySelectorAll(".sidebar-links a");
  console.log("All links found:", allLinks.length);

  allLinks.forEach((elem) => {
    elem.addEventListener("click", function () {
      const hrefLinkClick = elem.href;

      allLinks.forEach((link) => {
        if (link.href == hrefLinkClick) {
          link.classList.add("active");
          console.log("Link activated:", link.href);
        } else {
          link.classList.remove("active");
        }
      });
    });
  });

  const searchInput = document.querySelector(".search__wrapper input");
  console.log("Search input found:", searchInput);

  if (searchInput) {
    searchInput.addEventListener("focus", (e) => {
      document.body.classList.remove("collapsed");
      console.log("Search input focused");
    });
  }
});
