import csv

def ler_csv(arquivo):
    produtos = []
    try:
        with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Nome'] = row['Nome'].strip()
                produtos.append(row)
    except FileNotFoundError:
        produtos = []
    return produtos

def listar_categorias(produtos):
    return list(set(produto['Categoria'] for produto in produtos))

def listar_produtos_por_categoria(produtos, categoria):
    print(f"\n📦 Produtos na categoria '{categoria}':")
    for produto in produtos:
        if produto['Categoria'] == categoria:
            print(f"{produto['Nome']} - R${produto['Preço']} ({produto['Quantidade']} disponíveis)")

def adicionar_ao_carrinho(produtos, carrinho, nome, quantidade):
    try:
        quantidade = int(quantidade)
    except ValueError:
        print("⚠️ Quantidade inválida! Insira um número válido.")
        return False
    
    nome = nome.strip().lower()
    
    for produto in produtos:
        if produto['Nome'].strip().lower() == nome:
            estoque_disponivel = int(produto['Quantidade'])
            
            if estoque_disponivel >= quantidade:
                for item in carrinho:
                    if item['Nome'].strip().lower() == nome:
                        item['Quantidade'] = str(int(item['Quantidade']) + quantidade)
                        return True
                carrinho.append({'Nome': produto['Nome'].strip(), 'Preço': produto['Preço'], 'Quantidade': str(quantidade)})
                return True
            else:
                print(f"⚠️ Estoque insuficiente! Apenas {estoque_disponivel} disponíveis.")
                return False
    
    print("⚠️ Produto não encontrado! Verifique o nome digitado.")
    return False

def remover_do_carrinho(carrinho, nome):
    nome = nome.strip().lower()
    for item in carrinho:
        if item['Nome'].strip().lower() == nome:
            carrinho.remove(item)
            return True
    return False

def finalizar_compra(produtos, carrinho, arquivo):
    for item in carrinho:
        for produto in produtos:
            if produto['Nome'] == item['Nome']:
                produto['Quantidade'] = str(int(produto['Quantidade']) - int(item['Quantidade']))
    
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Nome', 'Preço', 'Quantidade', 'Categoria']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)