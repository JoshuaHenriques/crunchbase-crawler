import { Expert as ExpertType } from "../../interfaces/Expert";

export const Expert = ( { expert }: { expert: ExpertType }) => {
	return (
		<section>
			<div className="card my-5" >
				<div className="card-body">
					<h4 className="card-title">{ expert.name }</h4>
					<p>{ expert.job_title }</p>
					<p>{ expert.job_departments.join(', ') }</p>
					{/* <p>{ expert.linkedin }</p> 
					<p className="card-text">{ expert.company }</p> */}
					<a href={ "https://www.linkedin.com/in/" + expert.linkedin } rel="noreferrer" target="_blank" className="btn btn-primary">Linkedin</a>
				</div>
			</div>
		</section>
	)
}