# 🧩 Programação Orientada a Objetos (POO) em Python e IoT

Este documento apresenta os conceitos fundamentais de **Programação Orientada a Objetos (POO)** aplicados ao desenvolvimento de software e integração com hardware (Arduino/IoT), demonstrando como essa abordagem organiza, limpa e escala o seu código.

---

## 💡 O que é POO?

A **Programação Orientada a Objetos** é um paradigma de programação que utiliza "objetos" para representar dados e ações baseados no mundo real. 

Em vez de escrever um código linear com várias funções soltas, estruturamos o programa em blocos reutilizáveis chamados **Classes**, que servem como moldes para a criação de **Objetos**.

---

## 🌟 Os 4 Pilares da POO no Contexto de Hardware

### 1. Abstração
Isolar a complexidade. Para quem usa o código, não importa *como* o Python lê os bytes da porta serial do Arduino, importa apenas que o método `ler_sensor()` devolva o valor correto.

### 2. Encapsulamento
Proteger os dados internos do objeto. Restringe o acesso direto a certas variáveis para evitar que configurações críticas do hardware sejam alteradas acidentalmente por outras partes do código.

### 3. Herança
Reutilizar código. Se você tem uma classe base chamada `DispositivoIoT`, você pode criar classes filhas como `SensorTemperatura` ou `AtuadorRelé` que herdam as características gerais e adicionam funções específicas.

### 4. Polimorfismo
Permitir que classes diferentes respondam à mesma ação de formas diferentes. Por exemplo, chamar o método `conectar()` em um objeto do tipo `ConexaoSerial` executa um comportamento diferente de chamar `conectar()` em um objeto `ConexaoWiFi`.

---

## 🐍 Exemplo Prático em Python (Gerenciador do Arduino)

Veja como aplicar POO para criar uma estrutura organizada que gerencia a conexão serial com o seu Arduino:

```python
import serial
import requests

class ConectorArduino:
    """Classe responsável por gerenciar a comunicação com o Arduino."""
    
    def __init__(self, porta: str, velocidade: int = 9600):
        # Atributos (Características do objeto)
        self.porta = porta
        self.velocidade = velocidade
        self._conexao = None  # Atributo encapsulado (privado por convenção)

    def conectar(self):
        """Abre a conexão com a porta serial."""
        try:
            self._conexao = serial.Serial(self.porta, self.velocidade, timeout=1)
            print(f"✅ Conectado com sucesso na porta {self.porta}!")
        except Exception as e:
            print(f"❌ Erro ao conectar na porta {self.porta}: {e}")

    def ler_dado(self) -> str:
        """Lê e limpa o dado recebido do Arduino."""
        if self._conexao and self._conexao.is_open:
            linha = self._conexao.readline().decode('utf-8').strip()
            return linha
        return ""

    def fechar(self):
        """Fecha a conexão com segurança."""
        if self._conexao and self._conexao.is_open:
            self._conexao.close()
            print("🔌 Conexão serial encerrada.")


# 🚀 Execução do Código utilizando o Objeto
if __name__ == "__main__":
    # Instanciando o objeto (criando o gerenciador a partir do molde/classe)
    meu_arduino = ConectorArduino(porta="COM3")
    meu_arduino.conectar()
    
    API_URL = "https://exemplo.com"

    try:
        while True:
            dado_sensor = meu_arduino.ler_dado()
            if dado_sensor:
                print(f"📥 Dado do hardware capturado: {dado_sensor}")
                # Envia para a API externa
                requests.post(API_URL, json={"valor": dado_sensor})
    except KeyboardInterrupt:
        # Garante o fechamento da porta ao encerrar o script
        meu_arduino.fechar()
```

---

## 🎯 Vantagens de usar POO no seu Repositório

*   **Organização:** O código do script principal (`main.py`) fica muito mais limpo, pois a lógica pesada da conexão fica escondida dentro da classe.
*   **Reutilização:** Se você precisar conectar **dois ou três Arduinos** no mesmo computador, basta criar novas instâncias da classe:
    ```python
    arduino_sala = ConectorArduino(porta="COM3")
    arduino_cozinha = ConectorArduino(porta="COM4")
    ```
*   **Fácil Manutenção:** Se a forma de ler os dados mudar no futuro, você altera apenas a lógica dentro do método `ler_dado()`, sem quebrar o resto do projeto.
