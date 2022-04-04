import { Request, Response } from "express"
import { Company } from "../../types/Company"
import { Expert } from "../../types/Expert"
import { insertCompany, insertExpert } from "../../apis/database"

export const getExperts = async (req: Request) => {
    const company: string = req.body.experts
}