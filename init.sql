CREATE DATABASE IF NOT EXISTS uni_registro;
USE uni_registro;
-- Tabela de Professores (reuso da Ideia 1)
CREATE TABLE Professor (
id_prof INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
departamento VARCHAR(50) NOT NULL
);
-- Tabela de Disciplinas (reuso da Ideia 1)
CREATE TABLE Disciplina (
id_disc INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
carga_horaria INT NOT NULL
);
-- Tabela de Turmas (reuso da Ideia 1)
CREATE TABLE Turma (
id_turma INT AUTO_INCREMENT PRIMARY KEY,
semestre VARCHAR(10) NOT NULL,
ano INT NOT NULL,
id_disc INT NOT NULL,
id_prof INT NOT NULL,
FOREIGN KEY (id_disc) REFERENCES Disciplina(id_disc),
FOREIGN KEY (id_prof) REFERENCES Professor(id_prof)
);
-- Nova tabela: Alunos
CREATE TABLE Aluno (
id_aluno INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
curso VARCHAR(50) NOT NULL,
matricula VARCHAR(20) UNIQUE NOT NULL
);
-- Nova tabela: Inscrições
CREATE TABLE Inscricao (
id_insc INT AUTO_INCREMENT PRIMARY KEY,
id_aluno INT NOT NULL,
id_turma INT NOT NULL,
data_insc DATE NOT NULL DEFAULT CURRENT_DATE(),
FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
FOREIGN KEY (id_turma) REFERENCES Turma(id_turma),
UNIQUE KEY uq_aluno_turma (id_aluno, id_turma)
);