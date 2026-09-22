# PowerGrid Core ⚡ 
**Módulo:** Manutenção Preditiva (Tema D)

O **PowerGrid Core** é o núcleo computacional concebido para processar e indexar dados críticos de telemetria gerados por sensores numa rede elétrica. Este repositório contém a implementação da **Etapa N1**, focada na organização de dados, eficiência algorítmica e identificação de padrões de falha iminente (Manutenção Preditiva).

Projeto desenvolvido no âmbito da disciplina de Algoritmos e Estruturas de Dados II, do curso de Engenharia de Software da UniAlfa.

## 🚀 Funcionalidades Implementadas

O sistema opera através de uma interface de linha de comandos (CLI) e cumpre os seguintes requisitos algorítmicos:

*   **Ingestão de Dados:** Geração em tempo de execução de telemetria simulada (ID do Sensor, Timestamp, Tensão e Temperatura), incluindo a injeção controlada de anomalias.
*   **Ordenação Simples $O(n^2)$:** Implementação de **Insertion Sort** para organizar os dados por métricas de tensão.
*   **Ordenação Eficiente $O(n \log n)$:** Implementação de **Quick Sort** para ordenar massivamente os equipamentos pelo identificador (ID), garantindo a escalabilidade do sistema.
*   **Pesquisa Otimizada $O(\log n)$:** Motor de **Busca Binária** que exige ordenação prévia para localizar instantaneamente qualquer sensor na rede.
*   **Indexação Hierárquica:** Representação da topologia da rede através de uma **Árvore de Busca Binária (BST)**, utilizando o percurso **Em-Ordem** para exportar a hierarquia de forma estruturada.
*   **Motor de Diagnóstico:** Sistema de regras de negócio que isola equipamentos fora dos limites seguros (Tensão fora de 198.0V - 242.0V ou Temperatura acima de 60.0°C).

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Paradigma:** Programação Orientada a Objetos (POO)
*   **Interface:** CLI (Command Line Interface) nativa no terminal

## ⚙️ Como Executar o Projeto

1.  Certifique-se de que tem o Python instalado na sua máquina.
2.  Clone este repositório ou descarregue o ficheiro fonte.
3.  Abra o terminal na pasta do projeto e execute o ficheiro principal:

```bash
python "MANUTENCAO PREDITIVA SENSORES.py"
```

4. O sistema irá gerar automaticamente um lote de 15 leituras e apresentar o menu interativo:
   * **[1] e [2]:** Testam os algoritmos de ordenação.
   * **[3]:** Permite pesquisar um ID específico (ex: `S045`).
   * **[4]:** Constrói a árvore topológica e imprime o relatório em-ordem.
   * **[5]:** Apresenta o relatório de hardwares críticos.

## 👨‍💻 Autor

**Marco Antonio Oliveira Cavaco**  
Estudante de Engenharia de Software
