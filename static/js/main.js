// Query Cruise and Room
let rooms = document.getElementsByClassName("cruises-room");
let cruises = document.getElementsByClassName("cruise-list");

// Listen the clic of the Properly
document.addEventListener("click", (event) => {

    const link = event.target.closest('.dashboard-link');

    if (!link) return;

    event.preventDefault();

    const target = link.dataset.target;

    document.querySelectorAll('.dashboard-section').forEach(section => {
        section.style.display = section.id === target ? "block" : "none";
    });
});