# Django Project (Nucamp)

### Description

A back-end REST API project related to a cloud content management repository for a network of hospitals. It aims to provide a range of administrative functionalities and services related to content hosting, tracking and management. 
Authorized users within the network can access, upload, and download contents based on their access permissions defined in the security group attribute. Admins can look up detailed information of hosted contents by searching for specific metadata, can set up and configure user or group access depending on the hospital or hospitals they are affiliated with. The ER diagram contains seven related entities: User, Hosted Content, Uploaded Content, Checkedout Content, Hostpital, Department, Cost Center. They are divided into three API apps. This design decision is to allow decoupling and cohesion among models and views.
The end goal is to implement a robust list of REST endpoints and a combination of unit & integration tests. **(Front-end UI is outside the scope of the project)**


### Featured Framework and Tools

    * Django 
    * Django REST Framework
    * Python
    * PostgreSQL
    * AWS (work-in-progress)
    
&nbsp;&nbsp;&nbsp;
### ER Diagram 

![ERD_1](https://user-images.githubusercontent.com/11815017/188238637-4060ab20-aa63-4833-9d0e-e970e20094a7.jpg)

&nbsp;&nbsp;&nbsp;
![ERD_2](https://user-images.githubusercontent.com/11815017/188229724-6549b493-7106-4841-accd-576c0ecef388.jpg)

![Postgres_ERD](https://user-images.githubusercontent.com/11815017/189986197-7802d5c9-9407-49b0-9609-c0394e0edb03.jpg)


&nbsp;&nbsp;&nbsp;
### Endpoint URL List
![API Endpoints](https://user-images.githubusercontent.com/11815017/188231778-e56f405e-e1f8-483e-9208-7c33fd89414d.jpg)

&nbsp;
### Admin Database
![Admin Database_1](https://user-images.githubusercontent.com/11815017/188232444-018f5c81-b3df-4a26-bc6a-d2d7008098fc.jpg)

![Admin Database_2](https://user-images.githubusercontent.com/11815017/188232478-add0dacd-fef5-4304-8dfc-2b5dea235f5d.jpg)

![Admin Database_3](https://user-images.githubusercontent.com/11815017/188232522-fd88c811-7508-41f6-87a7-e37b353a47ba.jpg)


&nbsp;
### HTTP Response Examples for Custom Endpoints
![GET_a list of COC by user](https://user-images.githubusercontent.com/11815017/188232622-f4ed622f-d7dd-4b93-ad56-0138c4c8f699.jpg)

![GET_a list of COC by hospital](https://user-images.githubusercontent.com/11815017/188232725-3071dba8-32a7-407c-a8bf-ae131c31642d.jpg)

![GET_a list of COC by date](https://user-images.githubusercontent.com/11815017/188232790-2402265a-e15f-425f-bd64-c35bf8e3260f.jpg)

&nbsp;&nbsp;
### HTTP Response Examples for Standard Endpoints
![GET_a list of hospitals](https://user-images.githubusercontent.com/11815017/188233197-abec0787-caa5-46ef-9e1b-d20d1f9fe8c2.jpg)

![GET_a list of departments](https://user-images.githubusercontent.com/11815017/188233282-c9ae8dce-0934-4c24-b5df-c92e211b2e09.jpg)

![GET_a list of cost-centers](https://user-images.githubusercontent.com/11815017/188233348-87b60b76-d0ba-4214-872a-176c26edd59c.jpg)


&nbsp;&nbsp;&nbsp;
### Links Related To My Project &nbsp;

LINK TO VIDEO PRESENTATION: 

[https://drive.google.com/file/d/1-rg23ynuA69pwaWXBENM3AljMlgp2Ss1/view?usp=sharing](https://drive.google.com/file/d/1-rg23ynuA69pwaWXBENM3AljMlgp2Ss1/view?usp=sharing)

LINK TO GITHUB:

[https://github.com/jy492330/DevOps_Project](https://github.com/jy492330/DevOps_Project)

LINK TO AWS DATABASE:

[http://ec2-13-52-7-52.us-west-1.compute.amazonaws.com:8000/api/users/](http://ec2-13-52-7-52.us-west-1.compute.amazonaws.com:8000/api/users/)



