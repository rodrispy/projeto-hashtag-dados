<h1>👨‍💻 Projeto de Ciência de Dados</h1>
<h2>🏨 Airbnb Rio - Ferramenta de previsão de preço de imóvel para pessoas comuns</h2>
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogodownload.org%2Fwp-content%2Fuploads%2F2016%2F10%2Fairbnb-logo-10.png&f=1&nofb=1" align="center" width="400px">
<p>Este projeto está sendo realizado junto ao curso Python Impressionador, do Hashtag Programação.</p>
<p>Será utilizada a integração com algumas das bibliotecas mais comuns para tratamento e manipulação de dados do Python e modelagem para previsão com Machine Learning.</p>
<br>


<h2>✍️ Contexto</h2>
<p>No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertá-lo para ser alugado por diária.</p>
<p>O usuário cria o perfil de <i>host</i> (locatário da hospedagem) e cria o anúncio do seu imóvel.</p>
<p>Nesse anúncio, o <i>host</i> deve descrever as características do imóvel da forma mais completa possível, de forma a ajudar os locadores a escolher o melhor imóvel e  tornar o seu anúncio o mais atrativo possível.</p>
<p>Existem dezenas de personalizações possíveis para o anúncio, desde a quantidade mínima de dias, preço, quantidade de quartos, regras de cancelamento, taxa extra para hóspedes extras, exigência de verificação de identidade do locador, etc.</p>
<br>


<h2>🎯 Objetivo</h2>
<p>Construir um modelo de previsão de preço que permita:</p>
<ul>
	<li>O locatário, uma pessoa comum que possui um imóvel, saber quanto deve cobrar pela diária;</li>
	<li>O locador comum, saber se o preço está atrativo ou não para a hospedagem que está buscando;</li>
</ul>
<br>


<h2>📝 Materiais, inspirações e créditos</h2>
<p>As bases de dados foram retiradas do site <a href="https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro">Kaggle</a>, disponibilizadas pelo usuário <b>Allan Bruno.</b></p>
<p>As bases utilizadas no projeto foram baixadas na época de produção do curso e disponibilizadas na plataforma de ensino, para evitar resultados diferentes entre os alunos caso as bases no Kaggle fossem modificadas ao longo do tempo.</p>
<p>O curso também utiliza como referência a solução do usuário Allan Bruno, que pode ser visualizada <a href="https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb">neste notebook</a>, também no Kaggle.</p>
<p>A solução desenvolvida nesse projeto apresenta diferenças significativas em seu processo de construção, porém existem muitas semelhanças, como por exemplo:</p>
<ul>
	<li>As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês;</li>
	<li>Os preços são dados em reais (R$);</li>
	<li>As bases utilizadas são de abril de 2018 à maio de 2020, com exceção de junho de 2018 que não possui informações.</li>
</ul>
<br>


<h2>💭 Expectativas e considerações iniciais</h2>
<ul>
	<li>A sazonalidade pode ser um fator importante, visto que meses como dezembro podem ser bem caros no RJ;</li>
	<li>A localização do imóvel faz muita diferença no preço, já que no RJ as características do local mudam completamente dependendo da região (como segurança, paisagem, pontos turísticos, etc.);</li>
	<li>Adicionais/comodidades podem ter um impacto significativo, visto que existem muitos prédios e casas antigas no RJ;</li>
</ul>
<p>Esses fatores serão levados em consideração e analisados se de fato têm impacto sobre o valor dos imóveis, bem como outros pontos não tão intuitivos.</p>
<br>


<h2>Passo a passo do projeto</h2>
<ol>
	<li><a href="https://github.com/rodrishud/projeto-hashtag-dados/edit/main/README.md#%EF%B8%8F-contexto">Explicação do problema e do objetivo;</a> ✅</li>
	<li>Importação bibliotecas e bases de dados; ✅</li>
	<li>Identificação colunas que podem ser excluídas; ⬅️</li>
	<li>Tratamento de valores faltantes;</li>
	<li>Verificação tipos de dados em cada coluna;</li>
	<li>Análise exploratória e tratamento de outliers:
		<ul>
			<li>Dados numéricos contínuos e discretos;</li>
			<li>Dados de texto (categorias);</li>
			<li>Dados em lista;</li>
			<li>Dados em mapa;</li>
		</ul>
	<li>Encoding:</li>
		<ul>
			<li>Dados True ou False;</li>
			<li>Dados categoria texto;</li>
		</ul>
	<li>Modelo de previsão:</li>
		<ul>
			<li>Métricas de avaliação;</li>
			<li>Definição do tipo de modelo;</li>
			<li>Escolha dos modelos que serão testados;</li>
			<li>Treino e avaliação;</li>
		</ul>
	<li>Análise do melhor modelo;</li>
</ol>
<br>

  
<h3>Continua...</h3>
