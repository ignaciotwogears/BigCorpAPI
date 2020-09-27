# Big Corp API
## Python + Flask + Pandas + Docker + Kubernetes

The idea of this challenge is to develop an **API** with the capability to serve a big amount of data that is obtained from an external service in quota without overuse its endpoints and give a fast response even with 1000 records.
To reach that goal, and after trying 2 or 3 perspectives on testings codes, I decided that the best option was to use the **Pandas** Library to minimize the iterations and speed up times.
Also, I decide to use Flask as a framework for this development because is light and practical for minimalist projects, and in this case, we don't need a database or catching system.

# Endpoints
The full detail of all the endpoints and its functions are in the documentation folder.

If you are running locally, the base endpoint its :
```sh
http://localhost:8000/
```
Here you are a collection of possible functions to the service :

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
This project implements CI on GitHub, so, each time that the code is pushed to the master branch, it will run the tests, and if everything it's fine, it will build a Docker image and push to Docker Hub.

you can just  pull the image :

```sh
docker pull ignaciotwogears/bigcorpapi
```

And then run :

```sh
docker run -p 8000:8000  ignaciotwogears/bigcorpapi
```

Of course, you can also run the code installing the dependencies or build your local image with the dockerfile.

# Kubernetes
In the **Kubernetes** folder yo will find the deployment.yaml
**Just run :**

```sh
kubectl apply -f deployment.yaml
```

Then the deployment and service will be created!
The new base endpoint will be :
```sh
http://localhost:31006/
```

# A little explanation: 
The call :

```sh
http://localhost:8000/employees?limit=10&offset=10&expand=department.superdepartment&expand=manager.office
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
to find a manager to all the employees, the app make the following call to the external service filling all the needed employees in the dataframe

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

Now, with all the necessary data, the expanders functions add all the requested objects recursively diving as deep as necessary.
The combination of the powerful Pandas search tool and recursive logic allows the API to resolve the following endpoint with limit  = 1000

``` sh
http://localhost:8000/employees?limit=1000&offset=1000&expand=department.superdepartment&expand=manager.office
``` 

with just 5 calls to the external Employees service as can be seen below: 

``` sh


https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?limit=1000&offset=1000
        first        last    id  manager  department  office
0       Henry     Sanders  1001    974.0         3.0     3.0
1       Donna        Wood  1002    398.0         3.0     3.0
2      Robert     Collins  1003    237.0         3.0     1.0
3        Mark      Watson  1004    950.0         9.0     3.0
4    Margaret      Butler  1005    877.0         9.0     3.0
..        ...         ...   ...      ...         ...     ...
995    Donald       Brown  1996   1462.0         4.0     5.0
996    Sandra    Peterson  1997    213.0         1.0     5.0
997     Peter  Richardson  1998    617.0         5.0     5.0
998   Raymond      Wilson  1999   1242.0         2.0     1.0
999   Jessica     Bennett  2000    501.0         NaN     4.0

