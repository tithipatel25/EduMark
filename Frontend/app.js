// Toast Function
function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
}

function openAssignmentModal() {
    const students = window.currentStudents || [];

    marksContainer.innerHTML = students.map(s => `
        <div class="marks-row">
            <span>${s.first_name} ${s.last_name}</span>
            <input 
                type="number" 
                data-id="${s.student_id}" 
                placeholder="—"
                min="0"
                max="100"
            >
        </div>
    `).join('');

    assignmentNameInput.value = '';
    assignmentModal.style.display = 'flex';
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
// This is where you can update all the changes to the table in the middle section
async function fetchStudentsAndRenderTable() {
    const studentsTableCard = document.getElementById('studentsTableCard');

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
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td colspan="2">No students found.</td></tr>
                        </tbody>
                    </table>
                </div>
            `;
            studentsTableCard.style.display = "block";
            return;
        }

        // Collect all unique assignment names across all students
        const assignmentNames = [];
        students.forEach(s => {
            if (s.assignments) {
                Object.keys(s.assignments).forEach(name => {
                    if (!assignmentNames.includes(name)) {
                        assignmentNames.push(name);
                    }
                });
            }
        });

        // Build table headers
        const assignmentHeaders = assignmentNames.map(name => `<th>${name}</th>`).join('');

        // Build table rows
        const rows = students.map(s => {
            const assignmentCells = assignmentNames.map(name => {
                const mark = s.assignments && s.assignments[name] !== undefined
                    ? s.assignments[name] !== null ? s.assignments[name] : '—'
                    : '—';
                return `<td>${mark}</td>`;
            }).join('');

            return `
                <tr>
                    <td>${s.first_name} ${s.last_name}</td>
                    <td>${s.student_id}</td>
                    ${assignmentCells}
                </tr>
            `;
        }).join('');

        studentsTableDiv.innerHTML = `
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Full Name</th>
                            <th>Student ID</th>
                            ${assignmentHeaders}
                        </tr>
                    </thead>
                    <tbody>
                        ${rows}
                    </tbody>
                </table>
            </div>
        `;
        studentsTableCard.style.display = "block";

        // Store students globally for modal
        window.currentStudents = students;

    } catch (err) {
        console.error("Failed to fetch students:", err);
        studentsTableDiv.innerHTML = "<p>Error fetching students.</p>";
        studentsTableCard.style.display = "block";
    }
}


// Quick Action Buttons

createAssessmentBtn.addEventListener('click', () => {
    if (!window.currentStudents) {
        showToast('Please upload student data first!');
        return;
    }
    openAssignmentModal();
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









const assignmentModal = document.getElementById("assignmentModal");
const assignmentNameInput = document.getElementById("assignmentName");
const marksContainer = document.getElementById("marksContainer");
const saveAssignmentBtn = document.getElementById("saveAssignmentBtn");

if (saveAssignmentBtn) {

    saveAssignmentBtn.addEventListener("click", async () => {

        const name = assignmentNameInput.value.trim();

        if (!name) {
            showToast("Assignment name required");
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
                showToast("Failed to save assignment");
                return;
            }

            assignmentModal.style.display = "none";

            fetchStudentsAndRenderTable();

        } catch (err) {
            console.error(err);
            showToast("Server error");
        }

    });

}


document.getElementById("closeAssignmentModal").addEventListener("click", () => {
    assignmentModal.style.display = "none";
});