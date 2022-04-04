import { Request, Response } from "express"
import { Company } from "../../types/entities/Company"
import { Expert } from "../../types/entities/Expert"
import { insertCompany, insertExpert } from "../../apis/database/database"
import exp from "constants"

export const experts = async (req: Request, res: Response) => {
    // console.log(req.body)
    const experts: Expert[] = req.body.experts
    const company: Company = req.body.company
    console.log(company)
    // console.log(experts)
    // const expertsList: any = req.body

    insertCompany(company)
    experts.forEach((expert) => {
        insertExpert(expert, company.name)
    })
}