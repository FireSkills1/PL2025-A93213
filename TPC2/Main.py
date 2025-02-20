def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    header = None
    data = []
    current_line = ""
    inside_quotes = False

    for line in lines:
        line = line.strip()

        # Verifica se a linha abre ou fecha aspas
        num_quotes = line.count('"')
        if num_quotes % 2 == 1:
            inside_quotes = not inside_quotes

        # Se estamos dentro de aspas, continuamos acumulando até fechar
        current_line += " " + line if current_line else line
        if inside_quotes:
            continue  # Continua até fechar as aspas

        # Agora temos uma linha completa e podemos processá-la
        if header is None:
            header = current_line.split(';')  # Primeira linha é o cabeçalho
        else:
            values = []
            temp_value = ""
            in_quotes = False

            # Percorre caractere por caractere para dividir corretamente
            for char in current_line:
                if char == '"':
                    in_quotes = not in_quotes  # Alterna entre dentro/fora das aspas
                elif char == ';' and not in_quotes:
                    values.append(temp_value.strip())
                    temp_value = ""
                else:
                    temp_value += char

            values.append(temp_value.strip())  # Adiciona o último campo

            # Remove aspas extras dos valores
            values = [v[1:-1] if v.startswith('"') and v.endswith('"') else v for v in values]

            if len(values) == len(header):  # Garante que a linha é válida
                record = {header[i]: values[i] for i in range(len(header))}
                data.append(record)

        current_line = ""  # Reseta a linha acumulada

    return data


def get_composers_list(data):
    composers = set()
    for record in data:
        if 'compositor' in record:
            composers.add(record['compositor'])
    return sorted(composers)


def get_period_distribution(data):
    periods = {}
    for record in data:
        if 'periodo' in record:
            period = record['periodo']
            periods[period] = periods.get(period, 0) + 1
    return periods


def get_titles_by_period(data):
    result = {}
    for record in data:
        if 'periodo' in record and 'nome' in record:
            period = record['periodo']
            title = record['nome']
            result.setdefault(period, []).append(title)

    for period in result:
        result[period].sort()

    return result


def write_composers_to_file(composers, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Lista ordenada alfabeticamente dos compositores musicais:\n")
        for composer in composers:
            file.write(f"{composer}\n")


def write_period_distribution(distribution, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Distribuição das obras por período:\n")
        for period, count in distribution.items():
            file.write(f"{period}: {count} obra(s)\n")


def write_titles_by_period(titles_by_period, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Dicionário de obras por período:\n")
        for period, titles in titles_by_period.items():
            file.write(f"\n{period}:\n")
            for title in titles:
                file.write(f"  - {title}\n")


# Executando o código
data = read_file('obras.csv')

if data:
    print(f"Primeiro registro: {data[0]}")

composers = get_composers_list(data)
write_composers_to_file(composers, 'compositores.txt')

period_distribution = get_period_distribution(data)
write_period_distribution(period_distribution, 'distribuicao_periodos.txt')

titles_by_period = get_titles_by_period(data)
write_titles_by_period(titles_by_period, 'obras_por_periodo.txt')

print("Processamento concluído. Arquivos gerados com sucesso!")
