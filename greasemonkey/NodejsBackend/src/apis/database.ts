import { Expert } from "../types/Expert";
import { Company } from "../types/Company"

const pgp = require("pg-promise")();
const db = pgp("postgres://postgres:example@localhost:5433/postgres");

export const insertCompany = async (company: Company) => {
  await db.none(
    "INSERT INTO company(id, name) VALUES($1, $2)",
    [
      company.id,
      company.name,
    ]
  )
}

export const insertExpert = async (expert: Expert, company: string) => {
  await db.none(
    "INSERT INTO expert(name, job_title, job_departments, linkedin, company) VALUES($1, $2, $3, $4, $5)",
    [
      expert.name,
      expert.jobTitle,
      expert.jobDepartments,
      expert.linkedIn,
      company
    ]
  )
}