CREATE TABLE Professor (
    id_prof SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    departamento VARCHAR(50) NOT NULL
);

CREATE TABLE Disciplina (
    id_disc SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

CREATE TABLE Turma (
    id_turma SERIAL PRIMARY KEY,
    semestre VARCHAR(10) NOT NULL,
    ano INT NOT NULL,
    id_disc INT NOT NULL,
    id_prof INT NOT NULL,
    FOREIGN KEY (id_disc) REFERENCES Disciplina(id_disc),
    FOREIGN KEY (id_prof) REFERENCES Professor(id_prof)
);

CREATE TABLE Aluno (
    id_aluno SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(50) NOT NULL,
    matricula VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Inscricao (
    id_insc SERIAL PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_turma INT NOT NULL,
    data_insc DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_turma) REFERENCES Turma(id_turma),
    UNIQUE (id_aluno, id_turma)
);

BEGIN;

-- Populando Professor
INSERT INTO Professor (nome, email, departamento) VALUES
('Ana Souza', 'ana.souza@uni.com', 'Matemática'),
('Bruno Lima', 'bruno.lima@uni.com', 'Física'),
('Carla Dias', 'carla.dias@uni.com', 'Química'),
('Daniel Alves', 'daniel.alves@uni.com', 'Biologia'),
('Elisa Torres', 'elisa.torres@uni.com', 'Computação'),
('Fabio Costa', 'fabio.costa@uni.com', 'História');

-- Populando Disciplina
INSERT INTO Disciplina (nome, carga_horaria) VALUES
('Cálculo I', 60),
('Física I', 60),
('Química Geral', 60),
('Biologia Celular', 60),
('Algoritmos', 60),
('História Geral', 60);

-- Populando Turma
INSERT INTO Turma (semestre, ano, id_disc, id_prof) VALUES
('1', 2024, 1, 1),
('1', 2024, 2, 2),
('1', 2024, 3, 3),
('1', 2024, 4, 4),
('1', 2024, 5, 5),
('1', 2024, 6, 6);

-- Populando Aluno
INSERT INTO Aluno (nome, curso, matricula) VALUES
('Gabriel Silva', 'Engenharia', '2024001'),
('Helena Martins', 'Medicina', '2024002'),
('Igor Santos', 'Direito', '2024003'),
('Julia Rocha', 'Computação', '2024004'),
('Kleber Nunes', 'História', '2024005'),
('Larissa Melo', 'Biologia', '2024006');

-- Populando Inscricao
INSERT INTO Inscricao (id_aluno, id_turma) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

COMMIT;