
from unidades.models import UnidadeSaude

def run():
    unidades = [
        {
            'nome': 'UPA Vila Mariana',
            'tipo': 'UPA',
            'endereco': 'Rua Domingos de Morais, 1234',
            'latitude': -23.5928,
            'longitude': -46.6342,
            'medicamentos': 'Dipirona, Amoxicilina, Paracetamol',
            'especialidades': 'Clínico geral, Pediatria',
        },
        {
            'nome': 'UBS Saúde Ipiranga',
            'tipo': 'UBS',
            'endereco': 'Av. Nazaré, 654',
            'latitude': -23.5859,
            'longitude': -46.6101,
            'medicamentos': 'Ibuprofeno, Salbutamol',
            'especialidades': 'Clínico geral, Ginecologia',
        },
        {
            'nome': 'Policlínica Mooca',
            'tipo': 'Policlínica',
            'endereco': 'Rua da Mooca, 2000',
            'latitude': -23.5540,
            'longitude': -46.5965,
            'medicamentos': 'Losartana, Metformina, Omeprazol',
            'especialidades': 'Endocrinologia, Cardiologia',
        },
    ]

    for unidade in unidades:
        UnidadeSaude.objects.create(
            nome=unidade['nome'],
            tipo=unidade['tipo'],
            endereco=unidade['endereco'],
            latitude=unidade['latitude'],
            longitude=unidade['longitude'],
            medicamentos_disponiveis=unidade['medicamentos'],
            especialidades=unidade['especialidades'],
        )

    print("Unidades de teste criadas com sucesso!")
