let quote = document.getElementById('quote');
let author = document.getElementById('author');
let button = document.getElementById('button');

let url = "https://api.quotable.io/random"

const getQuote = () => {
    fetch(url)
        .then((data) => data.json())
        .then((item) => {
            quote.innerText = item.content;
            author.innerText = item.author;
        });
};

button.addEventListener('click', getQuote());
window.addEventListener('load', getQuote());