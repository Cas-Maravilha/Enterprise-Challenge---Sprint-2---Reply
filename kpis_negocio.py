import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import datetime as dt

class KPIsNegocio:
    """Implementa KPIs de negócio para modelos de IA"""
    
    def __init__(self, targets=None):
        # Valores-alvo para KPIs de negócio
        self.targets = targets or {
            'roi': 2.5,                # Retorno sobre investimento
            'custo_por_erro': 100.0,   # Custo médio por erro em unidades monetárias
            'economia_recursos': 0.3,   # Economia de recursos (30%)
            'tempo_resposta': 0.5,     # Tempo de resposta em segundos
            'satisfacao_usuario': 4.2  # Escala de 1-5
        }
        
        # Histórico de KPIs
        self.historico = []
    
    def calcular_roi(self, custo_implementacao, economia_mensal, periodo_meses=12):
        """
        Calcula o ROI do modelo
        
        Args:
            custo_implementacao: Custo total de implementação
            economia_mensal: Economia mensal gerada pelo modelo
            periodo_meses: Período de análise em meses
            
        Returns:
            float: ROI calculado
        """
        beneficio_total = economia_mensal * periodo_meses
        roi = (beneficio_total - custo_implementacao) / custo_implementacao
        
        return roi
    
    def calcular_custo_erros(self, y_true, y_pred, custo_fp=100, custo_fn=500):
        """
        Calcula o custo dos erros do modelo
        
        Args:
            y_true: Valores reais
            y_pred: Valores previstos
            custo_fp: Custo de um falso positivo
            custo_fn: Custo de um falso negativo
            
        Returns:
            dict: Custos calculados
        """
        cm = confusion_matrix(y_true, y_pred)
        
        if len(cm) == 2:  # Caso binário
            tn, fp, fn, tp = cm.ravel()
            
            # Custos totais
            custo_falsos_positivos = fp * custo_fp
            custo_falsos_negativos = fn * custo_fn
            custo_total = custo_falsos_positivos + custo_falsos_negativos
            
            # Custo médio por erro
            total_erros = fp + fn
            custo_medio = custo_total / total_erros if total_erros > 0 else 0
            
            return {
                'custo_falsos_positivos': custo_falsos_positivos,
                'custo_falsos_negativos': custo_falsos_negativos,
                'custo_total': custo_total,
                'custo_medio_por_erro': custo_medio,
                'total_erros': total_erros
            }
        else:
            # Para problemas multiclasse, simplificamos para um custo médio
            n_erros = np.sum(y_true != y_pred)
            custo_total = n_erros * custo_fp  # Simplificação
            
            return {
                'custo_total': custo_total,
                'custo_medio_por_erro': custo_fp,
                'total_erros': n_erros
            }
    
    def calcular_economia_recursos(self, tempo_manual, tempo_automatizado, 
                                  custo_hora=50, n_operacoes=1000):
        """
        Calcula economia de recursos com o modelo
        
        Args:
            tempo_manual: Tempo médio para operação manual (horas)
            tempo_automatizado: Tempo médio com modelo (horas)
            custo_hora: Custo por hora de trabalho
            n_operacoes: Número de operações no período
            
        Returns:
            dict: Métricas de economia
        """
        # Tempo total
        tempo_total_manual = tempo_manual * n_operacoes
        tempo_total_auto = tempo_automatizado * n_operacoes
        
        # Economia de tempo
        economia_tempo = tempo_total_manual - tempo_total_auto
        
        # Economia financeira
        economia_financeira = economia_tempo * custo_hora
        
        # Percentual de economia
        pct_economia = economia_tempo / tempo_total_manual if tempo_total_manual > 0 else 0
        
        return {
            'economia_tempo_horas': economia_tempo,
            'economia_financeira': economia_financeira,
            'percentual_economia': pct_economia
        }
    
    def calcular_tempo_resposta(self, tempos_execucao):
        """
        Calcula estatísticas de tempo de resposta
        
        Args:
            tempos_execucao: Lista de tempos de execução em segundos
            
        Returns:
            dict: Estatísticas de tempo
        """
        tempos = np.array(tempos_execucao)
        
        return {
            'tempo_medio': np.mean(tempos),
            'tempo_mediano': np.median(tempos),
            'tempo_p95': np.percentile(tempos, 95),
            'tempo_p99': np.percentile(tempos, 99),
            'tempo_minimo': np.min(tempos),
            'tempo_maximo': np.max(tempos)
        }
    
    def calcular_satisfacao_usuario(self, avaliacoes):
        """
        Calcula métricas de satisfação do usuário
        
        Args:
            avaliacoes: Lista de avaliações (1-5)
            
        Returns:
            dict: Métricas de satisfação
        """
        avaliacoes = np.array(avaliacoes)
        
        # Distribuição de avaliações
        distribuicao = {
            '1_estrela': np.sum(avaliacoes == 1) / len(avaliacoes),
            '2_estrelas': np.sum(avaliacoes == 2) / len(avaliacoes),
            '3_estrelas': np.sum(avaliacoes == 3) / len(avaliacoes),
            '4_estrelas': np.sum(avaliacoes == 4) / len(avaliacoes),
            '5_estrelas': np.sum(avaliacoes == 5) / len(avaliacoes)
        }
        
        # Satisfação geral
        media = np.mean(avaliacoes)
        
        # Percentual de avaliações positivas (4-5)
        pct_positivas = np.sum(avaliacoes >= 4) / len(avaliacoes)
        
        return {
            'media_avaliacoes': media,
            'mediana_avaliacoes': np.median(avaliacoes),
            'percentual_positivas': pct_positivas,
            'distribuicao': distribuicao
        }
    
    def registrar_kpis(self, kpis, data=None):
        """
        Registra KPIs no histórico
        
        Args:
            kpis: Dicionário com KPIs calculados
            data: Data do registro (opcional)
        """
        if data is None:
            data = dt.datetime.now()
        
        self.historico.append({
            'data': data,
            'kpis': kpis
        })
    
    def comparar_com_targets(self, kpis):
        """
        Compara KPIs com valores-alvo
        
        Args:
            kpis: Dicionário com KPIs calculados
            
        Returns:
            dict: Comparação com targets
        """
        comparacao = {}
        
        for kpi, valor in kpis.items():
            if kpi in self.targets:
                target = self.targets[kpi]
                diff = valor - target
                pct_diff = diff / target if target != 0 else 0
                
                # Determinar status (maior é melhor para ROI e economia, menor é melhor para custos e tempo)
                if kpi in ['roi', 'economia_recursos', 'satisfacao_usuario']:
                    status = 'Acima do target' if valor >= target else 'Abaixo do target'
                    cor = 'green' if valor >= target else 'red'
                else:
                    status = 'Abaixo do target' if valor <= target else 'Acima do target'
                    cor = 'green' if valor <= target else 'red'
                
                comparacao[kpi] = {
                    'valor': valor,
                    'target': target,
                    'diferenca': diff,
                    'diferenca_percentual': pct_diff,
                    'status': status,
                    'cor': cor
                }
        
        return comparacao
    
    def gerar_dashboard(self, kpis, comparacao=None):
        """
        Gera dashboard visual dos KPIs
        
        Args:
            kpis: Dicionário com KPIs calculados
            comparacao: Comparação com targets (opcional)
            
        Returns:
            matplotlib.figure: Figura com dashboard
        """
        # Criar figura
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Dashboard de KPIs de Negócio', fontsize=16)
        
        # Plotar ROI se disponível
        if 'roi' in kpis:
            ax = axs[0, 0]
            roi = kpis['roi']
            ax.bar(['ROI'], [roi], color='blue')
            
            if comparacao and 'roi' in comparacao:
                ax.axhline(y=comparacao['roi']['target'], color='red', linestyle='--', 
                          label=f"Target: {comparacao['roi']['target']}")
            
            ax.set_title('Retorno sobre Investimento (ROI)')
            ax.set_ylabel('ROI')
            ax.grid(axis='y', alpha=0.3)
        
        # Plotar custos se disponível
        if 'custo_total' in kpis:
            ax = axs[0, 1]
            custos = [kpis.get('custo_falsos_positivos', 0), 
                     kpis.get('custo_falsos_negativos', 0)]
            ax.bar(['Falsos Positivos', 'Falsos Negativos'], custos)
            ax.set_title('Custos por Tipo de Erro')
            ax.set_ylabel('Custo')
            ax.grid(axis='y', alpha=0.3)
        
        # Plotar economia se disponível
        if 'percentual_economia' in kpis:
            ax = axs[1, 0]
            pct = kpis['percentual_economia'] * 100
            ax.pie([pct, 100-pct], labels=['Economia', 'Custo Atual'], 
                  autopct='%1.1f%%', colors=['green', 'gray'])
            ax.set_title('Economia de Recursos')
        
        # Plotar evolução temporal se houver histórico
        if self.historico:
            ax = axs[1, 1]
            
            # Extrair dados do histórico para um KPI específico
            kpi_para_plotar = next(iter(self.targets.keys()))  # Primeiro KPI disponível
            
            datas = [h['data'] for h in self.historico]
            valores = []
            
            for h in self.historico:
                if kpi_para_plotar in h['kpis']:
                    valores.append(h['kpis'][kpi_para_plotar])
                else:
                    valores.append(None)
            
            # Filtrar None values
            datas_filtradas = []
            valores_filtrados = []
            for d, v in zip(datas, valores):
                if v is not None:
                    datas_filtradas.append(d)
                    valores_filtrados.append(v)
            
            if valores_filtrados:
                ax.plot(datas_filtradas, valores_filtrados, marker='o')
                ax.set_title(f'Evolução de {kpi_para_plotar}')
                ax.grid(True, alpha=0.3)
        
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        return fig


