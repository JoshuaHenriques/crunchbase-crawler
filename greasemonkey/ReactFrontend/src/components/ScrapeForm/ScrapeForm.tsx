import {  useState } from "react";
import { useExpertsManagement } from "../../hooks/useExpertsManagement";
import "./ScrapeForm.css"

export const ScrapeForm = () => {
  const { handleGetExpert } = useExpertsManagement()
  const [company, setCompany] = useState("");

  return (
    <section className="text-dark mt-5 d-flex justify-content-center">
      <div className="form">
        <form onSubmit={(e) => {e.preventDefault(); handleGetExpert(company)}}>
          <div className="form-group">
            <label htmlFor="exampleFormControlTextarea1">Enter URLS:</label>
            <textarea className="form-control" value={company} onChange={(e) => setCompany(e.target.value)} id="exampleFormControlTextarea1" rows={5} cols={50}></textarea>
            <div id="emailHelp" className="form-text text-center">
              Each url seperated by a newline and use "www." 
            </div>
          </div>
          <div className="text-center mt-4">
            <button type="submit" className="btn btn-primary btn-lg">
              Scrape
            </button>
          </div>
        </form>
      </div>
    </section>
  );
};
