## A) Análise Associativa (I)
___
![](https://i.imgur.com/2Y4980U.png)
Objetivo: O dataset bebê-baixo-peso foi construído com base no Very Low Weigth Infants Dataset e registra dados de 671 bebês com peso ao nascer abaixo de 1600 gramas. Há dados sobre a mãe e o bebê incluindo alguns medicamentos utilizados, questões relacionadas ao parto, problemas diagnosticados no nascituro, e se o mesmo sobreviveu ou não ao parto. Na literatura médica, já são conhecidos alguns fatores que diminuem as chances de sobrevida de bebês prematuros, por exemplo: bebês com extremo baixo peso (<1000 gramas), aqueles nascidos muito prematuramente (<27 semanas de idade gestacional), e presença de comorbidades tais como pneumotórax ou complicações cardio-pulmonares resultantes da própria imaturidade pulmonar. 

Deseja-se, portanto, utilizar os métodos de regras de associação para descobrir associações relevantes que não sejam óbvias.
___
a. Caso seja utilizado o Orange, é necessário reformatar o dataset para o formato “Basket” (mais informacões aqui e aqui). Caso escolha o software Weka, utilize o algoritmo de associação hotSpot (instalável através do Package Manager), com support=1 (ou muito próximo deste valor), outputRules=True, maxBranchingFactor<5 e ajuste o consequente da regra para a variável Dead através da opção target e targetIndex (=1 ou 2 para Died=no ou Died=yes). Opcionalmente, pode ser utilizado Python.
___
b. Em vez de regras genéricas, há interesse especial em descobrir regras que mostrem alguma associação entre o uso de beta-methasone pela gestante e a sobrevivência, ou não, do bebê-baixo-peso. Observe as regras encontradas pelo algoritmo e investigue se o resultado tem algum fundamento (Pesquise no Google!!).
___
c. Fato importante: este dataset foi coletado na Duke University Medical Center no Estado da Georgia (USA), sendo este um dos estados americanos onde há uma grande concentração de afro-descendentes. Com isto em mente, obtenha regras de associação (com pelo menos 20% de suporte) que envolvam uma eventual relação entre raça e a prevalência, ou não, de morte de bebês-baixo-peso). Discuta as implicações sociais dos achados.
___
### Dataset XXXXXXXXXXXX
   - [XXXXXXXXXXXX.csv](Dataset/XXXXXXXXXXXX.csv)