# Exemplo de uso
if __name__ == "__main__":
    # Instanciar classe
    kpis_negocio = KPIsNegocio()
    
    # Dados de exemplo
    np.random.seed(42)
    y_true = np.random.randint(0, 2, 1000)
    y_pred = np.random.randint(0, 2, 1000)
    
    # Calcular custo de erros
    custos = kpis_negocio.calcular_custo_erros(y_true, y_pred)
    print("Custos de erros:")
    for k, v in custos.items():
        print(f"  {k}: {v}")
    
    # Calcular ROI
    roi = kpis_negocio.calcular_roi(
        custo_implementacao=50000,
        economia_mensal=10000
    )
    print(f"\nROI: {roi:.2f}")
    
    # Calcular economia de recursos
    economia = kpis_negocio.calcular_economia_recursos(
        tempo_manual=0.5,
        tempo_automatizado=0.1
    )
    print("\nEconomia de recursos:")
    for k, v in economia.items():
        print(f"  {k}: {v}")
    
    # Registrar KPIs
    kpis = {
        'roi': roi,
        'custo_por_erro': custos['custo_medio_por_erro'],
        'economia_recursos': economia['percentual_economia'],
        'tempo_resposta': 0.3,
        'satisfacao_usuario': 4.5
    }
    kpis_negocio.registrar_kpis(kpis)
    
    # Comparar com targets
    comparacao = kpis_negocio.comparar_com_targets(kpis)
    print("\nComparação com targets:")
    for k, v in comparacao.items():
        print(f"  {k}: {v['valor']:.2f} vs target {v['target']:.2f} - {v['status']}")
    
    # Gerar dashboard
    kpis_dashboard = {**custos, **{'roi': roi}, **economia}
    fig = kpis_negocio.gerar_dashboard(kpis_dashboard, comparacao)
    plt.savefig('dashboard_kpis.png')