[1000 rows x 6 columns]
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=974&id=398&id=237&id=950&id=877&id=443&id=589&id=539&id=490&id=265&id=836&id=200&id=273&id=132&id=124&id=517&id=14&id=334&id=738&id=766&id=494&id=722&id=732&id=109&id=503&id=645&id=114&id=736&id=764&id=980&id=871&id=260&id=682&id=228&id=66&id=845&id=104&id=807&id=617&id=433&id=596&id=675&id=225&id=678&id=699&id=910&id=366&id=280&id=779&id=992&id=976&id=676&id=667&id=955&id=916&id=507&id=710&id=985&id=915&id=790&id=920&id=839&id=446&id=457&id=905&id=500&id=822&id=355&id=191&id=502&id=222&id=215&id=244&id=70&id=296&id=812&id=550&id=91&id=860&id=261&id=171&id=818&id=27&id=147&id=975&id=385&id=547&id=813&id=862&id=811&id=674&id=497&id=525&id=185&id=611&id=605&id=521&id=89&id=994&id=692&id=754&id=192&id=245&id=815&id=462&id=635&id=332&id=153&id=735&id=873&id=425&id=454&id=353&id=595&id=336&id=658&id=799&id=157&id=423&id=677&id=489&id=496&id=504&id=116&id=319&id=30&id=828&id=181&id=344&id=217&id=361&id=434&id=615&id=422&id=96&id=668&id=18&id=387&id=113&id=282&id=141&id=878&id=733&id=803&id=223&id=770&id=478&id=728&id=404&id=129&id=183&id=46&id=411&id=325&id=341&id=240&id=45&id=639&id=256&id=308&id=511&id=214&id=295&id=750&id=740&id=949&id=771&id=925&id=909&id=88&id=300&id=603&id=844&id=886&id=866&id=655&id=206&id=456&id=155&id=796&id=488&id=825&id=359&id=253&id=284&id=591&id=557&id=956&id=867&id=218&id=697&id=734&id=9&id=742&id=406&id=962&id=464&id=115&id=652&id=898&id=221&id=413&id=670&id=306&id=486&id=289&id=219&id=226&id=447&id=653&id=907&id=726&id=53&id=996&id=208&id=665&id=122&id=227&id=49&id=946&id=405&id=101&id=701&id=287&id=933&id=213&id=792&id=763&id=608&id=357&id=460&id=587&id=317&id=80&id=609&id=380&id=636&id=477&id=888&id=884&id=778&id=448&id=960&id=646&id=911&id=902&id=144&id=628&id=354&id=810&id=231&id=369&id=663&id=57&id=823&id=758&id=233&id=528&id=581&id=816&id=599&id=187&id=571&id=461&id=847&id=963&id=98&id=304&id=103&id=194&id=186&id=32&id=570&id=997&id=647&id=903&id=679&id=20&id=708&id=536&id=106&id=241&id=99&id=857&id=301&id=724&id=322&id=900&id=363&id=814&id=631&id=381&id=315&id=626&id=691&id=530&id=932&id=546&id=326&id=310&id=880&id=440&id=633&id=463&id=23&id=625&id=881&id=277&id=291&id=555&id=607&id=467&id=804&id=458&id=775&id=38&id=51&id=700&id=182&id=869&id=585&id=367&id=704&id=906&id=373&id=479&id=720&id=575&id=170&id=559&id=269&id=800&id=944&id=684&id=556&id=242&id=239&id=450&id=452&id=594&id=318&id=190&id=988&id=627&id=7&id=149&id=54&id=441&id=908&id=899&id=331&id=174&id=130&id=748&id=10&id=15&id=339&id=400&id=672&id=475&id=545&id=416&id=466&id=706&id=958&id=805&id=620&id=167&id=207&id=274&id=188&id=897&id=506&id=173&id=968&id=830&id=255&id=892&id=695&id=453&id=505&id=583&id=768&id=356&id=661&id=797&id=193&id=29&id=510&id=621&id=688&id=872&id=418&id=35&id=78&id=436&id=431&id=681&id=632&id=62&id=572&id=430&id=943&id=876&id=961&id=864&id=25&id=561&id=715&id=26&id=396&id=5&id=662&id=347&id=564&id=415&id=789&id=527&id=508&id=72&id=616&id=540&id=481&id=254&id=549&id=566&id=386&id=362&id=216&id=680&id=515&id=4&id=904&id=977&id=112&id=939&id=321&id=257&id=592&id=79&id=47&id=235&id=352&id=8&id=299&id=410&id=541&id=250&id=841&id=753&id=934&id=468&id=648&id=482&id=420&id=397&id=654&id=476&id=795&id=829&id=376&id=232&id=767&id=484&id=991&id=842&id=776&id=532&id=21&id=941&id=426&id=50&id=408&id=516&id=485&id=491&id=970&id=36&id=156&id=1000&id=102&id=435&id=111&id=95&id=542&id=195&id=288&id=707&id=731&id=761&id=741&id=1&id=143&id=794&id=229&id=140&id=382&id=338&id=826&id=875&id=150&id=940&id=774&id=938&id=492&id=923&id=999&id=501
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=136&id=158&id=39&id=43&id=236&id=22&id=117&id=198&id=2&id=134&id=148&id=146&id=424&id=348&id=55&id=360&id=638&id=81&id=94&id=178&id=97&id=13&id=574&id=378&id=330&id=68&id=41&id=388&id=37&id=76&id=480&id=403&id=473&id=151&id=365&id=64&id=358&id=268&id=164&id=75&id=840&id=641&id=161&id=297&id=105&id=126&id=48&id=618&id=172&id=168&id=512&id=61&id=52&id=267&id=197&id=417&id=127&id=159&id=123&id=93&id=24&id=278&id=166&id=548&id=85&id=11&id=6&id=154&id=162&id=717&id=252&id=163&id=138&id=455&id=563&id=74&id=421&id=560&id=262&id=176&id=368&id=83&id=340&id=3&id=67&id=145&id=71&id=125&id=333&id=179&id=384&id=34&id=184&id=613&id=119&id=264&id=42&id=328&id=311&id=210&id=108&id=12&id=619&id=316&id=432&id=31&id=59&id=377&id=137&id=73&id=17&id=276&id=28&id=470&id=290&id=90&id=650&id=259&id=346&id=44&id=660&id=303&id=224&id=275&id=401&id=428&id=281&id=142&id=211&id=567&id=798&id=177&id=893&id=58&id=391&id=370&id=372&id=393&id=725&id=364&id=769&id=472&id=246&id=629&id=294&id=63&id=19&id=554&id=371&id=569&id=696&id=861&id=469&id=251&id=597&id=442&id=534&id=196&id=498&id=110&id=947&id=69&id=586&id=263&id=614&id=307&id=234&id=375&id=509&id=175&id=202&id=739&id=806&id=392&id=929&id=579&id=286
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=87&id=84&id=16&id=324&id=399&id=33&id=258&id=199&id=56&id=128&id=107&id=531&id=247&id=212&id=40&id=409&id=60&id=180&id=238&id=606&id=189&id=329&id=522&id=558&id=445&id=139
https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees?id=100
       first     last    id  manager  department  office
