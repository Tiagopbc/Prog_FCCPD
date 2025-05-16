CREATE DATABASE uni_registro;

\c uni_registro;

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
