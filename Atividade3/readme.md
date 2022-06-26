## A) Árvores de decisão

1. Objetivo: explorar a classificação de dados com árvores de decisão usando o software Orange.

2. Procedimentos:

    a. O dataset Soybean se refere ao diagnóstico de 19 doenças comuns da soja. Ele tem 35 atributos e 683 instâncias. Faça o pré-processamento necessário para upload no Orange.
      - Procedimento realizados:
        - Download do [arquivo original](https://moodle.dainf.ct.utfpr.edu.br/mod/resource/view.php?id=46926)
        - Pré-processamento:
          - Análise do arquivo e seus dados internos [Dataset/soybean[original].txt](Dataset/soybean[original].txt)
          - Separação entre descrição do dataset e dados [Dataset/soybean-describe.txt](Dataset/soybean-describe.txt)
          - Criação de arquivo .csv apenas com dados [Dataset/soybean.csv](Dataset/soybean.csv)
          - Extração das classes (colunas) e adequação ao .csv
          - Adição da coluna "class" ao final do dataset

    b. Utilizando as ferramentas de visualização de dados, o que é possível preliminarmente inferir preliminarmente sobre os atributos deste dataset?
      - Análise:
      ![Imagem](https://i.imgur.com/QQ3Ztay.png)
      - Não há dados numéricos.
      - Uso para classificação de dados.
      - Não está adequado para regressão.

    c. Selecione a coluna “class” como o alvo da classificação, sendo as demais colunas os atributos previsores. Use validação cruzada estratificada de 5-folds para o treinamento de uma Árvore de Decisão com os parâmetros default. Anote o tamanho da árvore obtida (número total de nós, profundidade e número de nós-folhas) e as medidas de qualidade (acurácia, precision, recall e F1 score). Justifique qual a medida de qualidade adequada para este caso.
      - Selecione a coluna “class” como o alvo da classificação, sendo as demais colunas os atributos previsores
      ![Imagem](https://i.imgur.com/lPAevjv.png)
      - Use validação cruzada estratificada de 5-folds para o treinamento de uma Árvore de Decisão com os parâmetros default
      ![Imagem](https://i.imgur.com/xiz8HcA.png)
      - Árvore resultado
      ![Imagem](https://i.imgur.com/Qv6caoT.png)
      - Tamanho da árvore:
        - 96 nós
        - 41 folhas
        - profundidade: 14
      - Medidas de qualidade:
        - Acurácia: 74,8 % 
        - Precision: 75,3 %
        - Recall: 74,8 %
        - F1: 70,6 %
      - Analisaremos pela Acurácia, que determina o quanto de acerto a árvore de decisão terá sucesso no modelo.

    d. Mostre a matriz de confusão gerada pelo treinamento/teste da árvore de decisão. Identifique nesta árvore quais foram as classes que tiveram 100% e 0% de acerto, respectivamente. Justifique este comportamento (em especial para as classes com 0% de acerto).
      - Matriz de confusão gerada:
      ![Imagem](https://i.imgur.com/wYNtsDE.png)
      - Matriz de confusão classes 100% e 0% de acerto:
      ![Imagem](https://i.imgur.com/AEukZgS.png)
      -  