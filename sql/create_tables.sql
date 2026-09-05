CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    produto_id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    preco NUMERIC(10,2) DEFAULT 0.00,
    CONSTRAINT chk_preco CHECK (preco >= 0.00) 
);

CREATE TABLE IF NOT EXISTS vendas (
    venda_id INT PRIMARY KEY NOT NULL,
    data DATE NOT NULL,
    cliente_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT DEFAULT 0,

    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    
    CONSTRAINT chk_quantidade CHECK (quantidade >= 0)
);

COMMENT ON TABLE vendas IS 
    'Tabela de vendas. Relaciona produtos e clientes.';
