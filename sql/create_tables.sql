CREATE TABLE clientes(
    cliente_id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL
)


CREATE TABLE produtos(
    produto_id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    preco NUMERIC(10,2)
)

CREATE TABLE vendas(
    venda_id INT PRIMARY KEY NOT NULL,
    data DATE NOT NULL,
    cliente_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
)

ALTER TABLE vendas ADD CONSTRAINT pk_cliente FOREIGN KEY
(cliente_id) REFERENCES clientes (cliente_id)

ALTER TABLE vendas ADD CONSTRAINT pk_produto FOREIGN KEY
(produto_id) REFERENCES produtos (produto_id)
