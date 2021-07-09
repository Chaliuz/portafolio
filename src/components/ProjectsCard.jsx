import React from "react";

import { Card, CardBody, Col, Button } from "reactstrap";

import { Fade } from "react-reveal";

import YouTube from "react-youtube";

const ProjectsCard = ({ data }) => {
  return (
    <Col lg="6">
      <Fade bottom duration={1000} distance="40px">
        <Card className="shadow-lg--hover shadow mt-4">
          <CardBody>
            <div className="d-flex px-3">
              <div className="pl-4">
                <h5 className="text-info">{data.name}</h5>
                <p className="description mt-3">{data.desc}</p>
                {data.link ? (
                  <Button
                    className="btn-neutral btn-icon"
                    color="primary"
                    href={data.link.url}
                    target="_blank"
                  >
                    <span className="btn-inner--icon">
                      <i className="fa fa-arrow-right mr-2" />
                    </span>
                    <span className="nav-link-inner--text ml-1">
                      {data.link.name}
                    </span>
                  </Button>
                ) : null}

                {data.technologies ? (
                  <>
                    <p className="description mt-3">
                      Las tecnologías que usé fueron:
                    </p>
                    <ul>
                      {data.technologies.map((element) => (
                        <li>{element}</li>
                      ))}
                    </ul>
                  </>
                ) : null}

                {data.youtube ? (
                  <YouTube
                    videoId={"vBdkIV7YfYU"} // defaults -> null
                    opts={{ width: "95%" }}
                  />
                ) : null}
              </div>
            </div>
          </CardBody>
        </Card>
      </Fade>
    </Col>
  );
};

export default ProjectsCard;
