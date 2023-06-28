import React from 'react';
import {
    Card,
    CardBody,
    Badge
} from "reactstrap";


import { Fade } from 'react-reveal';

const EdutionCard = ({education}) => {
    return ( 
        <Fade right duration={1000} distance="40px">
            <Card className="card-lift--hover shadow mt-4">
                <CardBody>
                    <div className="d-flex px-3">
                    <div className="pl-4">
                        <h5 className="text-info">
                        {education.schoolName}
                        </h5>
                        <h6>{education.subHeader}</h6>
                        <Badge color="info" className="mr-1">
                        {education.duration}
                    </Badge>
                        <p className="description mt-3">
                            {education.desc}
                            <ul>
                            {
                                education.descBullets ? 
                                education.descBullets.map((desc) => {
                                    return <li key={desc}>{desc}</li>
                                }) : null
                            }
                            </ul>
                                {education.url ? 
                                  <a href={education.url} target="_blank" rel="noopener noreferrer">Enlace a diploma</a>
                                : null
                                }
                        </p>
                    </div>
                    </div>
                </CardBody>
            </Card>
        </Fade>
     );
}
 
export default EdutionCard;
