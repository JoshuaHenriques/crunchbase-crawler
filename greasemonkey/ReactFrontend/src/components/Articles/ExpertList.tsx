import { Expert } from "../Article/Expert"
import "./Experts.css"
import { Expert as ExpertType } from "../../interfaces/Expert";
import { useContext } from "react";
import { ExpertsContext } from "../../interfaces/ExpertsContextData";

export const ExpertList = () => {
	const { experts } = useContext(ExpertsContext)
	return (
		<section>
			<div className="container">
				<div className="row">
				{ experts.map((expert: ExpertType) => (
					<div className="col-4"  key={expert.linkedin}>
						<Expert key={expert.linkedin} expert={ expert }/>
					</div>
					)) }
				</div>
			</div>
		</section>
	)
}