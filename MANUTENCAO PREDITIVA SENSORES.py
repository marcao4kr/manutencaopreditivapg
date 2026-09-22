import random

TENSAO_MIN = 198.0
TENSAO_MAX = 242.0
TEMPERATURA_MAX = 60.0

class LeituraSensor:
    def __init__(self, id_sensor, timestamp, tensao, temperatura):
        self.id_sensor = id_sensor
        self.timestamp = timestamp
        self.tensao = tensao
        self.temperatura = temperatura

    def __str__(self):
        return (f"{self.id_sensor} | {self.timestamp} | "
                f"{self.tensao:6.1f} V | {self.temperatura:5.1f} C")

class NoArvore:
    def __init__(self, leitura):
        self.leitura = leitura
        self.esq = None
        self.dir = None

class ArvoreRede:
    def __init__(self):
        self.raiz = None

    def inserir(self, leitura):
        if self.raiz is None:
            self.raiz = NoArvore(leitura)
        else:
            self._inserir_recursivo(self.raiz, leitura)

    def _inserir_recursivo(self, no, leitura):
        if leitura.id_sensor < no.leitura.id_sensor:
            if no.esq is None:
                no.esq = NoArvore(leitura)
            else:
                self._inserir_recursivo(no.esq, leitura)
        elif leitura.id_sensor > no.leitura.id_sensor:
            if no.dir is None:
                no.dir = NoArvore(leitura)
            else:
                self._inserir_recursivo(no.dir, leitura)

    def percurso_em_ordem(self, no, resultado=None):
        if resultado is None:
            resultado = []
        if no:
            self.percurso_em_ordem(no.esq, resultado)
            resultado.append(no.leitura)
            self.percurso_em_ordem(no.dir, resultado)
        return resultado


def insertion_sort(lista, chave):
    vetor = lista[:]
    n = len(vetor)
    for i in range(1, n):
        atual = vetor[i]
        valor_chave = getattr(atual, chave)
        j = i - 1
        while j >= 0 and getattr(vetor[j], chave) > valor_chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = atual
    return vetor

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[len(lista) // 2]
    valor_pivo = getattr(pivo, chave)
    
    esq = [x for x in lista if getattr(x, chave) < valor_pivo]
    meio = [x for x in lista if getattr(x, chave) == valor_pivo]
    dir = [x for x in lista if getattr(x, chave) > valor_pivo]
    
    return quick_sort(esq, chave) + meio + quick_sort(dir, chave)

def busca_binaria(lista_ordenada, chave, valor_alvo):
    esq = 0
    dir = len(lista_ordenada) - 1

    while esq <= dir:
        meio = (esq + dir) // 2
        valor_meio = getattr(lista_ordenada[meio], chave)

        if valor_meio == valor_alvo:
            return lista_ordenada[meio]
        elif valor_meio < valor_alvo:
            esq = meio + 1
        else:
            dir = meio - 1
            
    return None


def gerar_leituras_simuladas(quantidade=15):
    leituras = []
    base_ano = 2026

    for i in range(quantidade):
        id_sensor = f"S{str(random.randint(1, 999)).zfill(3)}"
        timestamp = f"{base_ano}-09-10 08:{str(random.randint(0, 59)).zfill(2)}"

        if random.random() < 0.75:
            tensao = round(random.uniform(210.0, 230.0), 1)
            temperatura = round(random.uniform(35.0, 55.0), 1)
        else:
            tensao = round(random.uniform(180.0, 260.0), 1)
            temperatura = round(random.uniform(58.0, 80.0), 1)

        leituras.append(LeituraSensor(id_sensor, timestamp, tensao, temperatura))
    return leituras

def detectar_criticos(lista):
    criticos = []
    for leitura in lista:
        motivos = []
        if leitura.tensao < TENSAO_MIN or leitura.tensao > TENSAO_MAX:
            motivos.append("Tensão fora da faixa")
        if leitura.temperatura > TEMPERATURA_MAX:
            motivos.append("Temperatura elevada")
        if motivos:
            criticos.append((leitura, motivos))
    return criticos


def exibir_leituras(lista, titulo):
    print(f"\n{titulo}")
    print("-" * 55)
    for leitura in lista:
        print(leitura)

def exibir_criticos(criticos):
    print("\nLEITURAS CRÍTICAS DETECTADAS (ALERTA DE MANUTENÇÃO)")
    print("-" * 55)
    if not criticos:
        print("Nenhuma leitura crítica encontrada.")
        return
    for leitura, motivos in criticos:
        print(f"{leitura}  -> {', '.join(motivos)}")

def menu():
    print("\n=== PowerGrid Core - Tema D: Manutenção Preditiva ===")
    print("1. [Insertion Sort] Ordenar por tensão")
    print("2. [Quick Sort] Ordenar por ID do Sensor (Eficiente)")
    print("3. [Busca Binária] Localizar Sensor por ID")
    print("4. [Árvore BST] Inserir dados na Árvore e listar Em-Ordem")
    print("5. [Manutenção] Mostrar relatórios críticos")
    print("6. Mostrar leituras originais (desorganizadas)")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    leituras = gerar_leituras_simuladas(15)
    
    arvore_rede = ArvoreRede()
    for leitura in leituras:
        arvore_rede.inserir(leitura)

    while True:
        opcao = menu()

        if opcao == "1":
            ordenadas = insertion_sort(leituras, "tensao")
            exibir_leituras(ordenadas, "ORDENADO POR TENSÃO (INSERTION SORT)")
            
        elif opcao == "2":
            ordenadas = quick_sort(leituras, "id_sensor")
            exibir_leituras(ordenadas, "ORDENADO POR ID SENSOR (QUICK SORT)")
            
        elif opcao == "3":
            ordenadas = quick_sort(leituras, "id_sensor")
            alvo = input("Digite o ID do Sensor para buscar (ex: S045): ").upper()
            
            resultado = busca_binaria(ordenadas, "id_sensor", alvo)
            if resultado:
                print(f"\nSensor Localizado: {resultado}")
            else:
                print("\nSensor não encontrado na base de dados.")
                
        elif opcao == "4":
            percurso = arvore_rede.percurso_em_ordem(arvore_rede.raiz)
            exibir_leituras(percurso, "HIERARQUIA DA REDE (PERCURSO EM-ORDEM DA ÁRVORE BST)")
            
        elif opcao == "5":
            criticos = detectar_criticos(leituras)
            exibir_criticos(criticos)
            
        elif opcao == "6":
            exibir_leituras(leituras, "LEITURAS BRUTAS RECEBIDAS DA REDE")
            
        elif opcao == "0":
            print("Encerrando o PowerGrid Core...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()