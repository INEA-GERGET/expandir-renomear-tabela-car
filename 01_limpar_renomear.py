import pandas as pd
import logging

# Configuração básica de logging para feedback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

caminho_arquivo = 'Tabela_CAR.csv' 

# Parâmetros de leitura ajustados com base na análise do arquivo
csv_params = {
    'filepath_or_buffer': caminho_arquivo,
    'sep': ';',         
    'encoding': 'latin-1' 
}

try:
    logging.info(f"Tentando ler o arquivo: {caminho_arquivo}")
    
    # 1. Leitura do arquivo CSV com os parâmetros ajustados
    df = pd.read_csv(**csv_params, low_memory=False) 
    logging.info("✅ Arquivo lido com sucesso.")

    # Garante que os nomes das colunas estejam sem espaços extras no início/fim
    df.columns = df.columns.str.strip()
    
    tam_antes = len(df['Número do Recibo'])
    
    # Remove colunas não necessárias para nossa análise
    lista_remover = ['Data de nascimento dos Proprietários',
    'CPF do Cadastrante',
    'Nome do Cadastrante',
    'Área de Preservação Permanente de Banhado',
    'Área de Preservação Permanente de Lagos e Lagoas Naturais',
    "Área de Preservação Permanente de Nascentes ou Olhos D'água Perenes",
    "Área de Preservação Permanente de Reservatório artificial decorrente de barramento de cursos d'água",
    'Área de Preservação Permanente de Rios até 10 metros',
    'Área de Preservação Permanente de Rios de 10 até 50 metros',
    'Área de Preservação Permanente de Rios de 50 até 200 metros',
    'Área de Preservação Permanente de Rios de 200 até 600 metros',
    'Área de Preservação Permanente de Rios com mais de 600 metros',
    'Área de Preservação Permanente de Veredas',
    'Área de Preservação Permanente de Áreas com Altitude Superior a 1800 metros',
    'Área de Preservação Permanente de Áreas com Declividades Superiores a 45 graus',
    'Área de Preservação Permanente de Bordas de Chapada',
    'Área de Preservação Permanente de Topos de Morro',
    'Área de Preservação Permanente a Recompor de Lagos e Lagoas Naturais',
    "Área de Preservação Permanente a Recompor de Nascentes ou Olhos D'água Perenes",
    'Área de Preservação Permanente a Recompor de Rios até 10 metros',
    'Área de Preservação Permanente a Recompor de Rios de 10 até 50 metros',
    'Área de Preservação Permanente a Recompor de Rios de 50 até 200 metros',
    'Área de Preservação Permanente a Recompor de Rios de 200 até 600 metros',
    'Área de Preservação Permanente a Recompor de Rios com mais de 600 metros',
    'Área de Preservação Permanente a Recompor de Veredas',
    'Área de Preservação Permanente de Manguezais',
    'Área de Preservação Permanente de Restingas',
    'Area de uso restrito em área consolidada',
    'Area de uso restrito em área antropizada',
    'Total de Área de Uso Restrito para declividade de 25 a 45 graus',
    'Total de Área de Uso Restrito para regiões pantaneiras',
    'Total de Área de Servidão Administrativa de Entorno de Reservatório para Abastecimento ou Geração de Energia',
    'Total de Área de UServidão Administrativa de Reservatório para Abastecimento ou Geração de Energia',
    'Total de Área de Servidão Administrativa de Infraestrutura Pública',
    'Total de Área de Servidão Administrativa Utilidade Pública',
    'Reserva Legal Mínima exigida por Lei (ha)',
    'Deseja aderir ao Programa de Regularização Ambiental - PRA, caso o imóvel rural possua (uma das situações a seguir, ocorrida até 22 de julho de 2008): necessidade de recomposição de áreas de APP e de uso restrito; déficit referente a Reserva Legal; autuação?',
    'O imóvel rural possui área com déficit de vegetação nativa para fins de cumprimento da Reserva Legal?',
    'Qual alternativa você pretende adotar, isolada ou conjuntamente, para regularizar o déficit?',
    'Caso realize compensação, como deseja compensar a área com déficit?',
    'Existe Termo de Ajuste de Conduta (TAC) aprovado referente à regularização de APP, Reserva Legal ou área de uso restrito?',
    'Qual é o órgão emitente do TAC?',
    'Qual é a data de assinatura do TAC?',
    'Qual é a data de encerramento do TAC?',
    'Existem infrações cometidas até 22 julho de 2008, relativas à supressão irregular de vegetação em APP, Reserva Legal ou área de uso restrito do imóvel, objeto de autuação?',
    'O imóvel rural possui área remanescente de vegetação nativa excedente ao mínimo exigido para Reserva Legal?',
    'O que você deseja fazer com a área excedente?',
    'A Reserva Legal do imóvel rural está submetida à legislação de que período?',
    'Unnamed: 94']
    
    # É uma boa prática filtrar as colunas que realmente existem antes de tentar remover
    colunas_existentes = [col for col in lista_remover if col in df.columns]
    df = df.drop(colunas_existentes, axis=1)
    
    # Renomeia as colunas para trabalhar com elas no formulário 	
    dicionario = {
    'Número do Recibo': 'cod_imovel', 
    'Nome do Imóvel': 'nome_imovel',
    'CPF ou CNPJ dos Proprietários': 'cpf',
    'Nome dos Proprietários': 'nome',
    'Área do Imóvel (ha)': 'area_imovel',
    'Área Líquida do Imóvel (ha)': 'area_liq_imovel',
    'Módulos Fiscais': 'mod_fisc',
    'Tipo do Imóvel': 'tipo_imovel',
    'Estado': 'estado',
    'Município': 'municipio_imovel',
    'Situação do Imóvel': 'sit_imovel',
    'Fase do Processo': 'fase_processo',
    'Área Consolidada (ha)': 'area_consolidada',
    'Remanescente de Vegetação Nativa (ha)': 'veg_nativa',
    'Área de Pousio (ha)': 'area_pousio',
    'Área de Reserva Legal Proposta': 'area_res_propos',
    'Área de Reserva Legal Averbada': 'area_res_averb',
    'Área de Reserva Legal Aprovada e não Averbada': 'area_res_apr',
    'Área da APP à recompor (ha)': 'area_app_recomp',
    'Area de uso restrito em vegetação nativa': 'area_rest_nativa',
    'Área de uso restrito a recompor no imóvel': 'area_rest_imovel',
    'Área de uso restrito total': 'area_rest_total',
    'Excedente ou Passivo de RL (ha)': 'exc_pass',
    'Sobreposição com Outros Imoveis Rurais (ha)': 'sobrep_imvl_rural',
    'Sobreposição com Terra Indigena (ha)': 'sobrep_indigena',
    'Sobreposição com Unidade de Conservação (ha)': 'sobrep_uc',
    'Sobreposição com Assentamento (ha)': 'sobrep_assent',
    'Área Antropizada (ha)': 'area_antrop',
    'Vegetação Nativa em Reserva Legal (ha)': 'veg_nativa',
    'Área a Recompor em Reserva Legal (ha)': 'area_recompor',
    'Vegetação Nativa em APP (ha)': 'veg_nativa_app',
    'Área a recompor em APP (ha)': 'area_recompor_app',
    'Vegetação Nativa em area de Uso Restrito (ha)': 'veg_nativa_ur',
    'Área a recompor de Uso Restrito (ha)': 'area_recompor_ur',
    'Área de Reserva Legal dentro de APP (ha)': 'reserv_app',
    'Existe Programa de Recuperação de Áreas Degradadas (PRAD) ou outro documento aprovado referente à regularização de APP, Reserva Legal ou área de uso restrito?': 'prog_recup',
    'Qual é o órgão emitente do PRAD?': 'orgao_prad',
    'Qual é a data de assinatura do PRAD?': 'data_prad',
    'Qual é a data de encerramento do PRAD?': 'encer_prad',
    'Existe Reserva Particular do Patrimônio Natural - RPPN - no interior do imóvel rural?': 'rppn',
    'Qual a área (ha) da RPPN?': 'area_rppn',
    'Qual é data de publicação de reconhecimento da RPPN?': 'data_rppn',
    'Qual é o número de decreto/portaria de reconhecimento da RPPN?': 'num_rppn',
    'Possui cota de reserva florestal - CRF?': 'crf',
    'Ocorreu alteração no tamanho da área do imóvel após 22/07/2008?': 'alt_tam_imvl',
    'Qual era a área (ha) do imóvel em 22/07/2008?': 'area_imvl_2008'}

    df = df.rename(dicionario,  axis='columns')

    # Remove os dados de CARs que foram cancelados
    cars_nao_cancelados = df['sit_imovel'] != 'Cancelado'
    df = df[cars_nao_cancelados].copy()
    
    tam_antes = len(df['cod_imovel'])
    
    tam_depois = len(df['cod_imovel'])
    dif = tam_antes - tam_depois
    
    print(f'\n Tamanho do dataframe original: {tam_antes}')
    print(f'\n Foram removidos {dif} CARs CANCELADOS')
    print(f'\n Tamanho do dataframe atual: {tam_depois}')
    
    # 3. Mostrar as primeiras 5 linhas para inspeção
    print("\n" + "="*50)
    print("PRIMEIRAS 5 LINHAS DO DATAFRAME:")
    print("="*50)
    print(df.head())
    print("="*50)
    
    # CORREÇÃO: Adicionado index=False para não salvar o índice do pandas no CSV
    df.to_csv('Planilha.csv', index=False, sep=';') 
    logging.info("✅ Arquivo 'Tabela_CAR_limpa.csv' salvo com sucesso, sem o índice.")
