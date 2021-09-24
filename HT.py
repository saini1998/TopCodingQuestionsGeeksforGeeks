import json
import requests

def getData():
    """
    Function to get data from URL and print response
    """
    link = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=c8996ee3dfbceaa210f61784f427'
    response = requests.get(link)
    print("Get: ", response)
    data = response.json()
    return data

def post(data):
    """
    Function to post data to URL and print response
    """
    link = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=c8996ee3dfbceaa210f61784f427'
    response = requests.post(link, data=json.dumps(data))
    print('Post: ', response)

def makePairs(data):
    """
    Input: data from url response
    Forms pairs of dates in each country for two consecutive days and also find number of partners available for each pair
    """

    for country in countries:
        datesList = []
        for item in countryDatesList:
            for key in item:                    
                if country == key:
                    for i in item[key]:
                        if i not in datesList:
                            datesList.append(i)                             # list datesList contains dates available for partners in a country

        datesList.sort()                                                    # datesList is sorted

        currCountryDates[country] = datesList                               # dictionary currCountryDates that stores current value of country in list countries with available sorted dates
        consecutiveDates = []                                               # list to contain tuples of consecutive dates

        for date in range(len(datesList)-1):                                # loop to make tuples of consecuitve dates and append it to the list consecutiveDates 

            dd=int(datesList[date].split('-')[-1])
            dd1 = int(datesList[date+1].split('-')[-1])                     # splitting date dd from dd-mm-yyyy

            mm = int(datesList[date].split('-')[-2])
            mm1 = int(datesList[date + 1].split('-')[-2])                   # splitting month mm from dd-mm-yyyy

            yyyy = int(datesList[date].split('-')[-3])
            yyyy1 = int(datesList[date + 1].split('-')[-3])                 # splitting year yyyy from dd-mm-yyyy

            if ( dd+1==dd1 and mm==mm1 and yyyy==yyyy1 ):                   # check for consecutive dates
                datesTuple = (datesList[date],datesList[date+1])
                consecutiveDates.append(datesTuple)

            if dd == 30:                                                    # check if the date is 30 and falling in month of thirty days(april,june,sep,nov), then, to form a consecutive days tuple, next date(dd1) should be 01 of the next month
                if datesList[date].split('-')[-2] in month30:               # check if the month has 30 days
                   if dd1 == 1 and \
                       int(datesList[date+1].split('-')[-2])-1 == int(datesList[date].split('-')[-2]) and \
                           int(datesList[date+1].split('-')[-3]) == int(datesList[date].split('-')[-3]):

                       datesTuple = (datesList[date],datesList[date+1])
                       consecutiveDates.append(datesTuple)

            if dd==31:                                                      # check if the date is 31, then, to form a consecutive days tuple, next date(dd1) should be 01 of the next month
                if dd1 == 1 and \
                    int(datesList[date + 1].split('-')[-2]) - 1 == int(datesList[date].split('-')[-2]) and \
                        int(datesList[date+1].split('-')[-3])==int(datesList[date].split('-')[-3]):

                    datesTuple = (datesList[date], datesList[date + 1])
                    consecutiveDates.append(datesTuple)

        currCountryConsDates[country] = consecutiveDates                    # dictionary  currCountryConsDates with keys as country and values as list of tuples of conseutive date

        count = 0
        count1 = 0
        listdateCount = []

        for item in consecutiveDates:                                       # count number of partners availabe for every pair of dates for each country
                count1 = 0
                email = []
                for partner in data['partners']:
                    count = 0
                    if country == partner['country']:
                        for i in item:
                            if i in partner['availableDates']:
                                 count += 1

                    if count == 2:
                        count1 += 1
                        email.append(partner['email'])

                t = (item,count1,email)                                     # tuple t contains pair of dates, number of attendees avialabe for that pair of dates, and their email
                listdateCount.append(t)                                     # list contains all the above tuples t created for a pair of date
        
        dateWithTotal[country] = listdateCount                              # after the loop ends for each pair of date for every country respectively, a dictionary is created with key as name of country and value contains above list(listdateCount)

finall = []                                                                 # list that will contain reuired enteries for output

def dataFormat(dateWithTotal):
    """
    Function to make final json format
    """
    for item in dateWithTotal:                                              
            q = []

            for lst in dateWithTotal[item]:
                q.append(lst[1])

            m=max(q)

            for lst in dateWithTotal[item]:
                if lst[1] == m:
                    entry = dict()
                    entry = {
                        'attendeeCount': m,
                        'attendees': lst[2],
                        'name': item,
                        'startDate': lst[0][0] if len(lst[2])>0 else "null"
                    }
                    finall.append(entry)
                    break
    return finall                                                           # returns the final json format data

"""
----------------------------------------------------------> Main Function Starts
"""

if __name__ == "__main__":

    data = getData()                                                        # call to function getData()

    countryDatesList = []                                                   # list of dictionaries with country as key and available dates as values
    month30 = ['04','06','09','011']                                        # list month30 that contains months with 30 days
 

    for partner in data['partners']:                                        # loop to retrieve every partner in data
        countryDates = dict()                                               # dictionary that contains countries as key and available dates as values for each individual partners
        countryDates[partner['country']] = partner['availableDates']
        countryDatesList.append(countryDates)                               # each dictionary gets appended to the list for each partner


    countries = []                                                          # list of countries with partners present in data
    for item in countryDatesList:
        for key in item:
            if key not in countries:
                countries.append(key)

    currCountryDates = dict()
    currCountryConsDates = dict()
    dateWithTotal = dict()

    makePairs(data)                                                         # function call to makePairs

    finall = dataFormat(dateWithTotal)                                      # function returns final json format data

    
    resultData = dict()
    resultData['countries'] = finall                                        # dictionary that contain desired json format data
    # print(json.dumps(resultData,indent=2))

    post(resultData)

"""
----------------------------------------------------------> Main Function Ends
"""