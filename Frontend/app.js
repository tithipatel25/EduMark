const form = document.getElementById('marksForm');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const student = {
        name: document.getElementById('name').value,
        subject: document.getElementById('subject').value,
        marks: parseFloat(document.getElementById('marks').value, 10)
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/add_mark/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(student)
        });

        const data = await res.json();
        document.getElementById('response').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById('response').innerText = 'Error: ' + error;
    }
});
