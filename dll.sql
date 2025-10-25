-- Lógico_1: Sistema de Vacinação

CREATE TABLE Paciente (
    id_paciente VARCHAR(255) PRIMARY KEY,
    sexo VARCHAR(50),
    municipio VARCHAR(255),
    uf VARCHAR(2),
    idade INT,
    raca_cor VARCHAR(50)
);

CREATE TABLE EstrategiaVacinacao (
    id_estrategia_vacinacao INT PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE Estabelecimento (
    id_cnes INT PRIMARY KEY,
    nome_fantasia VARCHAR(255),
    razao_social VARCHAR(255),
    municipio VARCHAR(255),
    tipo VARCHAR(100)
);

CREATE TABLE Vacina (
    id_vacina INT PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE Fabricante (
    id_fabricante INT PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE fabrica (
    id_vacina INT,
    id_fabricante INT,
    PRIMARY KEY (id_vacina, id_fabricante),
    CONSTRAINT FK_fabrica_Vacina
        FOREIGN KEY (id_vacina)
        REFERENCES Vacina(id_vacina)
        ON DELETE RESTRICT,
    CONSTRAINT FK_fabrica_Fabricante
        FOREIGN KEY (id_fabricante)
        REFERENCES Fabricante(id_fabricante)
        ON DELETE RESTRICT
);

CREATE TABLE _AplicacaoDose_Estabelecimento_Vacina_Paciente (
    id_aplicacao VARCHAR(255) PRIMARY KEY,
    data_vacina DATE,
    local_aplicacao VARCHAR(100),
    via_administracao VARCHAR(100),
    dose_vacina VARCHAR(50),
    lote_vacina VARCHAR(100),
    cod_estrategia_vacinacao INT,
    cnes INT,
    cod_vacina INT,
    cod_paciente VARCHAR(255),
    CONSTRAINT FK_AplicacaoDose_EstrategiaVacinacao
        FOREIGN KEY (cod_estrategia_vacinacao)
        REFERENCES EstrategiaVacinacao(id_estrategia_vacinacao)
        ON DELETE CASCADE,
    CONSTRAINT FK_AplicacaoDose_Estabelecimento
        FOREIGN KEY (cnes)
        REFERENCES Estabelecimento(id_cnes)
        ON DELETE RESTRICT,
    CONSTRAINT FK_AplicacaoDose_Vacina
        FOREIGN KEY (cod_vacina)
        REFERENCES Vacina(id_vacina)
        ON DELETE RESTRICT,
    CONSTRAINT FK_AplicacaoDose_Paciente
        FOREIGN KEY (cod_paciente)
        REFERENCES Paciente(id_paciente)
        ON DELETE RESTRICT
);

