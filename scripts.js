// Basic JavaScript for carousel functionality
let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');

function showItem(index) {
    items.forEach((item, i) => {
        item.style.transform = `translateX(${100 * (i - index)}%)`;
    });
}

function nextItem() {
    currentIndex = (currentIndex + 1) % items.length;
    showItem(currentIndex);
}

document.getElementById("signupButton").addEventListener("click", function() {
    window.location.href = 'Dashboardsignup.html';
});

document.getElementById("loginButton").addEventListener("click", function() {
    window.location.href = 'login.html';
});

document.getElementById("logo").addEventListener("click", function() {
    window.location.href = 'index.html';
});

function prevItem() {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    showItem(currentIndex);
}

// Auto slide
setInterval(nextItem, 5000);

function toggleTeamMemberDetails() {
    var teamMembers = document.querySelectorAll('.team-member');
    teamMembers.forEach(function(member) {
        member.style.display = (member.style.display === 'none' || member.style.display === '') ? 'block' : 'none';
    });
}
