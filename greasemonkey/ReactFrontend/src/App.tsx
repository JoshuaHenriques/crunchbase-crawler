import "bootstrap/dist/css/bootstrap.min.css";

import { Selection } from "./components/Selection/Selection";
import { Header } from "./components/Header/Header";
import { ExpertsContext } from "./interfaces/ExpertsContextData";
import { ExpertList } from "./components/Articles/ExpertList";
import { useExpertsContextValue } from "./hooks/useExpertsContextValue";
import { useCompaniesContextValue } from "./hooks/useCompaniesContextValue";
import { CompaniesContext } from "./interfaces/CompaniesContextData";

export const App = () => {
  const expertsContextValue = useExpertsContextValue()
  const companiesContextValue = useCompaniesContextValue()

  return (
    <ExpertsContext.Provider value={expertsContextValue}>
      <CompaniesContext.Provider value={companiesContextValue}>
        <Header />
        <Selection />
        <ExpertList />
      {/* <Pagination nextPage={nextPage} prevPage={prevPage} /> */}
      </CompaniesContext.Provider>
    </ExpertsContext.Provider>
  );
};

export default App;
