import requests
import json, pprint
import pathlib
# variable region


BASE_URL = "http://saral.navgurukul.org/api/courses"
jsonData={}
def printText(text):
    print ("\n\n\t"+"*"*20+text+"*"*20+"\t\n\n")

printText("WELCOME TO SARAL")    

# colling API by get in function.
def getResp(api):
    getData = requests.get(api)                                                     
    jsonData = getData.json()
    return jsonData


# Write json_data in courses.json file. 
def writeData(data,fileName):
    with open(fileName, "w") as writeIt: 
	    writeIt.write(json.dumps(data))
    writeIt.close()


# Read the json_data from courses.json file.
def readData(fileName):
    with open(fileName, "r") as readIt: 
        readJson = json.load(readIt)
    return readJson

def getData(fileName,url):
    file = pathlib.Path(fileName)
    if file.exists ():
        read_json = readData("courses.json")
        jsonData=read_json
    else:
        jsonData=getResp(url)
        writeData(jsonData,"courses.json")

    return jsonData

jsonData = getData("courses.json",BASE_URL)

def getCourses(jsonData):
    index = 0
    while index<len(jsonData["availableCourses"]):
        print  (str(index)+"."+jsonData["availableCourses"][index]["name"])
        index = index+1
    
getCourses(jsonData)

printText("*"*10)
def getCourseId(jsonData):
    userInput = input("Enter your course number :- ")
    courseId = (jsonData["availableCourses"][int(userInput)]["id"])
    print (courseId)
    return courseId

courseId = getCourseId(jsonData)

# exercises calling API 

printText("COURSES EXERCISES")    
exerciseUrl = BASE_URL+"/"+str(courseId)+"/exercises"
exercisesData = getData("exercises.json",exerciseUrl)
def getExercises(exercisesData):
    index = 0
    while index<len(exercisesData["data"]):
        print  (str(index)+"."+exercisesData["data"][index]["name"])
        index = index+1
    
getCourses(exercisesData)

printText("*"*10)
def getCourseId(exercisesData):
    userInput = input("Enter your course number :- ")
    exersisesId = (jsonData["data"][int(userInput)]["id"])
    print (exersisesId)
    return exersisesId

exersisesId = getCourseId(exercisesData)


