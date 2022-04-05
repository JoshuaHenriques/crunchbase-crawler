import {  useContext, useEffect, useState } from "react";
import { useCompaniesManagement } from "../../hooks/useCompaniesManagement";
import { useExpertsManagement } from "../../hooks/useExpertsManagement";
import { CompaniesContext } from "../../interfaces/CompaniesContextData";
import "./Selection.css"

export const Selection = () => {
	const { companies } = useContext(CompaniesContext)
  const { handleGetExpert } = useExpertsManagement()
  const [company, setCompany] = useState("Select Company")
  const { handleGetCompanies } = useCompaniesManagement()

  useEffect(() => {
    const getCompanies = () => {
      handleGetCompanies()
    }

    getCompanies()
  }, [handleGetCompanies])

  return (
    <section className="text-dark mt-5 d-flex justify-content-center">
      <div className="form">
        <form onSubmit={(e) => {
            e.preventDefault()
            console.log(company)
            if(company != "Select Company") {
              handleGetExpert(company)
            } 
            }}>          
          <select className="form-select" aria-label="Default select example" onChange={(e) => setCompany(e.target.value)}>
            <option defaultValue="Select Company" value="Select Company">Select Company</option>
            { companies.map((option) => (<option key={option.name} value={option.name}>{option.name.charAt(0).toUpperCase() + option.name.slice(1)}</option>)) }
          </select>
          <div className="text-center mt-4">
            <button type="submit" className="btn btn-primary btn-md">
              Get Experts
            </button>
          </div>
        </form>
      </div>
    </section>
  );
};
