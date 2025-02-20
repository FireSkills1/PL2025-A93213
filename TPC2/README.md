# TPC1

![foto perfil](/images/A93213.jpg)

## Autor:
Manuel Vasconces Amaral dos Santos Fernandes(A93213)

Este código é um processador de arquivos CSV focado em obras musicais, extraindo informações específicas e gerando relatórios em arquivos de texto. Inicialmente, a função read_file(filename) abre o arquivo CSV (obras.csv), lê todas as linhas do arquivo e lida com linhas quebradas por aspas (") ao concatenar linhas incompletas até fechar as aspas. A primeira linha é tratada como o cabeçalho (nomes das colunas) e, para cada linha de dados, os valores são divididos corretamente, mesmo que contenham ponto e vírgula (;) dentro de aspas. Para cada linha, é criado um dicionário que associa os campos do cabeçalho aos valores respectivos, retornando uma lista de dicionários onde cada dicionário representa um registro do CSV.

O código também possui funções específicas para extrair dados. A função get_composers_list(data) extrai todos os compositores únicos do campo 'compositor' dos registros e retorna uma lista ordenada alfabeticamente. A função get_period_distribution(data) conta a quantidade de obras por período usando o campo 'periodo' e retorna um dicionário onde a chave é o período e o valor é o número de obras. Já a função get_titles_by_period(data) agrupa os títulos das obras ('nome') por período ('periodo') e retorna um dicionário onde cada período possui uma lista de títulos ordenados alfabeticamente.

Para a geração dos relatórios, o código utiliza três funções. A função write_composers_to_file(composers, output_file) escreve a lista de compositores no arquivo compositores.txt, colocando um compositor por linha. A função write_period_distribution(distribution, output_file) grava a distribuição de obras por período no arquivo distribuicao_periodos.txt. Por fim, a função write_titles_by_period(titles_by_period, output_file) salva o dicionário de obras por período no arquivo obras_por_periodo.txt, listando os títulos de cada período.

No fluxo principal do código, os dados são lidos do arquivo obras.csv, e o primeiro registro lido é exibido para uma verificação rápida. Em seguida, o código gera e salva os três relatórios: compositores, distribuição por período e obras por período. Por fim, exibe uma mensagem indicando o sucesso do processamento.
