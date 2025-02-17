import psycopg2, openpyxl

class Update_Dados:
    def __init__(self, nomes, imoveis, caminho):
        super().__init__()
        self.servidor = psycopg2.connect(
            dbname="houseup",  
            user="postgres",      
            password="houseuptec",    
            host="fdfd::1acd:4580",  
            port="5432"              
        )
        self.nomes = nomes
        self.caminho = caminho
        self.imoveis = imoveis
        self.carregar_dados()

    def carregar_dados(self):
        planilha = openpyxl.load_workbook(self.caminho)
        aba = planilha['Clientes']
        for nome in self.nomes:
            for linha in aba.iter_rows(min_row=2, max_row=aba.max_row):
                for celula in linha:
                    if celula.value == nome:
                        linha = [celula.value for celula in linha]
                        self.update_dados(linha)
                        break

        aba_2 = planilha['Imóveis']
        for imovel in self.imoveis:
            for linha_imovel in aba_2.iter_rows(min_row=2, max_row=aba_2.max_row):
                for celula_imovel in linha_imovel:
                    if celula_imovel.value == imovel:
                        linha_imovel = [celula_imovel.value for celula_imovel in linha_imovel]
                        self.update_imoveis(linha_imovel)
                        break

    def update_dados(self, linha):
        cursor = self.servidor.cursor()
        linha_str = list(map(str, linha))
        del linha_str[20]
        del linha_str[17]

        nome = linha_str[3]
        cursor.execute("SELECT nome FROM clientes WHERE nome = %s", (nome,))
        result_nome = cursor.fetchall()

        telefone = linha_str[5]
        cursor.execute("SELECT telefone FROM clientes WHERE telefone = %s", (telefone,))
        result_telefone = cursor.fetchall()

        cpf_cnpj = linha_str[7]
        cursor.execute("SELECT cpf_cnpj FROM clientes WHERE cpf_cnpj = %s", (cpf_cnpj,))
        result_cpf_cnpj = cursor.fetchall()

        data_cadastro = linha_str[11]
        cursor.execute("SELECT data_de_cadastro FROM clientes WHERE data_de_cadastro = %s", (data_cadastro,))
        result_data_cadastro = cursor.fetchall()

        if result_nome and result_telefone and result_cpf_cnpj and result_data_cadastro:
            print(f"Cliente {nome} já cadastrado")
            return
        
        cursor.execute('''
        INSERT INTO clientes (corretor, tipo, categoria, nome, email, telefone, profissao, cpf_cnpj, rg, data_de_nascimento, origem, data_de_cadastro, data_de_atualizacao, cep, logradouro, numero, complemento, cidade, bairro, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', linha_str)
        self.servidor.commit()
        cursor.close()

    def update_imoveis(self, linha):
        try:
            cursor = self.servidor.cursor()
            linha_str = list(map(str, linha))

            referencia = linha_str[1]
            cursor.execute("SELECT referencia FROM imoveis WHERE referencia = %s", (referencia,))
            result = cursor.fetchall()
            if result:
                print(f"Imóvel {referencia} já cadastrado")
                return

            cursor.execute('''
                INSERT INTO imoveis (corretor, referencia, transacao, status, rascunho, 
                tipo, subtipo, perfil, situacao, nome_condominio, 
                n_apartamento, valor, dormitorios, suites, garagens, 
                banheiros, estado, cidade, bairro, data_de_cadastro, 
                data_de_atualizacao, cep, logradouro, numero, complemento, 
                medidas, titulo, descricao_geral, descricao_condominio, 
                proprietarios, celular_do_proprietario, averbado, escritura, 
                esquina, ano_de_construcao, incorporacao, posicao_solar, 
                terreno, proximidades_do_mar, cep_condominio, rua_condominio, 
                numero_condominio, unidades_condominio, unidades_por_andar_condominio, 
                andares_condominio, torres_condominio, mostra_valor, mostrar_no_lugar_do_preco, preco_anterior, valor_iptu, 
                periodo_iptu, valor_condominio, tem_financiamento, aceita_financimaneto, 
                valor_das_taxas, descricao_das_taxas, aceita_permuta, descricao_permuta, mcmv, 
                video, tour3, comissao_combinada, observacao_da_negociacao, matricula, ocupacao, observacao_privada,
                mobilia, autorizacao_formalizada, com_placa, exclusividade, proxima_revisao, chaves_disponivel, 
                onde_pegar_chave, tarja, descricao_lote, mostrar_logradouro, mostrar_bairro, 
                mostrar_complemento, mostrar_n_da_rua, mostrar_condominio, 
                mostrar_andar, mostrar_n_apartamento, mostrar_mapa, mostrar_mapa_exato, 
                mostrar_street_view, previsao_entrega, monstra_site, paginal_inicial, anotacoes,
                negocios_abertos, negocios_ganhos, negocios_perdidos, garantias_de_locacao
                ) VALUES (
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s)''', linha_str)
            self.servidor.commit()
        except Exception as e:
            print(e)
        cursor.close()