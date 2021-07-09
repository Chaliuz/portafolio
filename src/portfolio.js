import emoji from "react-easy-emoji";

import connecttix from "./assets/img/icons/common/connecttix.jpg";
import logo_app_lecturapp from "./assets/img/icons/common/logo_app_lecturapp.png";

import android_logo from "./assets/img/icons/skills/android_logo.png";
import aws_logo from "./assets/img/icons/skills/aws_logo.png";
import docker_logo from "./assets/img/icons/skills/docker_logo.png";
import firebase_logo from "./assets/img/icons/skills/firebase_logo.png";
import flexbox_logo from "./assets/img/icons/skills/flexbox_logo.png";
import git_logo from "./assets/img/icons/skills/git_logo.png";
import google_cloud_logo from "./assets/img/icons/skills/google_cloud_logo.png";
import jest_logo from "./assets/img/icons/skills/jest_logo.png";
import linux_logo from "./assets/img/icons/skills/linux_logo.png";
import materialui_logo from "./assets/img/icons/skills/materialui_logo.png";
import node_logo from "./assets/img/icons/skills/node_logo.png";
import nvim_logo from "./assets/img/icons/skills/nvim_logo.png";
import react_logo from "./assets/img/icons/skills/react_logo.png";
import react_native_logo from "./assets/img/icons/skills/react_native_logo.png";
import redux_logo from "./assets/img/icons/skills/redux_logo.png";
import redux_persist_logo from "./assets/img/icons/skills/redux_persist_logo.png";
import scrum_logo from "./assets/img/icons/skills/scrum_logo.png";

// image projects:
import adn1 from "./assets/img/icons/projects/ADNVoladura/adn1.png";
import adn2 from "./assets/img/icons/projects/ADNVoladura/adn2.png";
import adn3 from "./assets/img/icons/projects/ADNVoladura/adn3.png";
import adn4 from "./assets/img/icons/projects/ADNVoladura/adn4.png";
import adn6 from "./assets/img/icons/projects/ADNVoladura/adn6.png";
import adn7 from "./assets/img/icons/projects/ADNVoladura/adn7.png";
import adn10 from "./assets/img/icons/projects/ADNVoladura/adn10.png";
import adn12 from "./assets/img/icons/projects/ADNVoladura/adn12.png";

// image projects:
import lecturapp1 from "./assets/img/icons/projects/lecturapp/lecturapp1.png";
import lecturapp2 from "./assets/img/icons/projects/lecturapp/lecturapp3.png";
import lecturapp3 from "./assets/img/icons/projects/lecturapp/lecturapp5.png";
import lecturapp4 from "./assets/img/icons/projects/lecturapp/lecturapp7.png";
import lecturapp5 from "./assets/img/icons/projects/lecturapp/lecturapp8.png";
import lecturapp6 from "./assets/img/icons/projects/lecturapp/lecturapp11.png";

export const greetings = {
  name: "Gonzalo Quispe Fernandez",
  title: "¿Que tal?, yo soy Gonzalo",
  // title: "¿Que tal?, me llamo Gonzalo",
  description:
    // "A passionate Full Stack Web Developer and Mobile App Developer having an experience of building Web applications with JavaScript / Reactjs / Nodejs / Python / Django / Flask and some other cool libraries and frameworks and Cross Platform Mobile Apps With Flutter.",
    "Soy un desorrallor de software frontend apasionado por la tecnología, con habilidades de liderazgo, enfocado en las tecnologías de React y React-Native.",
  // resumeLink: "https://cv.hanzla.ga",
  resumeLink:
    "https://drive.google.com/file/d/1-rolr535gPTq6ZXSsgb02c2PI9JtsD87/view?usp=sharing",
};

export const openSource = {
  githubUserName: "Chalius",
};

export const contact = {};

export const socialLinks = {
  // facebook: "https://www.facebook.com/1hanzla100",
  facebook: "https://www.facebook.com/gonzalo.quispefernandez/",
  // instagram: "https://www.instagram.com/1hanzla100",
  // twitter: "https://twitter.com/1hanzla100",
  github: "https://github.com/Chalius",
  // linkedin: "https://www.linkedin.com/in/hanzla-tauqeer-0869281ba/",
  linkedin: "https://www.linkedin.com/in/gquispe/",
  telegram: "https://t.me/chalius",
};

