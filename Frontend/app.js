// Elements
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const middleSection = document.getElementById('middleSection');
const studentsTableDiv = document.getElementById('studentsTable');

const createAssessmentBtn = document.getElementById('createAssessmentBtn');
const viewReportsBtn = document.getElementById('viewReportsBtn');
const messageStudentsBtn = document.getElementById('messageStudentsBtn');

// File Upload Handling

uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    if (!file.name.endsWith('.txt')) {
        alert('Please upload a .txt file');
        e.target.value = '';
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("http://127.0.0.1:8000/api/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (!res.ok) {
            alert(data.detail || "Upload failed");
            return;
        }

        alert(`Uploaded successfully! ${data.students_count} students added.`);
        console.log(data);

        // Hide middle section
        middleSection.style.display = "none";

        // Fetch students and render table
        fetchStudentsAndRenderTable();

    } catch (err) {
        console.error(err);
        alert("Backend not reachable");
    }
});


// Fetch students and render table

async function fetchStudentsAndRenderTable() {
    try {
        const res = await fetch("http://127.0.0.1:8000/api/students");
        const students = await res.json();

        if (!students || students.length === 0) {
            studentsTableDiv.innerHTML = `
            <div class="table-wrapper">
                <table border="1" cellpadding="8" cellspacing="0">
                    <tr>
                        <th>Full Name</th>
                        <th>Student ID</th>
                        <th>Add Assignment</th>
                    </tr>
                    ${students.map(s => `
                        <tr>
                            <td>${s.first_name} ${s.last_name}</td>
                            <td>${s.student_number}</td>
                            <td><button>Add</button></td>
                        </tr>
                    `).join('')}
                </table>
            </div>
        `;
        studentsTableDiv.style.display = "block";
            return;
        }

        let html = `
            <table border="1" cellpadding="8" cellspacing="0">
                <tr>
                    <th>Full Name</th>
                    <th>Student ID</th>
                    <th>Add Assignment</th>
                </tr>
        `;

        students.forEach(s => {
            html += `
                <tr>
                    <td>${s.first_name} ${s.last_name}</td>
                    <td>${s.student_id}</td>
                    <td><button>Add</button></td>
                </tr>
            `;
        });

        html += `</table>`;
        studentsTableDiv.innerHTML = html;
        studentsTableDiv.style.display = "block";

    } catch (err) {
        console.error("Failed to fetch students:", err);
        studentsTableDiv.innerHTML = "<p>Error fetching students.</p>";
        studentsTableDiv.style.display = "block";
    }
}


// Quick Action Buttons

createAssessmentBtn.addEventListener('click', () => {
    alert('Create New Assessment clicked!');
    // Add your functionality here
});

viewReportsBtn.addEventListener('click', () => {
    alert('View Reports clicked!');
    // Add your functionality here
});

messageStudentsBtn.addEventListener('click', () => {
    alert('Stay tuned!');
    // Add your functionality here
});


// Smooth Page Load Animation

window.addEventListener('load', () => {
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


// Navigation Links

const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        navLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        console.log('Navigated to:', link.textContent);
    });
});