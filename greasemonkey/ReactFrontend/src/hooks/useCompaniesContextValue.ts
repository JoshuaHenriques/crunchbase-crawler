import { useCallback, useState } from "react";
import { CompaniesContextData } from "../interfaces/CompaniesContextData";
import { Company } from "../interfaces/Company";

export const useCompaniesContextValue = (): CompaniesContextData => {
	const [companies, setCompanies] = useState<Company[]>([])

	const getCompanies = useCallback(async () => {
		// Maybe try React Query?
		// const parsedUrls: string[] = company.split('\n')
		try {
			const res = await fetch(`http://localhost:4000/getCompanies`, {
				method: "GET",
				headers: {
				"Access-Control-Allow-Origin": "*",
				"Content-type": "application/json"
				},
			})
			const data = await res.json()
			console.log(data)
			setCompanies(data.companies)
		} catch(e) {
			console.log(e)
		}
	  }, [setCompanies])
	return { companies, getCompanies }
}