export const skillsSection = {
  // title: "What I do",
  title: "Lo que hago",
  // subTitle: "CRAZY FULL STACK DEVELOPER WHO WANTS TO EXPLORE EVERY TECH STACK",
  subTitle:
    "DESARROLLADOR FROND END QUE QUIERE CONVERTIRSE EN EXPERTO FULLSTACK CON LAS TECNOLOGÍAS MERN.",
  // "LAS TECNOLOGÍAS QUE MÁS SUELO USAR SON LAS SIGUIENTES",
  skills: [
    /* emoji(
    "⚡ Develop highly interactive Front end / User Interfaces for your web and mobile applications"
  ),
  emoji("⚡ Progressive Web Applications ( PWA ) in normal and SPA Stacks"),
  emoji(
    "⚡ Integration of third party services such as Firebase/ AWS / Digital Ocean"
  ), */
    emoji(
      "⚡ Desarrollo de aplicaciones multiplataforma para iOS y Android usando react-native"
    ),
    emoji("⚡ Desarrollo de páginas web usando React y css3 Flex-box"),
    emoji(
      "⚡ Integración de servicios de terceros como Firebase / AWS / Google cloud"
    ),
    emoji(
      "⚡ Tengo conocimientos sobre temas de emprendimiento y habilidades de liderazgo"
    ),
  ],

  softwareSkills: [
    {
      skillName: "reactjs",
      // fontAwesomeClassname: "vscode-icons:file-type-reactjs",
      image: react_logo,
    },
    {
      skillName: "react-native",
      image: react_native_logo,
    },
    {
      skillName: "redux",
      image: redux_logo,
    },
    {
      skillName: "redux-persist",
      image: redux_persist_logo,
    },
    {
      skillName: "css3-Flexbox",
      // fontAwesomeClassname: "vscode-icons:file-type-css",
      image: flexbox_logo,
    },
    {
      skillName: "MaterialUI",
      image: materialui_logo,
    },
    {
      skillName: "Git-GitHub-GitLab",
      image: git_logo,
    },
    {
      skillName: "Jest",
      image: jest_logo,
    },
    {
      skillName: "Docker",
      image: docker_logo,
    },
    {
      skillName: "aws",
      image: aws_logo,
    },
    {
      skillName: "firebase",
      image: firebase_logo,
    },
    {
      skillName: "google-cloud",
      image: google_cloud_logo,
    },
    {
      skillName: "linux",
      image: linux_logo,
    },
    {
      skillName: "android",
      image: android_logo,
    },
    {
      skillName: "nodeJS",
      image: node_logo,
    },
    {
      skillName: "NeoVim",
      image: nvim_logo,
    },
    {
      skillName: "SCRUM",
      image: scrum_logo,
    },

    /*
    {
      skillName: "html-5",
      fontAwesomeClassname: "vscode-icons:file-type-html",
    },
    {
      skillName: "JavaScript",
      fontAwesomeClassname: "logos:javascript",
    },
    {
      skillName: "TypeScript",
      fontAwesomeClassname: "logos:typescript-icon",
    },
    {
      skillName: "nodejs",
      fontAwesomeClassname: "logos:nodejs-icon",
    },
    {
      skillName: "npm",
      fontAwesomeClassname: "vscode-icons:file-type-npm",
    },
    {
      skillName: "aws",
      fontAwesomeClassname: "logos:aws",
    },
    {
      skillName: "firebase",
      fontAwesomeClassname: "logos:firebase",
    },
    {
      skillName: "git",
      fontAwesomeClassname: "logos:git-icon",
    },
    {
      skillName: "docker",
      fontAwesomeClassname: "logos:docker-icon",
    },
    */
    /* {
    skillName: "flutter",
    fontAwesomeClassname: "logos:flutter",
  }, */
    /* {
    skillName: "swift",
    fontAwesomeClassname: "vscode-icons:file-type-swift",
  }, */
    /* {
    skillName: "python",
    fontAwesomeClassname: "logos:python",
  }, */
    /* {
    skillName: "mongoDB",
    fontAwesomeClassname: "vscode-icons:file-type-mongo",
  }, */
    /* {
    skillName: "sass",
    fontAwesomeClassname: "logos:sass",
  }, */
  ],
};

export const SkillBars = [
  {
    Stack: "React-Native",
    progressPercentage: "80",
  },
  {
    /* Stack: "Frontend/Design", //Insert stack or technology you have experience in
  progressPercentage: "90", //Insert relative proficiency in percentage */
    Stack: "React", //Insert stack or technology you have experience in
    progressPercentage: "70", //Insert relative proficiency in percentage
  },
  {
    Stack: "Redux",
    progressPercentage: "70",
  },
  {
    Stack: "Flex-box",
    progressPercentage: "60",
  },
  {
    Stack: "Emprendimiento",
    progressPercentage: "60",
  },
  {
    Stack: "Backend con node.js:",
    progressPercentage: "50",
  },
];

