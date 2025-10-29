import requests
import json
from datetime import datetime

class MonitorCEP:
    """
    Uma classe para monitorar e consultar endereços usando a API ViaCEP.
    Isso demonstra __init__, self, métodos, atributos e __str__.
    """

    API_BASE_URL = "https://viacep.com.br/ws/"

    def __init__(self, nome_monitor):
        self.nome_monitor = nome_monitor
        self.historico_consultas = []

        self.chaves_esperadas = {'cep', 'logradouro', 'bairro', 'localidade', 'uf'}

    def _adicionar_log(self, mensagem):
        """Um método "privado" para adicionar logs ao histórico"""

        agora = datetime.now()
        timestamp = agora.strftime("%Y-%m-%d %H:%M:%S")

        log_final = f"[{timestamp}] {self.nome_monitor}: {mensagem}"

        self.historico_consultas.append(log_final)
        print(log_final)

    def consultar_cep(self, cep):
        """
        Consulta um CEP na API.
        Isso demonstra try/expect, requests, json, if/else e 'set'.
        """

        url_completa = f"{self.API_BASE_URL}{cep}/json/"
        self._adicionar_log(f"Iniciando consulta para o CEP: {cep}...")

        try:
            resposta = requests.get(url_completa, timeout=5)

            if resposta.status_code == 200:

                dados_endereco = resposta.json()

                if 'erro' in dados_endereco:
                    self._adicionar_log(f"Falha: CEP {cep} não encontrado na base de dados.")
                    return None 
                
                self._adicionar_log("Consulta bem-sucedida.")

                chaves_recebidas = set(dados_endereco.keys())
                chaves_faltando = self.chaves_esperadas - chaves_recebidas

                if chaves_faltando:
                    self._adicionar_log(f"Alerta: A resposta não incluiu as chaves: {chaves_faltando}")
                
                return dados_endereco
            
            else:
                self._adicionar_log(f"Falha: O servidor respondeu com status {resposta.status_code}")
                return None
            
        except requests.exceptions.Timeout:
            self._adicionar_log("Erro Crítico: A requisição demorou demais (Timeout).")
        except requests.exceptions.RequestException as e:
            self._adicionar_log(f"Erro Crítico de conexão:{e}")
        except json.JSONDecodeError:
            self._adicionar_log("Erro Crítico: A resposta do servidor não foi um JSON válido")

        return None
    
    def imprimir_historico(self):
        """Demonstra um loop 'for' em uma lista. """
        print(f"/n--- Histórico completo de {self.nome_monitor} ---")

        for log in self.historico_consultas:
            print(log)

    def __str__(self):
        """Método mágico para 'print(objeto)'."""
        return f"Objeto MonitorCEP(Nome='{self.nome_monitor}', Consultas={len(self.historico_consultas)})"
    
def main():
    """Função principal que executa o programa."""

    monitor = MonitorCEP(nome_monitor="Logística-SP")

    print("--- Sistema de Monitoramento de Endereços ---")

    while True:
        print("/n--- Menu ---")
        print("1: Consultar novo CEP")
        print("2: Ver histórico de logs")
        print("Sair: Fechar o programa")

        escolha = input("Digite sua opção: ").strip().lower()

        if escolha == '1':
            cep = input("Digite o CEP (apenas números): ").strip()

            if len(cep) == 8 and cep.isdigit():
                endereco = monitor.consultar_cep(cep)

                if endereco:
                    print("/n--- Endereço Encontrado ---")
                    for chave, valor in endereco.item():
                        print|(f"  {chave}: {valor}")
            else:
                print("Entrada Inválida. O CEP deve conter 8 números.")

        elif escolha == '2':
            monitor.imprimir_historico()

        elif escolha == 'sair':
            print("Encerrando o sistema...")
            break

        else:
            print("Opçao inválida. Tente novamente")

    monitor.imprimir_historico()
    print("Sistema encerrado.")

if __name__ == '__main__':
    main()


    #   !!!!!!  GERAR UM CPF ALEATORIO PARA USAR NO PYTHON ACIMA ^^^   !!!!!!!

import random

numero_aleatorio = random.randint(1000001, 9999999)

cep_str = str(numero_aleatorio)

cep_str_completo = cep_str.zfill(8)

cep_formatado = f"{cep_str_completo[0:5]}-{cep_str_completo[5:]}"

print(f"O CEP aleatório gerado foi: {cep_formatado}")



