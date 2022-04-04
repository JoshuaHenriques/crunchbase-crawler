import { Request, Response } from "express"
import { getCompaniesDB } from "../../apis/database"

export const getCompanies = async (req: Request, res: Response) => {
    const companies = await getCompaniesDB()

    res.setHeader("Content-Type", "application/json");
    res.json({ companies: companies });
    res.end();
}