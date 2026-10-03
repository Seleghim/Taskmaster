use Taskmaster;
go

-- Clientes
INSERT INTO Clientes (Nome, Cidade, Estado)
VALUES
('João Silva', 'São Paulo', 'SP'),
('Maria Oliveira', 'Bauru', 'SP'),
('Carlos Santos', 'Rio de Janeiro', 'RJ'),
('Ana Costa', 'Curitiba', 'PR'),
('Lucas Almeida', 'Belo Horizonte', 'MG'),
('Juliana Souza', 'Campinas', 'SP'),
('Rafael Lima', 'Salvador', 'BA'),
('Beatriz Rocha', 'Brasília', 'DF');
GO

select * from clientes;

-- Produtos

INSERT INTO Produtos (NomeProduto, Categoria, Preco)
VALUES
('Notebook Pro', 'Eletronicos', 3500.00),
('Mouse sem Fio', 'Eletronicos',  120.00),
('Teclado Mecanico', 'Eletronicos', 280.00),
('Monitor 24"', 'Eletronicos', 950.00),
('Cadeira Escritório', 'Móveis', 850.00),
('Mesa Escritório', 'Móveis', 1200.00),
('Headset Gamer', 'Acessorios', 250.00),
('Webcam HD', 'Acessorios', 180.00);
GO

select * from Produtos;

--Vendas

INSERT INTO Vendas (ClienteID, DataVenda, ValorTotal)
VALUES
(17, '2026-01-15', 3620.00),
(18, '2026-01-18', 1200.00),
(19, '2026-02-03', 1130.00),
(20, '2026-02-10', 3500.00),
(21, '2026-02-22', 1100.00),
(22, '2026-03-05', 1480.00),
(23, '2026-03-14', 850.00),
(24, '2026-03-25', 2780.00);
GO

select * from vendas;

SELECT * FROM Clientes;
SELECT * FROM Vendas;
SELECT * FROM Produtos;

-- Itens das Vendas

INSERT INTO ItensVenda (VendaID, ProdutoID, Quantidade, PrecoUnitario)
VALUES
(2, 1, 1, 3500.00),
(2, 2, 1, 120.00),

(3, 6, 1, 1200.00),

(4, 4, 1, 950.00),
(4, 2, 1, 120.00),
(4, 8, 1, 60.00),

(5, 1, 1, 3500.00),

(6, 5, 1, 850.00),
(6, 7, 1, 250.00),

(7, 4, 1, 950.00),
(7, 7, 1, 250.00),
(7, 2, 1, 120.00),
(7, 8, 1, 160.00),

(8, 5, 1, 850.00),

(9, 6, 1, 1200.00),
(9, 1, 1, 1580.00);
GO

SELECT * FROM ItensVenda;

SELECT * FROM Produtos;

SELECT * FROM Vendas Order By DataVenda;

SELECT SUM (ValorTotal) AS FaturamentoTotal FROM Vendas;

SELECT AVG (ValorTotal) AS TicketMedio FROM Vendas;

SELECT C.Nome AS Cliente,
	V.VendaID,
	V.DataVenda,
	V.ValorTotal
FROM Vendas V
INNER JOIN Clientes C
	ON V.ClienteId = C.ClienteId
ORDER BY V.DataVenda;

SELECT 
	P.NomeProduto,
	SUM(I.Quantidade) AS QuantidadeVendida
FROM ItensVenda I
INNER JOIN Produtos P
	ON I.ProdutoID = P.ProdutoID
GROUP BY P.NomeProduto
ORDER BY QuantidadeVendida DESC;


