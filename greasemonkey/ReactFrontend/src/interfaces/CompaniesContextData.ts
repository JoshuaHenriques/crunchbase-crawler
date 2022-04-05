import { createContext } from "react"
import { Company } from "./Company"

export interface CompaniesContextData {
	companies: Company[]
	getCompanies: () => void
}

export const companiesContextDefaultValue: CompaniesContextData = {
	companies: [],
	getCompanies: () => null 
}

export const CompaniesContext = createContext<CompaniesContextData>(companiesContextDefaultValue)