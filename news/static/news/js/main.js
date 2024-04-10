let pageNumber = 1;
const perPage = 3;
let loading = false;

async function loadNews() {
  loading = true;
  const response = await fetch(`http://127.0.0.1:8000/news/load_more/?page=${pageNumber}&perPage=${perPage}`);
  const data = await response.json();
  console.log(data)
  loading = false;
  return data;
}

function displayNews(news) {
  const newsContainer = document.getElementById('news-container');
  news.forEach(item => {
    const newsItem = document.createElement('div');
    newsItem.classList.add('news-item');

    titleLink.textContent = item.title;
    const title = document.createElement('h2');
    title.appendChild(titleLink);

    const text = document.createElement('p');
    text.textContent = item.text;

    const image = document.createElement('img');
    image.src = "http://127.0.0.1:8000/media/" + item.image_url;
    image.alt = item.title;
    
    const tags = document.createElement('div');
    tags.classList.add('tags');
    item.tags.forEach(tag => {
      const tagElement = document.createElement('span');
      tagElement.textContent = tag.name;
      tags.appendChild(tagElement);
    });
    const likeButton = document.createElement('button');
    likeButton.classList.add('like-button');
    likeButton.innerHTML = '<i class="fas fa-thumbs-up"></i>';
    likeButton.addEventListener('click', () => likeButtonClicked(item.id));

    const dislikeButton = document.createElement('button');
    dislikeButton.classList.add('dislike-button');
    dislikeButton.innerHTML = '<i class="fas fa-thumbs-down"></i>';
    dislikeButton.addEventListener('click', () => dislikeButtonClicked(item.id));
    
    const dislikesCount = document.createElement('span');
    dislikesCount.id = `dislikes-count-${item.id}`;
    dislikesCount.textContent = item.dislikesCount;

    const likesCount = document.createElement('span');
    likesCount.id = `likes-count-${item.id}`;
    likesCount.textContent = item.likesCount;

    newsItem.appendChild(title);
    newsItem.appendChild(text);
    newsItem.appendChild(image);
    newsItem.appendChild(tags);
    newsItem.appendChild(likeButton);
    newsItem.appendChild(likesCount);
    newsItem.appendChild(dislikeButton);
    newsItem.appendChild(dislikesCount);

    newsContainer.appendChild(newsItem);
  });
}

window.addEventListener('scroll', async () => {
  const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
  if (scrollTop + clientHeight >= scrollHeight - 5 && !loading) {
    pageNumber++;
    const news = await loadNews();
    displayNews(news);
  }
});

async function updateLikes(newsId, action) {
    if (action === 'like'){
    const response = await fetch(`http://127.0.0.1:8000/news/get_likes/${newsId}/`, {
        method: 'GET',
    })
    const data = await response.json();
    return data.likesCount;
  }
  else if (action === 'dislike'){
      const response = await fetch(`http://127.0.0.1:8000/news/get_dislikes/${newsId}/`, {
        method: 'GET',
      })
      const data = await response.json();
      return data.dislikesCount};
}

async function likeButtonClicked(newsId) {
  const likesCount = await updateLikes(newsId, 'like');
  document.getElementById(`likes-count-${newsId}`).innerText = likesCount;
}

async function dislikeButtonClicked(newsId) {
  const dislikesCount = await updateLikes(newsId, 'dislike');
  document.getElementById(`dislikes-count-${newsId}`).innerText = dislikesCount;
}

window.onload = async () => {
  const news = await loadNews();
  displayNews(news);
};
