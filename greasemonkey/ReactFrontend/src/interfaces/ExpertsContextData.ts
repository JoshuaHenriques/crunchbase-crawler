import { createContext } from "react"
import { Expert } from "./Expert"

export interface ExpertsContextData {
	experts: Expert[]
	getExperts: (urls: string) => void
}

export const expertsContextDefaultValue: ExpertsContextData = {
	experts: [],
	getExperts: () => null 
}

export const ExpertsContext = createContext<ExpertsContextData>(expertsContextDefaultValue)