import { Request, Response } from "express"
import { Company } from "../../types/Company"
import { Expert } from "../../types/Expert"
import { insertCompany, insertExpert } from "../../apis/database"

export const experts = async (req: Request) => {
    const experts: Expert[] = req.body.experts
    const company: Company = req.body.company

    insertCompany(company)
    experts.forEach((expert) => {
        insertExpert(expert, company.name)
    })
}