import { useCallback, useContext } from "react"
import { CompaniesContext } from "../interfaces/CompaniesContextData"

export const useCompaniesManagement = () => {
	const { getCompanies } = useContext(CompaniesContext)

	const handleGetCompanies = useCallback(() => {
		getCompanies()
	}, [getCompanies])

	return {
		handleGetCompanies
	}
}