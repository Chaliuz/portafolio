import React from "react";
// import { BrowserRouter, Route, Switch } from "react-router-dom";

import Navigation from "./components/Navigation";
import Greetings from "./containers/Greetings";
import Skills from "./containers/Skills";
import Proficiency from "./containers/Proficiency";
import Education from "./containers/Education";
import Experience from "./containers/Experience";
import Projects from "./containers/Projects";
import GithubProfile from "./containers/GithubProfile";
const App = () => {
  return (
    // <BrowserRouter>
    //   <Switch>
    //     <Route
    //       path="/"
    //       exact
    //       render={(props) => (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <Navigation />
      <Greetings />
      <Skills />
      <Proficiency />
      <Education />
      <Experience />
      <Projects />
      <GithubProfile />
    </div>
    //       )}
    //     />
    //   </Switch>
    // </BrowserRouter>
  );
};

export default App;
