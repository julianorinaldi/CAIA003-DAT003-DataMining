## A) Classificação

1. Objetivo: explorar a classificação de dados com árvores de decisão árvores de decisão utilizando validação cruzada, Knn e redes neurais
___
2. Questões:

    2.1. Considere ainda uma árvore de decisão para classificar se um indivíduo sobreviveu ou não com base no dataset “titanic.csv”. Qual o resultado médio de acurácia e F1-score utilizando a estratégia de validação cruzada 5-fold? Discuta os resultados.
    ___
      - Resultados:
      ![](https://i.imgur.com/tacAdNx.png)
        - Acurácia: 76,6%
        - F1-score: 76,3%
      - Discussão:
      ![](https://i.imgur.com/tG2t7qQ.png)
        - Em uma análise de árvore simples é possível perceber que mulheres da classe 1 quase todas viveram.
    ___
    2.2. Ainda considerando o dataset “titanic.csv”, construa um modelo utilizando k-NN para prever se uma pessoa sobreviveu ou não. Considere diferentes valores de k vizinhos: k={2,3,4,5,6,7}. Use validação cruzada 5-fold na avaliação. Houve variação significativa nos diferentes modelos testados? Algum deles foi melhor do que a estratégia baseada em árvore de decisão?
    ___
      - Resultados:
      ![](https://i.imgur.com/vl3koJm.png)
      - Discussão:
        - A árvore se manteve com valores mais acertivos que o modelo KNN {2 a 7 vizinhos}.
    ___
    2.3. Avalie o resultado de uma rede neural com, pelo menos, duas camadas escondidas e dez neurônios em cada. Use validação cruzada
      - Resultados:
      ![](https://i.imgur.com/a8DjNpl.png)
      - Caso usar rede neural com todos os dados, realmente tem um resultado melhor que outros modelos.
      ![](https://i.imgur.com/EeNI0Dy.png)
      - Caso usar uma separação para treinamento e teste, na proporção de 30% x 70%, a rede neural teve um melhor acerto nos resultados.
___
### Dataset Titanic
   - [Dataset/titanic[original].csv](Dataset/titanic[original].csv)

### Arquivo para download (orange)
   - [titanic.ows](titanic.ows)