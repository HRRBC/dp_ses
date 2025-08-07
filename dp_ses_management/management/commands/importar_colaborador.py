import pandas as pd
from django.core.management.base import BaseCommand
from datetime import datetime
from django.db import transaction
from dp_ses_management.models import Colaborador

def formatar_cpf(cpf):
    """Formata e valida o CPF"""
    if pd.isna(cpf) or cpf in ['', 'NaN', 'NaT']:
        return None
    
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    return cpf if len(cpf) == 11 else None

def converter_data_excel(valor):
    """
    Converte valores de data do Excel para objeto date do Python
    Retorna None se não for possível converter
    """
    if pd.isna(valor) or valor in ['', 'NaN', 'NaT', None, 'None']:
        return None

    try:
        # Se já for um objeto datetime (pode ser o caso do pandas)
        if hasattr(valor, 'date'):
            return valor.date()
        
        # Se for string no formato 'YYYY-MM-DD 00:00:00'
        if isinstance(valor, str):
            valor = valor.split()[0]  # Pega apenas a parte da data
            return datetime.strptime(valor, '%Y-%m-%d').date()
        
        # Tentativa genérica como último recurso
        return pd.to_datetime(valor, errors='coerce').date()
    except:
        return None

class Command(BaseCommand):
    help = 'Importa colaboradores a partir de uma planilha Excel'

    def handle(self, *args, **options):
        caminho_arquivo = 'colaboradores.xlsx'
        
        try:
            # Ler arquivo Excel tratando explicitamente a coluna de data
            df = pd.read_excel(
                caminho_arquivo,
                sheet_name='LISTA GERAL',
                parse_dates=['NASCIMENTO'],
                date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S', errors='coerce')
            )
            
            # Verificar colunas existentes
            colunas_planilha = set(col.upper() for col in df.columns)
            self.stdout.write(f"Colunas encontradas na planilha: {colunas_planilha}")
            
            # Verificar colunas mínimas necessárias
            colunas_obrigatorias = {'CPF', 'NOME'}
            if not colunas_obrigatorias.issubset(colunas_planilha):
                raise ValueError(f"Colunas obrigatórias não encontradas. Esperado: {colunas_obrigatorias}")
            
            # Verificar se há dados
            if df.empty:
                raise ValueError("Planilha vazia")

            # Debug: mostrar primeiras linhas para verificação
            self.stdout.write("\nPrimeiras linhas da planilha:")
            self.stdout.write(str(df.head()))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erro ao ler arquivo: {str(e)}"))
            return

        total_criados = 0
        total_atualizados = 0
        total_erros = 0

        with transaction.atomic():
            for index, row in df.iterrows():
                try:
                    # Obter dados da linha
                    nome = row.get('NOME')
                    cpf = row.get('CPF')
                    data_nasc = row.get('NASCIMENTO')
                    
                    # Validações básicas
                    if pd.isna(nome) or not str(nome).strip():
                        raise ValueError("Nome é obrigatório")
                    
                    cpf_formatado = formatar_cpf(cpf)
                    if not cpf_formatado:
                        raise ValueError("CPF inválido")
                    
                    # Converter data
                    data_nascimento = converter_data_excel(data_nasc)
                    
                    # Debug
                    self.stdout.write(f"\nLinha {index+2}:")
                    self.stdout.write(f"CPF: {cpf_formatado}")
                    self.stdout.write(f"Nome: {nome}")
                    self.stdout.write(f"Data original: {data_nasc} (tipo: {type(data_nasc)})")
                    self.stdout.write(f"Data convertida: {data_nascimento} (tipo: {type(data_nascimento) if data_nascimento else 'None'})")
                    
                    # Criar/atualizar colaborador
                    colaborador, created = Colaborador.objects.update_or_create(
                        cpf=cpf_formatado,
                        defaults={
                            'nome_completo': str(nome).strip(),
                            'data_nascimento': data_nascimento,
                            'status': 'ativo'
                        }
                    )

                    if created:
                        total_criados += 1
                        self.stdout.write(self.style.SUCCESS(f"✅ Criado: {colaborador.nome_completo}"))
                    else:
                        total_atualizados += 1
                        self.stdout.write(f"✏️ Atualizado: {colaborador.nome_completo}")

                except Exception as e:
                    total_erros += 1
                    self.stdout.write(self.style.ERROR(
                        f"❌ Linha {index+2} | CPF: {cpf if not pd.isna(cpf) else 'N/D'} | Erro: {str(e)}"
                    ))
                    continue

        # Resumo final
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS("RESUMO DA IMPORTAÇÃO"))
        self.stdout.write(f"Total de linhas processadas: {len(df)}")
        self.stdout.write(f"Novos colaboradores criados: {total_criados}")
        self.stdout.write(f"Colaboradores atualizados: {total_atualizados}")
        self.stdout.write(self.style.ERROR(f"Erros encontrados: {total_erros}"))
        self.stdout.write("="*50)