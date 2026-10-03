USE Taskmaster;

CREATE TABLE Estoque (
    EstoqueID INT IDENTITY(1,1) PRIMARY KEY,
    ProdutoID INT NOT NULL,
    QuantidadeAtual INT NOT NULL,
    EstoqueMinimo INT NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

USE Taskmaster;

INSERT INTO Estoque (ProdutoID, QuantidadeAtual, EstoqueMinimo)
VALUES
(1, 15, 5),
(2, 8, 3),
(3, 20, 5),
(4, 12, 4),
(5, 6, 3),
(6, 10, 3),
(7, 18, 5),
(8, 7, 3);

SELECT
    p.NomeProduto,
    e.QuantidadeAtual,
    e.EstoqueMinimo,
    e.EstoqueMinimo - e.QuantidadeAtual AS QuantidadeRepor
FROM Estoque e
INNER JOIN Produtos p
    ON e.ProdutoID = p.ProdutoID
WHERE e.QuantidadeAtual < e.EstoqueMinimo;


UPDATE Estoque
SET QuantidadeAtual = 3
WHERE ProdutoID = 1;

UPDATE Estoque
SET QuantidadeAtual = 2
WHERE ProdutoID = 2;


SELECT
    v.VendaID,
    c.Nome AS Cliente,
    v.DataVenda,
    v.ValorTotal
FROM Vendas v
INNER JOIN Clientes c
    ON v.ClienteID = c.ClienteID
ORDER BY v.VendaID;


SELECT
    ClienteID,
    Nome
FROM Clientes
ORDER BY ClienteID;