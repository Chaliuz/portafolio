import React, { Fragment } from "react";

import { Fade } from "react-reveal";
import DisplayLottie from "../components/DisplayLottie";
import webdev from "../assets/lottie/webdev.json";

import { Container, Row, Col, UncontrolledTooltip } from "reactstrap";

import { skillsSection } from "../portfolio";

const Skills = () => {
  return (
    <Fade left duration={1000} distance="40px">
      <Container className="text-center my-5 section section-lg">
        <h1 className="h1">{skillsSection.title}</h1>
        <p className="lead">{skillsSection.subTitle}</p>
        <Row>
          <Col lg="6">
            <DisplayLottie animationData={webdev} />
          </Col>
          <Col lg="6">
            <div className="d-flex justify-content-center flex-wrap mb-5">
              {skillsSection.softwareSkills.map((skill) => {
                return (
                  <Fragment key={skill.skillName}>
                    <div
                      // className="icon icon-lg icon-shape shadow rounded-circle mb-5"
                      // className="icon icon-xl icon-shape shadow rounded-circle mb-5"
                      className="icon icon-xl  shadow rounded-circle mb-5"
                      id={skill.skillName}
                      style={{ margin: 4 }}
                    >
                      {skill.fontAwesomeClassname ? (
                        /*<span
                          className="iconify"
                          // className="icon icon-xl icon-shape shadow rounded-circle mb-5"
                          data-icon={skill.fontAwesomeClassname}
                          data-inline="false"
                        ></span>
                        */
                        <></>
                      ) : (
                        <img
                          // className="iconify"
                          className=" bg-white rounded-circle mb--1 img-center img-fluid shadow-lg "
                          // data-icon={skill.image}
                          src={skill.image}
                          alt="imageng"
                          // data-inline="false"
                        />
                      )}
                    </div>
                    <UncontrolledTooltip
                      delay={0}
                      placement="bottom"
                      target={skill.skillName}
                    >
                      {skill.skillName}
                    </UncontrolledTooltip>
                  </Fragment>
                );
              })}
            </div>
            <div>
              {skillsSection.skills.map((skill) => {
                return <p key={skill}>{skill}</p>;
              })}
            </div>
          </Col>
        </Row>
      </Container>
    </Fade>
  );
};

export default Skills;
