create extension if not exists "uuid-ossp";

create table if not exists expert (
    created_at      timestamp       default current_timestamp,
    updated_at      timestamp        default current_timestamp,
    id              uuid            not null primary key default uuid_generate_v4(),
    name            varchar(255)    not null,
    phone_number    varchar(10),
    email           varchar(255),
    linkedin        varchar(255),
    job_title       varchar(255),
    job_departments text[],
    company         varchar(255)
);

create table if not exists company (
    created_at      timestamp       default current_timestamp,
    updated_at      timestamp        default current_timestamp,
    id              uuid            not null,
    name            varchar(255)    not null
);