const form = document.getElementById('imageForm');
const captionOutput = document.getElementById('captionOutput');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('imageInput');
    const file = fileInput.files[0];

    if (!file) {
        captionOutput.textContent = 'Please select an image first.';
        return;
    }

    captionOutput.textContent = 'Generating caption...';

    // Simulate caption generation logic
    setTimeout(() => {
        captionOutput.textContent = 'Ahile kei xaina caption nai.';
    }, 2000);
});