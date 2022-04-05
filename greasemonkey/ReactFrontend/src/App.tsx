import "bootstrap/dist/css/bootstrap.min.css";

import { ScrapeForm } from "./components/ScrapeForm/ScrapeForm";
import { Header } from "./components/Header/Header";
import { ExpertsContext } from "./interfaces/ExpertsContextData";
import { ExpertList } from "./components/Articles/ExpertList";
import { useExpertsContextValue } from "./hooks/useExpertsContextValue";

export const App = () => {
  const expertsContextValue = useExpertsContextValue()

  return (
    <ExpertsContext.Provider value={expertsContextValue}>
      <Header />
      <ScrapeForm />
      <ExpertList />
      {/* <Pagination nextPage={nextPage} prevPage={prevPage} /> */}
      {/* <Footer /> */}
    </ExpertsContext.Provider>
  );
};

export default App;
