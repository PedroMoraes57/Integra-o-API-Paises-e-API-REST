from django.core.management.base import BaseCommand
from django.test.utils import get_runner
from django.conf import settings
from django.test.runner import DiscoverRunner
import io


class Command(BaseCommand):
    help = "Roda todos os testes da aplicação usuarios"

    def add_arguments(self, parser):
        parser.add_argument(
            "--app",
            type=str,
            default="usuarios",
            help="Nome do app Django para rodar os testes",
        )

    def handle(self, *args, **options):
        app_name = options["app"]
        self.stdout = io.TextIOWrapper(self.stdout.buffer, encoding='utf-8', errors='replace')
        self.stderr = io.TextIOWrapper(self.stderr.buffer, encoding='utf-8', errors='replace')
        
        self.print_header()

        runner = DiscoverRunner(verbosity=2)
        failures = runner.run_tests([app_name])

        self.print_summary(failures)

    def print_header(self):
        """Exibe o cabeçalho formatado"""
        header = """
========================================================
[ RELATÓRIO DE TESTES DA APLICAÇÃO USUÁRIOS ]
========================================================
Cada teste representa uma validação do sistema.
--------------------------------------------------------
Legenda:
✅ OK     -> Teste passou
❌ FAIL   -> Teste falhou
⚠️ ERROR -> Erro inesperado
--------------------------------------------------------
"""
        self.stdout.write(header)

    def print_summary(self, failures):
        """Exibe o resumo dos testes"""
        self.stdout.write("\n" + "-" * 30)
        self.stdout.write("RESUMO FINAL DOS TESTES:")
        self.stdout.write("-" * 30)

        if failures:
            self.stdout.write("❌ Alguns testes falharam!")
            self.stdout.write("Verifique os detalhes acima e corrija os problemas.")
        else:
            self.stdout.write("\n✅ Todos os testes passaram com sucesso!")
            self.stdout.write(" O sistema está consistente.")

        self.stdout.write("=" * 20)
