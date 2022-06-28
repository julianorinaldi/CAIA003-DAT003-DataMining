## B) Regras de classificação

3. Objetivo: explorar a classificação de dados com árvores de decisão e regras de classificação com o software Orange.

4. Procedimentos:
    a. Utilize o [Contraceptive Method Choice Dataset](https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice), disponível no Machine Learning Repository. O objetivo aqui é predizer o método contraceptivo utilizado por mulheres da Indonésia, com base em indicadores demográficos e sócio-econômicos. O dataset tem 1473 instâncias e 9 atributos previsores, e 3 classes desbalanceadas (No-use, Long-term e Short-term).

      - Procedimento realizados:
        - Análise do dataset observando dados.
        - Análise da documentação sobre o dataset.
        - Adição da coluna cabeçário no arquivo [cmc[preparado].data](Dataset/cmc[preparado].data) para prepará-lo ao uso.
        - Criação do projeto no Orange [contraceptive-method-choice.ows](contraceptive-method-choice.ows)
          - Widget CSV File Import para aquivo `cmc[preparado].data`
          - Widget Edit Domain para definir tipo de dados
          - Widget Data Table para ver o dados
          - Widget Select Columns para definir a classe target
          - Widget para análise de dados (vários)

          ![Imagem](https://i.imgur.com/YZWBrVw.png)

    b. Utilizando as ferramentas de visualização de dados, o que é possível preliminarmente inferir preliminarmente sobre os atributos deste dataset?
      - Análise:
        - Os dados estão bem distribuídos e próximos, é difícil inferir algo apenas olhando aos dados.

    c. Utilizando a ferramenta de discretização, faça um pré-processamento dos atributos numéricos wifes_age e number_chd_born, discretizando os dados em faixas com igual frequência, respectivamente em: {jovem, adulta, madura, meia-idade} e {1, 2, 3_4, 5+}.

      - Procedimentos:
        - Widget Discretize

        ![Imagem](https://i.imgur.com/jMdXNoZ.png)

          - Atributo `wife-age`: Equal-frequency discretization -> Namber of intervals: 4
          - Atributo `number-children-born`: Equal-frequency discretization -> Namber of intervals: 4
          
        - Widget Edit Domain
          - Atributo `wife-age`: {jovem, adulta, madura, meia-idade}
          - Atributo `number-children-born`: {1, 2, 3_4, 5+}
          
          ![Imagem](https://i.imgur.com/5xy2CtX.png)
          ![Imagem](https://i.imgur.com/034NEYl.png)

        - Widget Data Table (visualizar dados)
        
        ![Imagem](https://i.imgur.com/Jfwn2fR.png)
    
    d. Utilize os algoritmos baseline (ZeroRule e OneRule) para estabelecer um referencial de comparação acerca da qualidade da classificação. Anote as métricas de qualidade (acurácia, precision, recall e F1 score).

      - Procedimentos:
        - Algoritmo ZeroRule: nenhuma regra
          - Simplesmente prediz a classe da maioria.
          - Se o número de instâncias por classe for balanceado, qualquer classe pode ser usada
          - Acurácia ZeroRule
            - Quantidade de classes: 3 `1=No-use, 2=Long-term, 3=Short-term`
            - Quantidade de instâncias: 1473
            - Agrupamento:
              - No-use	629
              - Long-term	333
              - Short-term	511
            - Acurácia: 333/1473 = 22,60% (na pior hipótese)

            ![Imagem](https://i.imgur.com/yHDZolE.png)

          - Algoritmo OneRule: regra um
          - Aplica o classificador usando apenas o atributo de maior maior importância (que minimiza a entropia ou outra medida)
          - Acurácia OneRule
            - Análise com Widget Rank
              - feature `number-children-born` teve melhor acurácia.
             
            ![Imagem](https://i.imgur.com/qcjDuIP.png)

            ![Imagem](https://i.imgur.com/awsEXcC.png)

            - Resultados:
              - Acurácia: 47,5%
              - Precision: 36,1%
              - Recall: 47,5%
              - F1 score: 40,20%

    e. Utilize o CN2 para gerar regras de classificação que sejam compreensíveis e interessantes (mas, não óbvias). Com base nestas regras, contextualize e esclareça o perfil (sócio-econômico e cultural) das usuárias de métodos contraceptivos short_term e principalmente long_term na Indonésia.

      - Análise:
        - `short_term` aparenta ser usado para mulheres com com edução mais básica

        ![Imagem](https://i.imgur.com/D7pMZVm.png)

        - `long_term` aparenta ser usado para mulheres com com edução mais completa
        
        ![Imagem](https://i.imgur.com/w7KcbBA.png)

    f. Compare a qualidade preditiva dos três métodos (ZeroRule, OneRule e CN2).

      - Análise:
        - ZeroRule: 22,60%
        - OneRule: 47,5%
        - CN2: 47,5%
      - OneRule e CN2 tiverem mesmo resultados.

    g. Gere uma árvore de decisão com uma profundidade que permita a sua compreensão. Compare o resultado aqui obtido com as regras de classificação anteriormente obtidas e discuta os pontos positivos e negativos das duas abordagens (árvores X regras) em termos de qualidade preditiva e compreensibilidade.

      - Análise:
        - Usando uma árvore de decisão com todos as feature, resultou em mesma acurácia que uma árvore apenas com feature `number-children-born` com 47,5%, sendo assim, a maior acurácia conseguida nos métodos utilizados fica em 47,5%.