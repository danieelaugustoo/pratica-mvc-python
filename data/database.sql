create database if not exists agenda;

use agenda;

drop table if exists `tarefa`;

create table if not exists `tarefa` (
    `id` int not null `auto_increment` primary key,
    `titulo` varchar(60) not null,
    `data_conclusao` datetime null
);
Estudar MySQL
Levar o cachorro para passear
Ir ao estádio assistir ao jogo Palmeiras x Corinthians



