import lib

def main():
    arquivo_csv = 'estoque.csv'
    produtos = lib.ler_csv(arquivo_csv)
    carrinho = []

    while True:
        print("\n🛒 Sistema de Compras - Mercatto 🛒")
        print("1. Listar Produtos")
        print("2. Adicionar Produto ao Carrinho")
        print("3. Remover Produto do Carrinho")
        print("4. Visualizar Carrinho")
        print("5. Finalizar Compra")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n📦 Categorias Disponíveis:")
            categorias = lib.listar_categorias(produtos)
            for i, categoria in enumerate(categorias, start=1):
                print(f"{i}. {categoria}")
            escolha_categoria = input("Digite o número da categoria desejada: ")
            if escolha_categoria.isdigit() and 1 <= int(escolha_categoria) <= len(categorias):
                categoria_escolhida = categorias[int(escolha_categoria) - 1]
                lib.listar_produtos_por_categoria(produtos, categoria_escolhida)
            else:
                print("⚠️ Opção inválida!")

        elif escolha == '2':
            nome = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
            quantidade = input("Quantidade: ")
            if lib.adicionar_ao_carrinho(produtos, carrinho, nome, quantidade):
                print(f"✅ {quantidade}x '{nome}' adicionado ao carrinho!")
            else:
                print("⚠️ Produto não encontrado ou estoque insuficiente.")

        elif escolha == '3':
            nome = input("Digite o nome do produto que deseja remover do carrinho: ")
            if lib.remover_do_carrinho(carrinho, nome):
                print(f"✅ Produto '{nome}' removido do carrinho!")
            else:
                print("⚠️ Produto não encontrado no carrinho.")

        elif escolha == '4':
            print("\n🛍️ Seu Carrinho:")
            if not carrinho:
                print("⚠️ Carrinho vazio.")
            else:
                total = sum(float(item['Preço']) * int(item['Quantidade']) for item in carrinho)
                for i, item in enumerate(carrinho, start=1):
                    print(f"{i}. {item['Nome']} - R${item['Preço']} ({item['Quantidade']} unidades)")
                print(f"💰 Total da compra: R${total:.2f}")

        elif escolha == '5':
            if not carrinho:
                print("⚠️ Carrinho vazio. Adicione produtos antes de finalizar a compra.")
            else:
                metodo = input("Escolha o método de entrega (1- Retirada, 2- Entrega): ")
                metodo_entrega = "Retirada" if metodo == '1' else "Entrega"
                pagamento = input("Escolha o método de pagamento (1- Cartão, 2- Dinheiro, 3- Pix): ")
                pagamento_metodo = {"1": "Cartão", "2": "Dinheiro", "3": "Pix"}.get(pagamento, "Desconhecido")
                if metodo == '2':
                    endereco = input("Digite o endereço de entrega: ")
                    print(f"🛍️ Compra finalizada! Método: {metodo_entrega}, Pagamento: {pagamento_metodo}, Endereço: {endereco}")
                else:
                    print(f"🛍️ Compra finalizada! Método: {metodo_entrega}, Pagamento: {pagamento_metodo}")
                lib.finalizar_compra(produtos, carrinho, arquivo_csv)
                carrinho.clear()

        elif escolha == '6':
            print("🛒 Saindo do sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Escolha novamente.")

if __name__ == '__main__':
    main()