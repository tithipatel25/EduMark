// Toast Function
function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
}



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
        showToast('Please upload a .txt file');
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
            showToast(data.detail || "Upload failed");
            return;
        }

        showToast(`Uploaded successfully! ${data.students_count} students added.`);
        console.log(data);

        // Hide middle section
        middleSection.style.display = "none";

        // Fetch students and render table
        fetchStudentsAndRenderTable();

    } catch (err) {
        console.error(err);
        showToast("Backend not reachable");
    }
});


// Fetch students and render table

async function fetchStudentsAndRenderTable() {
    const studentsTableCard = document.getElementById('studentsTableCard'); // add this line

    try {
        const res = await fetch("http://127.0.0.1:8000/api/students");
        const students = await res.json();

        if (!students || students.length === 0) {
            studentsTableDiv.innerHTML = `
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Full Name</th>
                                <th>Student ID</th>
                                <th>Add Assignment</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td colspan="3">No students found.</td></tr>
                        </tbody>
                    </table>
                </div>
            `;
            studentsTableCard.style.display = "block"; // changed
            return;
        }

        studentsTableDiv.innerHTML = `
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Full Name</th>
                            <th>Student ID</th>
                            <th>Add Assignment</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${students.map(s => `
                            <tr>
                                <td>${s.first_name} ${s.last_name}</td>
                                <td>${s.student_id}</td>
                                <td><button>Add</button></td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
        studentsTableCard.style.display = "block"; // changed

    } catch (err) {
        console.error("Failed to fetch students:", err);
        studentsTableDiv.innerHTML = "<p>Error fetching students.</p>";
        studentsTableCard.style.display = "block"; // changed
    }
}


// Quick Action Buttons

createAssessmentBtn.addEventListener('click', () => {
    showToast('Create New Assessment clicked!');
    // Add your functionality here
});

viewReportsBtn.addEventListener('click', () => {
    showToast('View Reports clicked!');
    // Add your functionality here
});

messageStudentsBtn.addEventListener('click', () => {
    showToast('Stay tuned!');
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









const assignmentModal = document.getElementById("assignmentModle");
const assignmentNameInput = document.getElementById("assignmentName");
const marksContainer = document.getElementById("marksContainer");
const saveAssignmentBtn = document.getElementById("saveAssignmentBtn");

if (saveAssignmentBtn) {

    saveAssignmentBtn.addEventListener("click", async () => {

        const name = assignmentNameInput.value.trim();

        if (!name) {
            alert("Assignment name required");
            return;
        }

        const inputs = marksContainer.querySelectorAll("input");
        const marksObject = {};

        inputs.forEach(input => {

            const studentId = input.dataset.id;
            const value = input.value;

            marksObject[studentId] = value ? Number(value) : null;

        });

        try {

            const res = await fetch("http://127.0.0.1:8000/api/add-assignment", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    assignment_name: name,
                    marks: marksObject
                })
            });

            if (!res.ok) {
                alert("Failed to save assignment");
                return;
            }

            assignmentModal.style.display = "none";

            fetchStudentsAndRenderTable();

        } catch (err) {
            console.error(err);
            alert("Server error");
        }

    });

}