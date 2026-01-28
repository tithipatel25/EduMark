// File upload handler
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');

uploadBtn.addEventListener('click', function() {
    fileInput.click();
});

fileInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        if (file.name.endsWith('.txt')) {
            alert(`File "${file.name}" uploaded successfully!`);
            
            // Read and process the file
            const reader = new FileReader();
            reader.onload = function(event) {
                console.log('File content:', event.target.result);
                // Here you would typically process the file content
                // For example: parseStudentData(event.target.result);
            };
            reader.readAsText(file);
        } else {
            alert('Please upload a .txt file');
            e.target.value = '';
        }
    }
});

// Quick Action Buttons
const createAssessmentBtn = document.getElementById('createAssessmentBtn');
const viewReportsBtn = document.getElementById('viewReportsBtn');
const messageStudentsBtn = document.getElementById('messageStudentsBtn');

createAssessmentBtn.addEventListener('click', function() {
    alert('Create New Assessment clicked!');
    // Add your functionality here
});

viewReportsBtn.addEventListener('click', function() {
    alert('View Reports clicked!');
    // Add your functionality here
});

messageStudentsBtn.addEventListener('click', function() {
    alert('Message Students clicked!');
    // Add your functionality here
});

// Smooth page load animation
window.addEventListener('load', function() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});

// Optional: Add interactivity to navigation links
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
        console.log('Navigated to:', this.textContent);
    });
});