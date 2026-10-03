USE Taskmaster;
GO

CREATE TABLE Clientes (
    ClienteID INT IDENTITY(1,1) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100),
    Estado CHAR(2)
);
GO

CREATE TABLE Produtos (
    ProdutoID INT IDENTITY(1,1) PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Categoria VARCHAR(50),
    Preco DECIMAL(10,2) NOT NULL
);
GO

CREATE TABLE Vendas (
    VendaID INT IDENTITY(1,1) PRIMARY KEY,
    ClienteID INT NOT NULL,
    DataVenda DATE NOT NULL,
    ValorTotal DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_Vendas_Clientes
        FOREIGN KEY (ClienteID)
        REFERENCES Clientes(ClienteID)
);
GO

CREATE TABLE ItensVenda (
    ItemVendaID INT IDENTITY(1,1) PRIMARY KEY,
    VendaID INT NOT NULL,
    ProdutoID INT NOT NULL,
    Quantidade INT NOT NULL,
    PrecoUnitario DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_ItensVenda_Vendas
        FOREIGN KEY (VendaID)
        REFERENCES Vendas(VendaID),

    CONSTRAINT FK_ItensVenda_Produtos
        FOREIGN KEY (ProdutoID)
        REFERENCES Produtos(ProdutoID)
);
GO