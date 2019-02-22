# This replaces script Connectdb.py.
# By Jose Aguilar on 2/21/2019.
# Parachute Project.

import pyodbc

'''

Objective.
===========

serverbase serves as an interface between SQL database (Parachute's database) and project.

Description.
------------

server base access the SQL database stored in azure which manages by the use of
two tables the information of the users.

the database contains two tables:

1. **dbo.parachute**:
    - This table holds all of the login and user information.
    - This table is accessed to authenticate the users.
    - Database Structure of Main Table (dbo.parachute):

| null?     |  Y  |      Y      |      Y      |      N     |      Y      |      Y      |
| --------- | --- | ----------- | ----------- | ---------- | ----------- | ----------- |
|   Column  | ID  |  Last Name  | First Name  | Department |  Username   |   Password  |
| --------- |---- | ----------- | ----------- | ---------- | ----------- | ----------- |
|   value   | id  |    lname    |    fname    |     dep    |      usr    |    psw      |
| --------- |---- | ----------- | ----------- | ---------- | ----------- | ----------- |
| data type | int | varchar(50) | varchar(50) | varchar(50)| varchar(50) | varchar(50) |

_The `id` field will use constrains `PRIMARY KEY` and `IDENTITY`_

    2. ** dbo.%user% ** _(%user% means user name.)_
        - This table holds the information of the user that deals with the time
          sheets.
        - Database Structure of User Table (dbo.%User%):

|    nul?   |  Y  |    Y     |     Y     |     Y      |       N       |
| --------- | --- | -------- | --------- | ---------- | ------------- |
|  Column   | ID  | Check in | Check out | Total Time | Description   |
| ----------| --- | -------- | --------- | ---------- | ------------- |
|   value   | id  |   chkin  |   chkout  |    time    | description   |
| --------- | --- | -------- | --------- | ---------- | ------------- |
| data type | int | datetime | datetime  |  time(2)   | varchar(1000) |

_The `id` field will use constrains `PRIMARY KEY` and `IDENTITY`_

Note that the methods that access and mutate the data in the dbo.parachute table
**cannot change the usr and id fields. If a change of user is required, then,
contacting the administrator of the database will do**

Methods:
=========

__init__(usr: string, psw: string): **constructor**
---------------------------------------------------------------------------------------------

#### Arguments:
usr: string
    - user name to be used for login process.
psw: string
    - password to be used for login process.

#### Description:
The constructor takes care of three things:
    1. connection to the internet. (OperationalError by pyodbc)
    2. validates connection the string. (InterfaceError by pyodbc)
    3. authentication of the user name and password. (KeyChainError by dbdriver)
The constructor will not take care of any exceptions; therefore, **it is the
responsability of the method calling and instantiating the object to wrap the
call in a try-except block!**
Once the connection to the server has been established and the user name and
password were succesfully authenticated in the database, the constructor
proccedes to save the connection string into `connectionstring: string` and the
user name and password into `keychain: [usr: string, psw: string]`.

fetchrow(id: int): [id: int, chkin: date, chkout: date, time: time, description: string/null]
---------------------------------------------------------------------------------------------

#### Arguments:
id: int
    - The row number as set in the database `ID` column.

#### Description:
The method acesses the database with the connection string and the login
information to retrieve the entire row that has the same value in the ID column
as the `id` argument.
If no such row exists, a NoDataOnCursorError exception is thrown.

#### Return:
[id: int, chkin: date, chkout: date, time: time, description: string/null]
    - The list returned holds the entire row that has the same value as the `id`
      argument and is organized in the exact order as in the SQL database.
_Note that the description field can be either a string or a null value._

fetch(id: int, column: string): string/null
---------------------------------------------------------------------------------------------

#### Arguments:
id: int
    - The row number as set in the database `ID` column.
column: string
    - The column name from where the data is to be retrieved.

#### Description:
The method acesses the database with the connection string and the login
information to retrieve the data that is holded in the cell that is on the same
row as the `id` value as the `id` argument and the same column that is titled as
the `column` argument.
If no such cell exists, a NoDataOnCursorError exception is thrown.

#### Return:
string/null
    - The value found in the cell on the row with the same `ID` column value as
      the `id` argument and on the same column title as `column` argument.

appendrow(data: [chkin: date, chkout: date, time: time, description: string/null]): void
---------------------------------------------------------------------------------------------

#### Arguments:
data:  [chkin: date, chkout: date, time: time, description: string/null]
    - The data to be appended at the end of dbo.%user% table. The order on how
      the data is organized **matters.**
    - The ID value of the table is **auto generated.** when the data is appended

#### Description:
The data is grouped and inserted into a SQL query to modify the existing table
and append a new row at the end of the table. As mentioned before, the ID value
is auto generated and cannot be customized.

#### Return:
No Return.

setcell(id: int, column: string, value: string): void
---------------------------------------------------------------------------------------------

#### Arguments:
id: int
    - the ID value to be compared with inside the table to select the cell to be
      replaced
column: string
    - The name of the Column where the data is to be inserted.
value: string
    - The data value that it is to be set

#### Description:
The `value` argument is inserted into the dbo.%user% table where the row
contains an `ID` value equal to the `id` argument; and where the column name is
the same as the `column` argument.

#### Return:
No Return.

getusrinfo(void): [id: int, lname: string, fname: string, dep: string/null]
---------------------------------------------------------------------------------------------

#### Arguments:
No arguments.

#### Description:
Based on the keychain list, the user information is returned.
This includes:
1. id in the database of the user.  (id)     [0]
2. last name of the user.           (lname)  [1]
3. first name of the user.          (fname)  [2]
4. department of the user.          (dep)    [3]
    - _Note that the department field may be a string or null._

#### Return:
[id: int, lname: string, fname: string, dep: string/null]
    - List containing the basic data of the user.

getkeychain(void): [usr: string, psw: string]
---------------------------------------------------------------------------------------------

#### Arguments:
No arguments.

#### Description:
Simply returns the keychain list. (see keychain value)
#### Return:
[usr: string, psw: string]
    - List containing the information of the user name and password of the user.
        1. user name   (usr)  [0]
        2. password    (psw)  [1]

setusrinfo([lname: string, fname: string, dep: string]): void
---------------------------------------------------------------------------------------------

#### Arguments:
[lname: string, fname: string, dep: string]
    - Contains the information of the user to be set.

#### Description:
Creates a SQJ query to replace the data of the user with the new data._
_Note that the data does not contain password or user name. This is because that_
_the user name cannot be changed and likewise the password requires an_
_alternative method to be changed._

#### Return:
No Return.

setpsw(psw: string)
---------------------------------------------------------------------------------------------
#### Arguments:
psw: string
    - The new password to be set up.

#### Description:
Replaces the old password with a new password. The method changed the keychain
value and the `psw` entry in the dbo.%usr% table.

#### Return:
No Return.

Values:
========

connectionstring: string
    - Contains the connection string to connect to the database.

keychain: [usr: string, psw: string]
    - Contains the user name and password of the user.

'''
class serverbase():
    def __init__():
        pass
