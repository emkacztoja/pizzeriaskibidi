let count = 0;
document.getElementById('click-button').addEventListener('click', () => {
    count++;
    document.getElementById('click-count').innerText = count;
});
