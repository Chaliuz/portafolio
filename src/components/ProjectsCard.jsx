import React from "react";

import { Card, CardBody, Col, Button } from "reactstrap";

import { Fade } from "react-reveal";

import YouTube from "react-youtube";

import AwesomeSlider from "react-awesome-slider";
import "react-awesome-slider/dist/styles.css";

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
                  <div
                    style={
                      {
                        // display: "flex",
                        // justifyContent: "center",
                        // alignSelf: "center",
                        // alignItems: "center",
                        // width: "87%",
                      }
                    }
                  >
                    <YouTube videoId={data.youtube} opts={{ width: "95%" }} />
                  </div>
                ) : null}
                {data.imgs_for_slider ? (
                  <div
                    style={{
                      display: "flex",
                      // alignSelf: "center",
                      justifyContent: "center",
                      marginBottom: 50,
                    }}
                  >
                    <AwesomeSlider
                      // media={[
                      //   {
                      //     source: android_logo,
                      //   },
                      //   {
                      //     source: aws_logo,
                      //   },
                      //   {
                      //     source: docker_logo,
                      //   },
                      // ]}
                      style={{ height: 400, width: 200 }}
                      media={data.imgs_for_slider}
                    />
                  </div>
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