0      Henry  Sanders  1001    974.0         3.0     3.0
1      Donna     Wood  1002    398.0         3.0     3.0
2     Robert  Collins  1003    237.0         3.0     1.0
3       Mark   Watson  1004    950.0         9.0     3.0
4   Margaret   Butler  1005    877.0         9.0     3.0
..       ...      ...   ...      ...         ...     ...
22     Larry    Kelly   522    144.0         1.0     NaN
23  Kimberly   Morris   558    413.0        10.0     1.0
24   Stephen   Watson   445    146.0         2.0     5.0
25    Thomas   Flores   139    109.0         1.0     NaN
0    Richard   Rogers   100      1.0         5.0     4.0

[1712 rows x 6 columns]
       first     last    id  manager  department  office
0      Henry  Sanders  1001    974.0         3.0     3.0
1      Donna     Wood  1002    398.0         3.0     3.0
2     Robert  Collins  1003    237.0         3.0     1.0
3       Mark   Watson  1004    950.0         9.0     3.0
4   Margaret   Butler  1005    877.0         9.0     3.0
..       ...      ...   ...      ...         ...     ...
22     Larry    Kelly   522    144.0         1.0     NaN
23  Kimberly   Morris   558    413.0        10.0     1.0
24   Stephen   Watson   445    146.0         2.0     5.0
25    Thomas   Flores   139    109.0         1.0     NaN
0    Richard   Rogers   100      1.0         5.0     4.0

[1712 rows x 6 columns]
``` 

I hope you have enjoyed reading this project and of course I am open to any suggestions and improvements.


