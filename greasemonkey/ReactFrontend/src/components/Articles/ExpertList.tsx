import { Expert } from "../Article/Expert"
import "./Experts.css"
import { Expert as ExpertType } from "../../interfaces/Expert";
import { useContext } from "react";
import { ExpertsContext } from "../../interfaces/ExpertsContextData";

export const ExpertList = () => {
	const { experts } = useContext(ExpertsContext)
	return (
		<section>
			<div className="container d-flex justify-content-center">
				<div className="experts">
				{ experts.map((expert: ExpertType) => (<Expert key={expert.linkedin} expert={ expert }/>)) }
				</div>
			</div>
		</section>
	)
}