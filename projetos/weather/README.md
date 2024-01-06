# Mini Projeto de Previsão do Tempo #
## Author: Ivanoel Rodrigo ##
### Skills ###
#### HTML5, CSS, JAVASCRIPT, API OPENWEATHER, JSON ####



Esse projeto tem como finalidade prever a temperatura de uma região, comecei fazendo a estrutura do site com HTML5, utilizei css para 
fazer a centralização do body na tela, antes de tudo zerei algumas configurações e deixei o link para compatibilidade de
alguns navegadores, utitizei a função hover do css para chamar uma cidade e fazer o efeito para mostra o tempo, aqui utilizei 
uma APi da  OpenWeather (https://home.openweathermap.org/) para buscar a região solicitada, deixei alguns parametros como:${parseInt(json.main.temp)}<span>°C</span; 
${json.main.humidity}%; ${parseInt(json.wind.speed)}; ${parseInt(json.main.temp)}<span>°C</span>; ${json.weather[0].description} para buscar temperatura,
descrição, umidade e vento. usei também o fontawesome para usar icones para umidade e vento,
converte a API para o idioma &lang = pt_br.