const container = document.querySelector('.container');
const pesquisar = document.querySelector('.pesquisar-box button');
const climaBox = document.querySelector('.clima-box');
const detalhesClima = document.querySelector('.detalhes-clima');
const error404 = document.querySelector('.nao-encontrado');

pesquisar.addEventListener('click', () => {
    const APIKey = 'a359e7071e17350bcce277a0e70c27fa';
    const city = document.querySelector('.pesquisar-box input').value;
    if (city === '')
        return;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${APIKey}&lang=pt_br`)
        .then(response => response.json())
        .then(json => {
            if (json.cod === '404') {
                container.style.height = '400px';
                climaBox.style.display = 'none';
                detalhesClima.style.display = 'none';
                error404.style.display = 'block';
                error404.classList.add('fadeIn');
                return;
            }

            error404.style.display = 'none';
            error404.classList.remove('fadeIn');
            const image = document.querySelector('.clima-box img');
            const temperatura = document.querySelector('.clima-box .temperatura');
            const descricao = document.querySelector('.clima-box .descricao');
            const data = document.querySelector('.clima-box .data');
            const umidade = document.querySelector('.detalhes-clima .umidade span');
            const vento = document.querySelector('.detalhes-clima .vento span');
            
            switch (json.weather[0].main) {
                case 'Clear':
                    image.src = 'img/01d.png';
                    break;

                case 'Rain':
                    image.src = 'img/11d.png';
                    break;

                case 'Snow':
                    image.src = 'img/13n.png';
                    break;

                case 'Clouds':
                    image.src = 'img/04n.png';
                    break;

                case 'Haze':
                    image.src = 'img/50d.png';
                    break;

                default:
                    image.src = '';
            }
            
            temperatura.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
            descricao.innerHTML = `${json.weather[0].description}`;            
            umidade.innerHTML = `${json.main.humidity}%`;
            vento.innerHTML = `${parseInt(json.wind.speed)} Km/h`;
            climaBox.style.display = '';
            detalhesClima.style.display = '';
            climaBox.classList.add('fadeIn');
            detalhesClima.classList.add('fadeIn');
            container.style.height = '590px';
        });
});