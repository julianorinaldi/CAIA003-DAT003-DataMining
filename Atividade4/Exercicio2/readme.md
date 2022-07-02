## B) Regressão
___
3. Dados: use o dataset 'datasetCarros.csv' em todos os exercícios.
___
4. Objetivo: explorar os conceitos de regressão.
___
5. Questões:
    a. Faça um modelo de regressão linear simples utilizando a variável 'KmRodado' para prever a 'PrecoVenda'.
    ![](https://i.imgur.com/khdsW4p.png)
    ___
    b. Calcule o R2 para o modelo criado.
       - R2: 0.0008518862620293666
    ![](https://i.imgur.com/EIUOZdP.png)
    ___
    c. Separe o dataset em teste (5%) e treino (95%). Use o método 'train_test_split' do sklearn; configure o parâmetro random_state=10.
    ![](https://i.imgur.com/UsitHGi.png)
    ___
    d. Treine um modelo de regressão linear múltipla no dataset de treino utilizando todas as variáveis (exceto 'Nome') para prever a 'PrecoVenda' e exiba os coeficientes do modelo.
    ![](https://i.imgur.com/cG5oRF4.png)
    ![](https://i.imgur.com/Fvuxv0Z.png)
    ___
    e. Avalie o modelo encontrado utilizando o dataset de teste. Calcule o R2 e MSE.
      - Coeficiente: [ 8.40174424e-01, -7.57888404e-04, 6.57984636e-05, -7.15540633e-01]
      - Mean squared error: 29.83
      - R2 (ou coeficiente de determinação): -0.1014
      - Validação cruzada -267.7867
    ___
___
### Dataset Carros
   - [Dataset/datasetCarros[original].csv](Dataset/datasetCarros[original].csv)

### Google Colab
   - [B) Regressão (a) até (e)](https://colab.research.google.com/drive/1HIy2GjizyzUX-dkZDiZ3bzAKO7Qq6syj?usp=sharing)