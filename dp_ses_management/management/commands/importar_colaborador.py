import pandas as pd
from django.core.management.base import BaseCommand
from django.core.validators import validate_integer
from django.core.exceptions import ValidationError
from dp_ses_management.models import Colaborador

def formatar_cpf(cpf):
    """Formata e valida o CPF, removendo caracteres não numéricos e verificando tamanho"""
    if pd.isna(cpf) or cpf in ['', 'NaN', 'NaT']:
        return None
    
    # Remove qualquer caractere não numérico
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    
    if not cpf:  # Se ficou vazio após a filtragem
        return None
        
    # Valida se tem 11 dígitos
    if len(cpf) != 11:
        raise ValueError(f"CPF deve ter 11 dígitos (recebido: {cpf})")
    return cpf

def converter_data(valor):
    """Converte valores de data da planilha para formato adequado"""
    try:
        if pd.isna(valor) or valor in ['', 'NaN', 'NaT']:
            return None
        return pd.to_datetime(valor).date()
    except Exception as e:
        raise ValueError(f"Data inválida: {valor} | Erro: {str(e)}")

class Command(BaseCommand):
    help = 'Importa colaboradores a partir de uma planilha Excel'

    def handle(self, *args, **kwargs):
        caminho_arquivo = 'colaboradores.xlsx'
        
        try:
            # Ler arquivo verificando os cabeçalhos
            df = pd.read_excel(caminho_arquivo)
            
            # Verificar colunas esperadas (com tratamento para diferenças de case e acentos)
            colunas_planilha = [col.upper() for col in df.columns]
            colunas_necessarias = {'CPF', 'NOME', 'MATRÍCULA', 'MATRICULA', 'DATA DE NASCIMENTO', 'DATA_NASCIMENTO'}
            
            if not colunas_necessarias.intersection(colunas_planilha):
                raise ValueError(f"Colunas não encontradas. Esperado: {colunas_necessarias} | Encontrado: {df.columns.tolist()}")
                
            # Padroniza nomes das colunas
            df.columns = df.columns.str.upper()
            
            # Verifica se há dados
            if df.empty:
                raise ValueError("A planilha está vazia")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erro ao ler arquivo: {str(e)}"))
            return

        total_criados = 0
        total_atualizados = 0
        total_erros = 0

        for index, row in df.iterrows():
            try:
                # Obtém valores com tratamento de casos alternativos
                nome = row.get('NOME') or row.get('NOME COMPLETO')
                cpf = row.get('CPF')
                matricula = row.get('MATRÍCULA') or row.get('MATRICULA')
                data_nasc = row.get('DATA DE NASCIMENTO') or row.get('DATA_NASCIMENTO')

                # Validações básicas
                if pd.isna(nome) or str(nome).strip() == '':
                    raise ValueError("Nome do colaborador não pode ser vazio")
                
                cpf_formatado = formatar_cpf(cpf)
                if not cpf_formatado:
                    raise ValueError("CPF inválido ou vazio")
                
                # Processamento dos dados
                colaborador, created = Colaborador.objects.update_or_create(
                    cpf=cpf_formatado,
                    defaults={
                        'nome_completo': str(nome).strip(),
                        'matricula': str(matricula).strip() if not pd.isna(matricula) else '',
                        'data_nascimento': converter_data(data_nasc),
                        'status': 'ativo'
                    }
                )

                if created:
                    total_criados += 1
                    msg = f"✅ Criado: {colaborador.nome_completo} (CPF: {cpf_formatado})"
                    self.stdout.write(self.style.SUCCESS(msg))
                else:
                    total_atualizados += 1
                    self.stdout.write(f"✏️ Atualizado: {colaborador.nome_completo}")

            except Exception as e:
                total_erros += 1
                cpf_erro = str(cpf) if not pd.isna(cpf) else 'N/D'
                msg_erro = f"❌ Erro na linha {index + 2} | CPF: {cpf_erro} | Erro: {str(e)}"
                self.stdout.write(self.style.ERROR(msg_erro))
                continue

        # Resumo final
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS(f"Importação concluída!"))
        self.stdout.write(f"Total de registros processados: {len(df)}")
        self.stdout.write(f"Novos colaboradores criados: {total_criados}")
        self.stdout.write(f"Colaboradores atualizados: {total_atualizados}")
        self.stdout.write(self.style.ERROR(f"Registros com erro: {total_erros}"))
        self.stdout.write("="*50)