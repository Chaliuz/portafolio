import React from "react";
import EdutionCard from "../components/EdutionCard";
import { educationInfo } from "../portfolio";
import { Container, Row, Col } from "reactstrap";

const Edution = () => {
  return (
    <section className="section pb-0 bg-gradient-info my-5 bg-primary text-white">
      <Container>
        <div className="d-flex px-3">
          <div>
            <div className="icon icon-lg icon-shape bg-gradient-white shadow rounded-circle text-info">
              <i className="ni ni-books text-info" />
            </div>
          </div>
          <div className="pl-4">
            <h4 className="display-3 text-white">Educación</h4>
          </div>
        </div>
        {/* old */}
        {/* --------------------------------------------------- */}
        <Row className="row-grid align-items-center">
          {educationInfo.map((info) => {
            return (
              <Col className="order-lg-1" lg="5" px="0" key={info.schoolName}>
                <EdutionCard education={info} />
              </Col>
            );
          })}
        </Row>
        {/* --------------------------------------------------- */}
        {/* new */}
        {/* --------------------------------------------------- */}
        <div className="d-flex flex-wrap align-items-stretch">
          {educationInfo.map((info) => {
            return (
              <div className="w-25 m-2" key={info.schoolName}>
                <EdutionCard education={info} />
              </div>
            );
          })}
        </div>



        {/* --------------------------------------------------- */}
      </Container>
      <div className="separator separator-bottom separator-skew zindex-100">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          preserveAspectRatio="none"
          version="1.1"
          viewBox="0 0 2560 100"
          x="0"
          y="0"
        >
          <polygon className="fill-white" points="2560 0 2560 100 0 100" />
        </svg>
      </div>
    </section>
  );
};

export default Edution;
