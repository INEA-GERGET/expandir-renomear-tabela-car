import pandas as pd
import os
import re

# --- 1. Configuração de Caminhos ---
NOME_ARQUIVO_ENTRADA = "Tabela_CAR_limpa.csv" 
NOME_ARQUIVO_SAIDA = "Tabela_CAR_Final.csv" 

def transformar_planilha(arquivo_entrada: str, arquivo_saida: str):
    """
    Transfor ma a planilha usando o método EXPLODE após garantir que as coluna.
    """
    try:
        # --- PASSO 1: Leitura Robusta ---
        print(f"Lendo o arquivo de entrada: {arquivo_entrada}...")
        
        # Leitura com os parâmetros de codificação e separador corretos
        df = pd.read_csv(
            arquivo_entrada, 
            sep=';', 
            encoding='latin-1',
            low_memory=False # Mantido para evitar o DtypeWarning e garantir que o pandas leia os tipos corretamente
        )
        df.columns = df.columns.str.strip()
        
        print("✅ Leitura do arquivo concluída com sucesso.")

        # --- PASSO 2: Transformação de Dados (Explode Otimizado com Alinhamento) ---
        
        colunas_expandir = [
            'cpf', 
            'nome'
        ]
        
        # 2.1. Pré-processamento: Converte as colunas para lista usando '\n' como separador
        for coluna in colunas_expandir:
            # Garante que a coluna é string, remove espaços e faz o split
            # O .fillna('') é importante para garantir que o .str.split funcione
            df[coluna] = df[coluna].astype(str).str.strip().fillna('').str.split('\n')
            
        
        # 2.2. ALINHAMENTO MANUAL: Garante que todas as listas tenham o mesmo comprimento
        
        df_listas = df[colunas_expandir].to_dict('records')
        
        for i, row in enumerate(df_listas):
            # Encontra o tamanho máximo da lista nesta linha
            max_len = max(len(row[col]) for col in colunas_expandir)
            
            # Padroniza todas as listas para o tamanho máximo
            for coluna in colunas_expandir:
                lista = row[coluna]
                if len(lista) < max_len:
                    # Adiciona valores nulos (pd.NA) até atingir o max_len
                    lista.extend([pd.NA] * (max_len - len(lista)))
        
        # 2.3. Cria DataFrames temporários com as listas alinhadas e substitui as colunas
        for coluna in colunas_expandir:
            df[coluna] = [row[coluna] for row in df_listas]


        # 2.4. Aplica o EXPLODE em todas as colunas de proprietário ao mesmo tempo
        # Esta linha agora deve funcionar, pois as listas estão alinhadas
        df_final = df.explode(colunas_expandir)
        
        # 2.5. Limpeza Final dos Dados Explodidos (remove espaços)
        for col in colunas_expandir:
             # O str.strip() deve ser feito APENAS em colunas de string
             df_final[col] = df_final[col].apply(lambda x: str(x).strip() if pd.notna(x) else pd.NA)

        # 2.6. Remove linhas onde o CPF/CNPJ (após o explode) está vazio ou é 'nan'
        df_final = df_final[df_final['cpf'].astype(str).str.lower() != 'nan']
        df_final = df_final.dropna(subset=['cpf'])
        
        # 2.7. Seleciona e define a ordem final das colunas
        colunas_selecionadas = [
            'cpf', 
            'nome',
            'cod_imovel', 
            'nome_imovel',
            'area_imovel',
            'area_liq_imovel',
            'mod_fisc',
            'tipo_imovel',
            'estado',
            'municipio_imovel',
            'sit_imovel',
            'fase_processo',
            'area_consolidada',
            'veg_nativa',
            'area_pousio',
            'area_res_propos',
            'area_res_averb',
            'area_res_apr',
            'area_app_recomp',
            'area_rest_nativa',
            'area_rest_imovel',
            'area_rest_total',
            'exc_pass',
            'sobrep_imvl_rural',
            'sobrep_indigena',
            'sobrep_uc',
            'sobrep_assent',
            'area_antrop',
            'veg_nativa',
            'area_recompor',
            'veg_nativa_app',
            'area_recompor_app',
            'veg_nativa_ur',
            'area_recompor_ur',
            'reserv_app',
            'prog_recup',
            'orgao_prad',
            'data_prad',
            'encer_prad',
            'rppn',
            'area_rppn',
            'data_rppn',
            'num_rppn',
            'crf',
            'alt_tam_imvl',
            'area_imvl_2008'
        ]
        
        # Filtra e reordena as colunas
        df_final = df_final[colunas_selecionadas]

        
        # --- PASSO 4: Salvamento do Resultado ---
        df_final.to_csv(arquivo_saida, index=False)
        
        print(f"\n✅ Sucesso! Os dados transformados e renomeados foram salvos em: {arquivo_saida}")
        tamanho_antes = len(df['cpf'])
        tamanho_depois = len(df_final['cpf'])
        diff = tamanho_depois - tamanho_antes
        print("✨ "*32)
        print(f"✨   Nova planilha {NOME_ARQUIVO_SAIDA} com {diff} linhas a mais do que a planilha original   ✨ ")
        print("✨ "*32)

    except FileNotFoundError:
        print(f"❌ Erro: O arquivo de entrada '{arquivo_entrada}' não foi encontrado. Verifique a ortografia e a localização.")
    except Exception as e:
        print(f"❌ Ocorreu um erro durante o processamento: {e}")

# Executa a função
transformar_planilha(NOME_ARQUIVO_ENTRADA, NOME_ARQUIVO_SAIDA)
