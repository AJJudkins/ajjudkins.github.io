let quote = document.getElementById('quote');
let author = document.getElementById('author');
let type = document.getElementById('genre');

const getUrl = async () => {
    let url = chooseType();
    await fetch(url)
        .then((data) => data.json())
        .then((item) => {
            quote.innerText = item.content;
            author.innerText = item.author;
        });
}

const chooseType = () => {
    let type = document.getElementById("genre").value;

    switch (type) {
        case "love":
            output = 'https://api.quotable.io/random';
            return output;
            break;
        case "happiness":
            output = 'https://api.quotable.io/random';
            return output;
            break;
        case "tech":
            output = 'https://api.quotable.io/random';
            return output;
            break;
        case "famous":
            output = 'https://api.quotable.io/random';
            return output;
            break;
        default:
            output = 'https://api.quotable.io/random';
            return output;
            break;
    }
};

document.getElementById('genre').addEventListener("change", getUrl());
document.getElementById('button').addEventListener('click', getUrl());
window.addEventListener('load', getUrl());