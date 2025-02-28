document.addEventListener("DOMContentLoaded", function() {
    const notes = document.querySelectorAll('.anotacoes');
    notes.forEach(note => {
        const noteId = note.getAttribute('data-id');

        const savedLeft = localStorage.getItem(`noteLeft${noteId}`);
        const savedTop = localStorage.getItem(`noteTop${noteId}`);

        if (savedLeft && savedTop) {
            note.style.left = savedLeft;
            note.style.top = savedTop;
        } else {
            // Generate random initial position
            const randomLeft = Math.floor(Math.random() * (window.innerWidth - note.offsetWidth));
            const randomTop = Math.floor(Math.random() * (window.innerHeight - note.offsetHeight));
            note.style.left = `${randomLeft}px`;
            note.style.top = `${randomTop}px`;
            localStorage.setItem(`noteLeft${noteId}`, `${randomLeft}px`);
            localStorage.setItem(`noteTop${noteId}`, `${randomTop}px`);
        }

        note.style.position = 'absolute';
        note.style.cursor = 'move';

        let isDragging = false;
        let offsetX, offsetY;

        note.addEventListener('mousedown', function(e) {
            isDragging = true;
            offsetX = e.clientX - note.getBoundingClientRect().left;
            offsetY = e.clientY - note.getBoundingClientRect().top;
            note.style.zIndex = 1000; // Bring the note to the front
        });

        document.addEventListener('mousemove', function(e) {
            if (isDragging) {
                const newLeft = `${e.clientX - offsetX}px`;
                const newTop = `${e.clientY - offsetY}px`;
                note.style.left = newLeft;
                note.style.top = newTop;
                localStorage.setItem(`noteLeft${noteId}`, newLeft);
                localStorage.setItem(`noteTop${noteId}`, newTop);
            }
        });

        document.addEventListener('mouseup', function() {
            isDragging = false;
            note.style.zIndex = ''; // Reset z-index
        });
    });
});