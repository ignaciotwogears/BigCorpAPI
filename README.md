# Big Corp API

The idea of this challenge is to develop an **API** with the capability to serve a big amount of data that is obtained from an external service in quota without overuse its endpoints and give a fast response even with 1000 records.
To reach that goal, and after trying 2 or 3 perspectives on testings codes, I decided that the best option was to use the **Pandas** Library to minimize the iterations and speed up times.
Also, I decide to use Flask as a framework for this development because is light and practical for minimalist projects, and in this case, we don't need a database or catching system.

# Endpoints
The specification of the endpoints and its functions are in the documentation folder.

If you are running local the base endpoint is :
```sh
http://localhost:8000/
```
Here you are a collection of possible calls to the service :

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
**And then run :**

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

# A little explanation: 
The following call :

```sh
http://localhost:8000/employees?limit=3&expand=department.superdepartment&expand=manager.office
```
returns the following json data:

```json
[
    {
        "first": "Arthur",
        "last": "Reed",
        "id": 11,
        "manager": {
            "first": "Patricia",
            "last": "Diaz",
            "id": 1,
            "manager": null,
            "department": 5,
            "office": {
                "id": 2,
                "city": "New York",
                "country": "United States",
                "address": "20 W 34th St"
            }
        },
        "department": {
            "id": 10,
            "name": "Product Management",
            "superdepartment": {
                "id": 3,
                "name": "Product",
                "superdepartment": null
            }
        },
        "office": 4
    },
    {
        "first": "Lisa",
        "last": "Long",
        "id": 12,
        "manager": {
            "first": "Daniel",
            "last": "Smith",
            "id": 2,
            "manager": 1,
            "department": 5,
            "office": {
                "id": 2,
                "city": "New York",
                "country": "United States",
                "address": "20 W 34th St"
            }
        },
        "department": {
            "id": 6,
            "name": "Outbound Sales",
            "superdepartment": {
                "id": 1,
                "name": "Sales",
                "superdepartment": null
            }
        },
        "office": 3
    },
    {
        "first": "George",
        "last": "Morgan",
        "id": 13,
        "manager": {
            "first": "Raymond",
            "last": "Allen",
            "id": 7,
            "manager": 4,
            "department": 5,
            "office": {
                "id": 3,
                "city": "London",
                "country": "United Kingdom",
                "address": "32 London Bridge St"
            }
        },
        "department": {
            "id": 7,
            "name": "Application Security",
            "superdepartment": {
                "id": 2,
                "name": "Engineering",
                "superdepartment": null
            }
        },
        "office": 5
    },
    {
        "first": "Matthew",
        "last": "Lopez",
        "id": 14,
        "manager": {
            "first": "Daniel",
            "last": "Smith",
            "id": 2,
            "manager": 1,
            "department": 5,
            "office": {
                "id": 2,
                "city": "New York",
                "country": "United States",
                "address": "20 W 34th St"
            }
        },
        "department": {
            "id": 4,
            "name": "Design",
            "superdepartment": {
                "id": 3,
                "name": "Product",
                "superdepartment": null
            }
        },
        "office": 1
    },
    {
        "first": "Thomas",
        "last": "Washington",
        "id": 15,
        "manager": {
            "first": "Ruth",
            "last": "Morgan",
            "id": 4,
            "manager": null,
            "department": 6,
            "office": {
                "id": 2,
                "city": "New York",
                "country": "United States",
                "address": "20 W 34th St"
            }
        },
        "department": {
            "id": 9,
            "name": "Sales Development",
            "superdepartment": {
                "id": 6,
                "name": "Outbound Sales",
                "superdepartment": {
                    "id": 1,
                    "name": "Sales",
                    "superdepartment": null
                }
            }
        },
        "office": 1
    },
    {
        "first": "Frank",
        "last": "Long",
        "id": 16,
        "manager": {
            "first": "Raymond",
            "last": "Allen",
            "id": 7,
            "manager": 4,
            "department": 5,
            "office": {
                "id": 3,
                "city": "London",
                "country": "United Kingdom",
                "address": "32 London Bridge St"
            }
        },
        "department": {
            "id": 7,
            "name": "Application Security",
            "superdepartment": {
                "id": 2,
                "name": "Engineering",
                "superdepartment": null
            }
        },
        "office": 5
    },
    {
        "first": "Anthony",
        "last": "Stewart",
        "id": 17,
        "manager": {
            "first": "Thomas",
            "last": "Parker",
            "id": 3,
            "manager": null,
            "department": 4,
            "office": null
        },
        "department": {
            "id": 8,
            "name": "Front-End",
            "superdepartment": {
                "id": 2,
                "name": "Engineering",
                "superdepartment": null
            }
        },
        "office": 4
    },
    {
        "first": "Virginia",
        "last": "Hayes",
        "id": 18,
        "manager": {
            "first": "Daniel",
            "last": "Phillips",
            "id": 6,
            "manager": 4,
            "department": 4,
            "office": {
                "id": 1,
                "city": "San Francisco",
                "country": "United States",
                "address": "450 Market St"
            }
        },
        "department": {
            "id": 1,
            "name": "Sales",
            "superdepartment": null
        },
        "office": 2
    },
    {
        "first": "Cynthia",
        "last": "Scott",
        "id": 19,
        "manager": {
            "first": "Frank",
            "last": "Long",
            "id": 16,
            "manager": 7,
            "department": 7,
            "office": {
                "id": 5,
                "city": "Tokyo",
                "country": "Japan",
                "address": "1 Chome-1-2 Oshiage, Sumida City"
            }
        },
        "department": {
            "id": 2,
            "name": "Engineering",
            "superdepartment": null
        },
        "office": 1
    },
    {
        "first": "Gregory",
        "last": "Adams",
        "id": 20,
        "manager": {
            "first": "Lisa",
            "last": "Long",
            "id": 12,
            "manager": 2,
            "department": 6,
            "office": {
                "id": 3,
                "city": "London",
                "country": "United Kingdom",
                "address": "32 London Bridge St"
            }
        },
        "department": {
            "id": 5,
            "name": "Inbound Sales",
            "superdepartment": {
                "id": 1,
                "name": "Sales",
                "superdepartment": null
            }
        },
        "office": 3
    }
]
```

