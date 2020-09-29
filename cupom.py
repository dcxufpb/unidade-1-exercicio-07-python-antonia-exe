# coding: utf-8

def isEmpty(value: str) -> bool:
    return (value == None) or (len(value) == value.count(" "))

def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):

    if (isEmpty(nome_loja)):
        raise Exception("O campo nome da loja é obrigatório")

    if (isEmpty(logradouro)):
        raise Exception("O campo logradouro do endereço é obrigatório")

    if numero == 0:
        numero = "s/n"

    if (isEmpty(municipio)):
        raise Exception("O campo município do endereço é obrigatório")

    if (isEmpty(estado)):
        raise Exception("O campo estado do endereço é obrigatório")

    if (isEmpty(cnpj)):
        raise Exception("O campo CNPJ da loja é obrigatório")
  
    if (isEmpty(inscricao_estadual)):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    linha2 = f"{logradouro}, {numero}"
    if not isEmpty(complemento):
        linha2 += f" {complemento}"

    linha3 = str()
    if not isEmpty(bairro):
        linha3 += f"{bairro} - "
    linha3 += f"{municipio} - {estado}"

    linha4 = str()
    if not isEmpty(cep):
        linha4 = f"CEP:{cep}"
    if not isEmpty(telefone):
        if not isEmpty(linha4):
            linha4 += " "
        linha4 += f"Tel {telefone}"
    if not isEmpty(linha4):
        linha4 += "\n"

    linha5 = str()
    if not isEmpty(observacao):
        linha5 += f"{observacao}"

    output = f"{nome_loja}\n"
    output += f"{linha2}\n"
    output += f"{linha3}\n"
    output += f"{linha4}"
    output += f"{linha5}\n"
    output += f"CNPJ: {cnpj}\n"
    output += f"IE: {inscricao_estadual}"

    return output
