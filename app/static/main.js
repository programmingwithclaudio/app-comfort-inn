// Sign In Form
const $signinBtn = document.getElementById("signin");
const $signinContainer = document.getElementById("signin-container");

$signinBtn.addEventListener("click", () => {
    $signinContainer.style.display = "block";
    document.getElementById("signin-email").focus();
});

document.onkeydown = function(e) {
    e = e || window.event;
    if (e.key === "Escape") {
        $signinContainer.style.display = "none";
    }
};

// Sign Up Form
const $signupBtn = document.getElementById("signup");
const $signupContainer = document.getElementById("signup-container");

$signupBtn.addEventListener("click", () => {
    $signupContainer.style.display = "block";
    document.getElementById("signup-firstname").focus();
});

document.onkeydown = function(e) {
    e = e || window.event;
    if (e.key === "Escape") {
        $signupContainer.style.display = "none";
    }
};
