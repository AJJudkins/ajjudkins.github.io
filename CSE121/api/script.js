let quote = document.getElementById('quote');
let author = document.getElementById('author');
let type = document.getElementById('genre');

const getQuote = () => {

    if (type === "random") {
        let url = "https://api.quotable.io/random"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    } else if (type === "love") {
        let url = "https://api.quotable.io/quotes?tags=love"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    } else if (type === "happiness") {
        let url = "https://api.quotable.io/quotes?tags=happiness"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    } else if (type === "tech") {
        let url = "https://api.quotable.io/random?tags=technology"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    } else if (type === "famous") {
        let url = "https://api.quotable.io/random?tag=famous-quotes"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    } else {
        let url = "https://api.quotable.io/random"
        fetch(url)
            .then((data) => data.json())
            .then((item) => {
                quote.innerText = item.content;
                author.innerText = item.author;
            });
    }
}
document.getElementById('genre').addEventListener("change", getQuote());
document.getElementById('button').addEventListener('click', getQuote());
window.addEventListener('load', getQuote());