# 🎓 Certificate Generator

Automação completa para gerar certificados personalizados em PDF e unificá-los em um único arquivo final.  
Este projeto lê uma lista de nomes, posiciona cada nome exatamente nas coordenadas desejadas e cria um PDF individual seguindo o modelo base.

Ideal para eventos, cursos, workshops ou qualquer cenário onde muitos certificados precisam ser produzidos com rapidez e precisão.

---

## Funcionalidades

- 📌 Gera PDFs individuais de certificados a partir de um template vazio (ou base)
- ✍️ Escreve o nome na *mesma posição, fonte, cor e tamanho do modelo original*
- 📄 Suporte a listas com grande volume (100, 200, 500 nomes…)
- 🔗 Junta todos os certificados em um único arquivo final
- 🖨️ Arquivos prontos para impressão ou envio
- 🧩 Compatível com **Python 3.13**

---

## Tecnologias utilizadas

- **Python 3.13**
- **ReportLab** — para gerar o texto sobre o PDF
- **PyPDF2** — para mesclar PDFs
- Arquivos:
  - `nomes.txt`
  - `docBranco.pdf`
  - Scripts Python

-

