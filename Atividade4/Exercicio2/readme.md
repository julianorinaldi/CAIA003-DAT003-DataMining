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
    c. Separe o dataset em teste (5%) e treino (95%). Use o método 'train_test_split' do sklearn; configure o parâmetro random_state=10.
    d. Treine um modelo de regressão linear múltipla no dataset de treino utilizando todas as variáveis (exceto 'Nome') para prever a 'PrecoVenda' e exiba os coeficientes do modelo.
    e. Avalie o modelo encontrado utilizando o dataset de teste. Calcule o R2 e MSE.
___
### Dataset Carros
   - [Dataset/datasetCarros[original].csv](Dataset/datasetCarros[original].csv)