export const educationInfo = [
  {
    /* schoolName: "Harvard University",
  subHeader: "Master of Science in Computer Science",
  duration: "September 2017 - April 2019",
  desc: "Participated in the research of XXX and published 3 papers.",
  descBullets: [
    "Lorem ipsum dolor sit amet, consectetur adipdfgiscing elit",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
  ], */
    schoolName: "Instituto tecnológico TECSUP",
    subHeader: "Desarrollo de software e integración de sistemas",
    duration: "Marzo 2018 - Enero 2021",
    desc: "Egresé en el decimo superior ocupando el 2do puesto de mi promoción.",
    /* descBullets: [
    "Lorem ipsum dolor sit amet, consectetur adipdfgiscing elit",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
  ], */
  },
  {
    /* schoolName: "Harvard",
  subHeader: "Master of Science in Computer Science",
  duration: "September 2017 - April 2019",
  desc: "Participated in the research of XXX and published 3 papers.",
  descBullets: [
    "Lorem ipsum dolor sit amet, consectetfgur adipiscing elit",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
  ], */
    schoolName: "Universidad Nacional de San Agustín (UNSA)",
    subHeader: "Ingeniería de minas",
    duration: "September 2012 - April 2017",
    desc: "Entré a trabajar en la mina Cerro Verde.",
    /* descBullets: [
    "Lorem ipsum dolor sit amet, consectetfgur adipiscing elit",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    ], */
  },
  /* {
    schoolName: "Stanford University",
    subHeader: "Bachelor of Science in Computer Science",
    duration: "September 2013 - April 2017",
    desc: "Ranked top 10% in the program. Took courses about Software Engineering, Web Security, Operating Systems, ...",
    descBullets: ["Lorem ipsum dolorfdg sit amet, consectetur adipiscing elit"],
  }, */
];

export const experience = [
  {
    /* role: "Front-End Developer",
    company: "Github",
    companylogo: github,
    date: "May 2017 – May 2018",
    desc: "Lorem ipsum dolor sit amet, consefdctetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", */
    role: "Desarrollo móvil multiplataforma",
    company: "Emprendimiento propio",
    companylogo: logo_app_lecturapp,

    date: "Enero 2021 – Actualidad",
    desc: "Desorrolló a medio tiempo un aplicativo multiplataforma usando React-Native. Esta app busca hacer gustar la lectura a los niños.",
  },
  {
    /* role: "software engineer",
    company: "google",
    companylogo: googlelogo,
    date: "june 2018 – present",
    desc: "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    descbullets: [
      "lorem ipsum dolor sit amet, consdfgectetur adipiscing elit",
      "lorem ipsum dolor sit amet, consectetur adipiscing elit",
    ], */
    role: "Desarrollador de software móvil",
    company: "ConnectiX",
    companylogo: connecttix,

    date: "Noviembre 2019 – Febrero 2020",
    desc: "Desarrolló de aplicativo Android para el control de gasolina de camioneros.",
    /* descbullets: [
      "lorem ipsum dolor sit amet, consdfgectetur adipiscing elit",
      "lorem ipsum dolor sit amet, consectetur adipiscing elit",
    ], */
  },
  /* {
    role: "Software Engineer Intern",
    company: "Airbnb",
    companylogo: airbnb,
    date: "Jan 2015 – Sep 2015",
    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  }, */
];

export const projects = [
  {
    name: "LecturApp",
    desc: "Emprendimiento que desarrolla un aplicativo móvil que consulta la información en un backend desarrollado con node.js. ",
    technologies: [
      "React-Native",
      "Redux",
      "Redux-persist",
      "Figma",
      "Lean Canvas",
    ],
    imgs_for_slider: [
      { source: lecturapp1 },
      { source: lecturapp2 },
      { source: lecturapp3 },
      { source: lecturapp4 },
      { source: lecturapp5 },
      { source: lecturapp6 },
    ],
  },

  /* import android_logo2 from "../assets/img/icons/skills/android_logo.png";
import aws_logo2 from "../assets/img/icons/skills/aws_logo.png";
import docker_logo2 from "../assets/img/icons/skills/docker_logo.png"; */

  {
    name: "ADNVoladura",
    desc: "Aplicativo móvil que resuelve complicadas formulas matemáticas para facilitar la tarea de operadores de minería a cielo abierto.",
    technologies: ["React-Native", "Redux", "Redux-persist"],
    imgs_for_slider: [
      { source: adn1 },
      { source: adn2 },
      { source: adn3 },
      { source: adn4 },
      { source: adn6 },
      { source: adn7 },
      { source: adn10 },
      { source: adn12 },
    ],
  },
  {
    name: "Robot Araña",
    desc: "Robot que se controla mediante internet desarrollado con Arduino que captura datos como: temperatura, humedad, etc. y se lo envía a un servidor para que los almacene.",
    technologies: ["Arduino", "Django", "Android"],
    youtube: "vBdkIV7YfYU",
    /* link: {
      name: "hanzla",
      url: "kasjfklsdjf",
    }, */
  },
  {
    name: "App para restaurante",
    desc: "Aplicativo multiplataforma que sirve para realizar pedidos de comida.",
    technologies: ["React-native", "Firebase"],
    youtube: "5ebskOPeNFQ",
    /* link: {
      name: "hanzla",
      url: "kasjfklsdjf",
    }, */
  },
];
