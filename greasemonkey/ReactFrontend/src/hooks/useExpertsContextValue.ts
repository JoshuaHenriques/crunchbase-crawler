import { useCallback, useState } from "react";
import { Expert } from "../interfaces/Expert"
import { ExpertsContextData } from "../interfaces/ExpertsContextData";

export const useExpertsContextValue = (): ExpertsContextData => {
	const [experts, setExperts] = useState<Expert[]>([])

	const getExperts = useCallback(async (company: string) => {
		// Maybe try React Query?
		// const parsedUrls: string[] = company.split('\n')
		try {
			const res = await fetch(`http://localhost:4000/getExperts?company=${company}`, {
				method: "GET",
				headers: {
				"Access-Control-Allow-Origin": "*",
				"Content-type": "application/json"
				},
			})
			const data = await res.json()
			console.log(data)
			setExperts(data.experts)
		} catch(e) {
			console.log(e)
		}
	  }, [setExperts])
	return { experts, getExperts }
}