import { Request, Response } from "express"
import { getExpertsDB } from "../../apis/database"

export const getExperts = async (req: Request, res: Response) => {
    const company = req.query.company
    const experts = await getExpertsDB(company)

    res.setHeader("Content-Type", "application/json");
    res.json({ experts: experts });
    res.end();
}