To do that, first of all, the app calls to the endpoint :
``` sh
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit=10&offset=10
```
and then it turn the returned data into a Pandas dataframe with the following result

``` sh
      first        last  id  manager  department  office
0    Arthur        Reed  11        1          10       4
1      Lisa        Long  12        2           6       3
2    George      Morgan  13        7           7       5
3   Matthew       Lopez  14        2           4       1
4    Thomas  Washington  15        4           9       1
5     Frank        Long  16        7           7       5
6   Anthony     Stewart  17        3           8       4
7  Virginia       Hayes  18        6           1       2
8   Cynthia       Scott  19       16           2       1
9   Gregory       Adams  20       12           5       3

```
to find the manager to all the employees the app make the following call to the external service filling all the needed employees in the dataframe

``` sh
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=1&id=2&id=7&id=4&id=3&id=6
```
as a result we get this new dataframe :

``` sh
0    Arthur        Reed  11      1.0          10     4.0
1      Lisa        Long  12      2.0           6     3.0
2    George      Morgan  13      7.0           7     5.0
3   Matthew       Lopez  14      2.0           4     1.0
4    Thomas  Washington  15      4.0           9     1.0
5     Frank        Long  16      7.0           7     5.0
6   Anthony     Stewart  17      3.0           8     4.0
7  Virginia       Hayes  18      6.0           1     2.0
8   Cynthia       Scott  19     16.0           2     1.0
9   Gregory       Adams  20     12.0           5     3.0
0  Patricia        Diaz   1      NaN           5     2.0
1    Daniel       Smith   2      1.0           5     2.0
2   Raymond       Allen   7      4.0           5     3.0
3      Ruth      Morgan   4      NaN           6     2.0
4    Thomas      Parker   3      NaN           4     NaN
5    Daniel    Phillips   6      4.0           4     1.0
```


