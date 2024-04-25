import React, { Fragment } from "react";

import { Fade } from "react-reveal";
import DisplayLottie from "../components/DisplayLottie";
import webdev from "../assets/lottie/webdev.json";

import { Container, Row, Col, UncontrolledTooltip } from "reactstrap";

import { skillsSection } from "../portfolio";


import react_logo from "../assets/img/icons/skills/react_logo.png";

const Skills = () => {
  return (
    <Fade left duration={1000} distance="40px">
      <Container className="text-center my-5 section section-lg" >
        <h1 className="h1">{skillsSection.title}</h1>
        <p className="lead">{skillsSection.subTitle}</p>
        <div style={{ display: "flex", flexDirection: "row", justifyContent: "center", alignItems: "start", flexWrap: "wrap", marginBlock: "25px" }}>
          <TechBranch title={"Frontend"} skillsSection={skillsSection.softwareSkillsFrontend} />
          <TechBranch title={"Backend"} skillsSection={skillsSection.softwareSkillsBackend} />
          <TechBranch title={"Devops"} skillsSection={skillsSection.softwareSkillsDevops} />
          <TechBranch title={"Others"} skillsSection={skillsSection.softwareSkillsOthers} />
        </div>

        <Row>
          <Col lg="6">
            <DisplayLottie animationData={webdev} />
          </Col>
          <Col lg="6" className="flex flex-col justify-center align-center" >
            {/* <Fade left duration={1000} distance="40px"> */}
            {/*   <div className="d-flex justify-content-center flex-wrap mb-5"> */}
            {/* {skillsSection.softwareSkills.map((skill) => { */}
            {/*   return ( */}
            {/*     <Fragment key={skill.skillName}> */}
            {/*       <div */}
            {/*         // className="icon icon-lg icon-shape shadow rounded-circle mb-5" */}
            {/*         // className="icon icon-xl icon-shape shadow rounded-circle mb-5" */}
            {/*         className="icon icon-xl  shadow rounded-circle mb-5" */}
            {/*         id={skill.skillName} */}
            {/*         style={{ margin: 4 }} */}
            {/*       > */}
            {/*         {skill.fontAwesomeClassname ? ( */}
            {/*           <></> */}
            {/*         ) : ( */}
            {/*             <img */}
            {/*               // className="iconify" */}
            {/*               className=" bg-white rounded-circle mb--1 img-center img-fluid shadow-lg " */}
            {/*               // data-icon={skill.image} */}
            {/*               src={skill.image} */}
            {/*               alt="imageng" */}
            {/*             // data-inline="false" */}
            {/*             /> */}
            {/*           )} */}
            {/*       </div> */}
            {/*       <UncontrolledTooltip */}
            {/*         delay={0} */}
            {/*         placement="bottom" */}
            {/*         target={skill.skillName} */}
            {/*       > */}
            {/*         {skill.skillName} */}
            {/*       </UncontrolledTooltip> */}
            {/*     </Fragment> */}
            {/*   ); */}
            {/* })} */}
            {/*   </div> */}
            {/* </Fade> */}

            <div className="mt-8" >
              {skillsSection.skills.map((skill) => {
                return <p key={skill}>{skill}</p>;
              })}
            </div>
          </Col>
        </Row>
      </Container>
    </Fade >
  );
};


function TechBranch({ title, skillsSection }) {
  return (

    <div className="card-lift--hover shadow mt-5" style={{
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      // borderStyle: "solid",
      // borderWidth: "3px",
      // borderColor: "#15cceb",
      width: "400px",
      margin: "15px",
      borderRadius: "5px",
      backgroundColor: "#15cceb"
    }}>
      <p style={{ fontSize: "25px", fontWeight: "bold", margin: "10px", color: "white" }}>{title}</p>
      <div style={{ width: "70%", marginBottom: "15px" }}>
        {
          skillsSection.map((el) => (
            <div style={{ display: "flex", flexDirection: "row", justifyContent: "space-between", alignItems: "center", margin: "20px", }}>
              <img
                className=" bg-white rounded-circle mb--1 img-center img-fluid shadow-lg "
                src={el.image}
                alt="imageng"
                // data-inline="false"
                style={{ width: "55px", flex: "0.2" }}
              />

              <div style={{ display: "flex", flexDirection: "column", flex: "0.8" }}>
                <span style={{ flex: "0.8", fontSize: "20px", color: "white" }}>{el.skillName}</span>
                {el.url &&
                  (
                    <a style={{}} href={el.url} target="_blank" rel="noopener noreferrer">Certificado</a>
                  )
                }

              </div>
            </div>
          ))
        }
      </div>

    </div >
  )
}




export default Skills;
