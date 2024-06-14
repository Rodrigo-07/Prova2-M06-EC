# Prova2-M06-EC

Prova do Rodrigo de programação do Módulo 06, turma 08 de Engenharia da Computação - 14/06/2024

O objetivo da prova era desenvolver um algoritmo capaz de detectar faces em um vídeo, tomando cuidado com falsos positivos.

## Como utilizar

Para rodar o modelo de detecção de rostos, basta clonar o repositorio e rodar `python3 src/main.py`

O resultado final pode ser avaliado em src/video_final.mp4


## Resposta das perguntas técnicas

### 2.1

**Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.**

O método que eu escolhi foi o haar cascade. Ele utiliza "Haars" que são  áreas retangulares onde é calculado a diferenças de inetensidade pixels adjacentes a essa área retangular, utilizando convoluções. Para detectar um certo objeto, utilizamos um classificador já treinados com muitas imagens que contem os valores certos valores que sempre aparecem para aquele obejto. Esse classificador calcula essa diferença em cascata para a rápida detecção.

### 2.2

**Considere as seguintes alternativas para resolver o problema de detecção de faces:**

    HAAR Cascade
    CNN
    NN Linear
    Filtros de correlação cruzada

**Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.**

Vou fazer a avaliação em três nívesi: Alta, média e baixa.

1. CNN 
   1. Avaliação: 
      1. Viabilidade Técnica: Alta
      2. Facilidade de Implementação: Baixa
      3. Versatilidade: Alta
   2. Justificativa:
      1. CNNs são ótimas para captar mais detalhes, caracteristacas e padrões da imagem dessa forma a aplicaão dela para detecção de faces é uma ótima escolha, já que o rosto de alguem varia muito de pessoa para pessoa e pode estar em diferentes angulos na imagem. Porém, por serem mais complexas são mais difíceis de implementar.
2. HAAR Cascade
   1. Avaliação: 
      1. Viabilidade Técnica: Alta
      2. Facilidade de Implementação: Alta
      3. Versatilidade: Média
   2. Justificativa:
      1. Haar Cascade consegue resolver o problema de detecção de rostos em diversos casos, especialmente quando temos imagem claras e de frente das pessoas. Além disso, elas são muitos fáceis de serem implementadas devido o algoritimo que ela usa, podendo ser utilizada até em microcontroladores, por exemplo. O principal problema é que ela usa metodo de como fosse uma "comparação", fazendo com que ela não consiga se adaptar a muitos cenários.
3. Filtros de correlação cruzada
   1. Avaliação: 
      1. Viabilidade Técnica: Baixa
      2. Facilidade de Implementação: Alta
      3. Versatilidade: Baixa
   2. Justificativa:
      1. Nesse tipo de detecção eu utilizo um kernel que é o que eu quero detectar e fazer a correlação cruzada sobre a imagem aonde eu quero detectar esse kernel. Dessa forma faz com que ela não se aplica a muitos tipos de rostos e nem angulos diferentes que esse rosto pode estar, já que ela tem um kernel espefico. Isso também implica na baixa versatilidade. Porém, por sua implementação ser basicamente fazer operações de matrizes, conseguimos fazer isso de maneira mais fácil.
4. NN Linear
   1. Avaliação: 
      1. Viabilidade Técnica: Baixa
      2. Facilidade de Implementação: Alta
      3. Versatilidade: Baixa
   2. Justificativa:
      1. Redes neurais lineares têm capacidades muito mais limitadas do que uma CNN devido a fato dela não conseguir capturar relações não lineares, fazendo com que ela não consiga se adaptar as vários tipos de imagens. A única vantagem desse metodo, é a facilidade de implementar o que pode ser bom em casos onde as imagens tem um padrão bem definido e são simples.

### 2.3

**Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.**

Em relaão ao 2.2, aqui o que vai mudar vai ser apenas a viabilade técnica então vou focar apenas nisso.

1. CNN:
   1. Justificativa:
      1. Como foi explicado antes, as CNNs conseguem capturar muitas mais relações, caracteristicas e padrões na imagem assim ajudando na hora de capturar detalhes como microexpressões fraciais e correlacionar esses diferentes elementos para detectar a emoção.
2. HAAR Cascade
   1. Justificativas:
      1. Apesar do haar cascade não ser o melhor metodo para capturar pequenas váriações em imagens, nesse caso expressões, podemos utilizar mais de um tipo de haar cascade para fazer uma validação. Por exemplo, utilizar um haar cascade para detectar um rosto aí depois apenas no frame do rosto rodar outro haar cascade para detectar as expressões.
3. NN Linear
   1. Justificativa:
      1. Seguindo uma estratégia parecida com a explicada acima, se já tivermos o rosto conseguimos pegar emoções mais básicas e mais expressivas como uma pessoa muito alegre ou muito triste, por possuirem padrões mais detectáveis.
4. Filtros de correlação cruzada:
   1. Justificativa:
      1. Por utilizarem um kernel único e as emoções váriarem muito, isso complica a detecção de emoções com esse método.

### 2.4

**  **

Acredito que nenhum dos método faz essa correlação entre frames já que geralmente passamos frame a frame pelo metodo. Acredito que tenha funções já prontas para essa consideração temporal dos frames em bibliotecas como tensorflow. Porém, poderiamos adicionar um algoritimo que guarda a localização das faces dos últimos frames e "foca" nas proximidades desses frames quando for analisar o próximo frame.