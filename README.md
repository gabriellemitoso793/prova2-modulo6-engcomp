# prova2-modulo6-engcomp

## Perguntas técnicas

1. 
O método de identificação de imagens Haar Cascade funciona através da visualização das áreas do frame com um foco na intensidade do pixel. Dessa forma, é através da detecção da diferença de intensidades entre duas áreas escolhidas que a identificação das faces, ou, até mesmo, de um objeto acontece. O método é bastante utilizado em drones, robôs e celulares. Assim, chegamos a conclusão de que, o Haar Cascade é versátil e cumpre bem o papel de identificar as faces no vídeo da Fifa. 

2. 
Ordem, do melhor para o pior: Haar Cascade, CNN, Filtros de correlação cruzada e NN Linear.

Haar Cascade: O método Haar Cascade é mais fácil de implementar e entrega bons resultados em termos técnicos. Além disso, é mais versátil de ser utilizado em imagens com diferentes iluminações.

CNN: O método CNN funciona bem para a detecção de faces devido à sua capacidade de identificar características específicas nas imagens. Mas, devido a dificuldade de implementação, se torna menos versátil.

Filtros de correlação cruzada: Os filtros de correlação cruzada podem ser utilizados para a detecção, mas são menos viáveis porque dependem da iluminação da imagem.

NN Linear: As redes neurais lineares é o método menos viável entre todos, pois tem uma capacidade pequena de identificar padrões nas imagens através da classificação.


3.  
Para identificar aspectos específicos como a detecção de emoções através da imagem de uma face, o CNN é o mais indicado, pois o modelo consegue identificar caracteristicas específicas de uma imagem. Em segundo lugar, fica o Haar Cascade, pois, ainda que ele tenha limitações em capturar detalhes mais específicos da face, ele ainda funciona melhor na detecção. Já em terceiro lugar, fica o NN Linear, pois ele apenas identifica através de classificação. Por fim, em quarto lugar, fica os filtros de correlação cruzada, pois, devideo à sua falta de capacidade de modelar, não conseguiria identificar as emoções.

4.
Nenhum dos métodos tem capacidade de gravar mudanças de expressões na variação dos frames, isso ocorre porque os métodos de classificação analisam frame a frame sem necessariamente ser algo continuado. Dessa forma, uma alteração que poderia ser feita é a combinação de métodos diferentes, por exemplo, primeiro pode-se usar um Haar Cascade para identificar se há face, após isso, pode-se usar um CNN para procurar características específicas como um sorriso. Assim, é mais provável ter garantias de um método que funciona. 


5. 
A bola de ouro eu não sei, mas no Grammy 2024, o Song of The Year é da Taylor Swift!

## Parte prática

### Objetivo

Implementar um modelo de detecção para idenificar faces no vídeo da Fifa.

### Lógica

Foram utilizados dois métodos diferentes de Haar Cascade:

> haarcascade_frontalface_default

> haarcascade_eye

Um que identifica faces de frente e outro que identifica olhos, pois, ambos juntos conseguem evitar falsos positivos

### Instalação e Configuração

1. **Clone o Repositório:**
Primeiro é necesário clonar o repositório, para isso, acesse o terminal do seu computador e execute os seguintes comandos:

   ```bash
   git clone https://github.com/gabriellemitoso793/prova2-modulo6-engcomp.git
   cd prova2-modulo6-engcomp
   ```
2. **Crie um ambiente virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Baixe todas as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Rode o arquivo**:
    ```bash
    python3 convert_video_fifa.py
    ```


## Visualização do vídeo

https://drive.google.com/file/d/1Nihn-DPwQyESYrO4yXORLtj7vOhf8xej/view?usp=sharing