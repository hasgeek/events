---
layout: workshop
title: "Workshop: Design & implement a scalable application using OpenFaaS"
subtitle: "Learn to build and scale applications by building API's for an e-commerce site"
datelocation: "9 AM to 1:30 PM, 19 May 2018, Avi Networks India, Bangalore"
city: Bangalore
start_time: 2018-05-19
end_time: 2018-05-19
description: "Build API’s for an e-commerce site (using OpenFaaS framework) and learn how to connect them via UI and scale this application using Docker & K8’s and touch up monitoring which is an in-built component of OpenFaaS."
boxoffice_item_collection: "e2ea67ca-e20a-4f89-80c9-20641e04c13d"

venue:
  label: Avi Networks India
  address: |
    #110, JB House, 1st Main Rd, 
    5th Block,, Koramangala Industrial Layout,
    Koramangala, Bengaluru, Karnataka 560095.
  lat: 12.934025
  lng: 77.613376
  google_maps_url: https://goo.gl/maps/9sFiG6QKNxK2
  
instructors:
- name: Vivek Sridhar
  image_url: https://images.hasgeek.com/embed/file/830a6dac0c8d49589783c95d1d27c837
  website:
    url: 
    label: 
  byline: Developer Advocate, DigitalOcean
  bio: |
    Vivek is a tech enthusiast with over 11 years experience in the Software Industry. He is currently working as a Developer Advocate with DigitalOcean and has been a Technology Advisor to several tech startups. Previously he was Head of DevOps & QA at Blackbuck and was a DevOps Solution Architect at HCL (Australia) in client engagement and pre-sales roles. Vivek started his career with IBM Rational (INDIA Software Labs) and is passionate about working with software developer communities. 

related_events:
- rootconf-2018
- rootconf-2018-designing-microservices
- rootconf-2018-designing-restful-apis
- rootconf-2018-automation-with-ansible
- rootconf-2018-kubernetes-201
- rootconf-2018-monitoring-servers
- rootconf-2018-unittests-for-python

overview:
  left_content: |

    # Abstract
    
    Is there a better time to be a developer! Thanks to Cloud Computing, deploying applications is much more comfortable than it used to be. Serverless computing is an abstraction layer in the cloud. It does not mean that there are no servers, but instead, underlying infrastructure (VM, storage, containers, etc.), as well as the operating system, is abstracted away from the developer. Applications are run in compute containers that are event triggered. Developers have to create functions and depend on the infrastructure to allocate the proper resources to execute the task. Manage the load by creating copies of the functions and scale to meet the demand. 

    OpenFaaS (Functions as a Service) is a framework for building serverless functions with Docker Swarm or Kubernetes which has fantastic support for metrics. We can package/deploy any simple API / service as a function.

    At a high level in this session, we will discuss and deploy some the functions to Docker Swarm & Kubernetes. We will apply the functions design pattern to build the e-commerce site and learn how to connect functions to UI, connect functions to functions and scale this application with Docker Swarm / Kubernetes. We will touch upon monitoring which is an in-stacked component of OpenFaaS. At the end of the session, participants should be able to build & deploy some of the functions integrated with UI and understand how to orchestrate functions to build applications with some lab exercise.
    

    # Resources

    The material for this workshop will be available on GitHub with documentation and slides used for this workshop.


  right_content: |
    # Outline

    - How infrastructure evolved from DC to functions
        
    - Use - Cases & Problems
    
    - Emerging technologies to solve problems related to scale
    
    - Introduction to the OpenFaaS framework (Hand-On)
    
        - Installing OpenFaaS
    
        - Deploy a function & learn FaaS CLI
    
        - Metrics & Prometheus
    
        - Introduction to Functions templates & deep-dive
    
        - Integrating UI with functions
    
        - Collaborating with other functions
    
        - Auto-Scaling demo with OpenFaaS
        
    # Pre-requisites

    1. This is a hands-on workshop, and hence, participants should bring laptops and should be comfortable with any one of  the programming language (Go, Python3, Python, NodeJS, etc.)
    2. Prior knowledge of Docker / Microservices & DigitalOcean is helpful.

    # Takeaways

    At the end of the session, attendees should be able to build & deploy some of the functions integrated with UI and understand how to orchestrate functions to create scalable applications.


---
