import os
from PyPDF2 import PdfMerger

Pasta = "certificados_teste"
Saida = "certificados_final.pdf"

def listar_pdfs():
    return sorted([
        f for f in os.listdir(Pasta)
        if f.lower().endswith(".pdf")
    ])

print("\n========= GERADOR DE ARQUIVO FINAL =========\n")

pdfs = listar_pdfs()
total = len(pdfs)

print(f"Foram encontrados {total} PDFs na pasta '{Pasta}'.\n")

print("Escolha uma opção:")
print("1 - Juntar TODOS os PDFs")
print("2 - Juntar SOMENTE uma quantidade específica")
opcao = input("\nDigite 1 ou 2: ")

merger = PdfMerger()

if opcao == "1":
    print("\n➡️  Unindo todos os PDFs...")
    for pdf in pdfs:
        merger.append(os.path.join(Pasta, pdf))

elif opcao == "2":
    qtd = int(input(f"\nQuantos PDFs você deseja juntar? (1 até {total}): "))

    if qtd < 1 or qtd > total:
        print("❌ Quantidade inválida.")
        exit()

    print(f"\n➡️  Unindo os {qtd} primeiros PDFs da lista...")
    for pdf in pdfs[:qtd]:
        merger.append(os.path.join(Pasta, pdf))

else:
    print("❌ Opção inválida.")
    exit()

with open(Saida, "wb") as f:
    merger.write(f)

print(f"\n✔ Arquivo final criado com sucesso: {Saida}")

