# Symphony-CrescendoA
Assessment
Quick Setup instructions please do follow below steps:

1. Create a postgres database with the name "symphony_CrescendoA_assessment"
2. Update your uname and password of your postgres database in the "app.py" file at line number "14"
3. Create a virtual environment using command "python3 -m virtualenv (name of your environment)"
4. install all the packages in requirement.txt into your local environment using the command "pip install -m requirement.txt"
5. ready to go , Just run the "app.py" file using the command "python app.py"  (as of now we are using a non-prod server).
6. Make the request to the application endpoints below using any tool, such as postman.  


Note:

- On first request all tables will be created at the database.
- Create teams and roles before jumping in to employees .
- sample python script to run the api's are available under the folder "./samples" where you can find payload and other information.


#Endpoint information:

- "/role/register"     -> api to register a Role (POST)
- "/team/register"     -> api to register a Team (POST)
- "/employee/register" -> api to Register a Employee (POST)

- "/employee/<<int:id>>" -> api to get information about Employee on id , (GET) 
                        api to update Employee one or more information(attributes) and finally , (PUT)
                        api to delete employee.  (DELETE)

- "/Budget/max"        -> api to get team which has highest budget. (GET)
- "/Budget/min"        -> api to get team which has lowest budget. (GET)
- "/TeamSize/min"      -> api to get team which is of less in size. (GET)
- "/TeamSize/max"      -> api to get Team which is of larger in size. (GET)
















