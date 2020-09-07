# Big Corp API

The idea of this challenge is to develop an **API** with the capability to serve a big amount of data that is obtained from middleware in quota without overuse of its endpoints and give a fast response even with 1000 records.
To reach that goal, and after trying 2 or 3 perspectives on testings codes, I decided that the best option was to use the **Pandas** Library to minimize the iterations and speed up times.
Also, I decide to use Flask as a framework for this development because is light and practical for minimalist projects and in this case we dont need database or catching system.

# Endpoints
The specification of the endpoints and its functions are in the documentation folder.

If you are running local the base endpoint is :
```sh
http://localhost:8000/
```
And here a collection of possibles calls to the endpoints and its process:

```sh
/employees?limit=3&expand=department
```
```sh
/employees?limit=3&expand=department.superdepartment&expand=manager.office
```
```sh
/departments/9?expand=superdepartment.superdepartment
```
```sh
/employees?limit=1000&offset=10000&expand=manager.manager.manager
```


# Implementation
this project it's developed with CI with Github Workflows so, each time that the code is pushed to the master branch, the testings will be run, and if everything it's fine, the Docker image will be pushed to the Docker hub.
you can just  pull the image :
```sh
docker pull ignaciotwogears/bigcorpapi
```
And then run :
```sh
docker run -p 8000:8000  ignaciotwogears/bigcorpapi
```
of course, you can also run the code installing the dependencies or build your local image with the dockerfile.

# Kubernetes
In the **Kubernetes** folder yo will find the deployment.yaml
**Just run :**
kubectl apply -f deployment.yaml
and the deployment and service will be created!
The new base endpoint will be :
```sh
http://localhost:31006/
```

