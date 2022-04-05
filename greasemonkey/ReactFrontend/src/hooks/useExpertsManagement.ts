import { useCallback, useContext } from "react"
import { ExpertsContext } from "../interfaces/ExpertsContextData"

export const useExpertsManagement = () => {
	const { getExperts } = useContext(ExpertsContext)

	const handleGetExpert = useCallback((company: string) => {
		getExperts(company)
	}, [getExperts])

	return {
		handleGetExpert
	}
}