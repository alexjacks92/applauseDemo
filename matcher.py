import csv
import operator

class Tester:
    ''' Representation of a Tester, based on testers.csv '''
    def __init__(self, testerId, firstName, lastName, country, lastLogin):
        self.testerId = testerId
        self.firstName = firstName
        self.lastName = lastName
        self.country = country
        self.lastLogin = lastLogin
        self.deviceNames = []
        self.deviceIds = []
        self.findOwnedDevices()
        self.experience = -1; # We don't know what devices we care about yet

    def prettyPrint(self):
        ''' Print out all of this tester's data in a human readable way '''
        print('testerId: {}, firstName: {}, lastName: {}, country: {}, lastLogin: {}, experience: {}, devices: {}'
              .format(self.testerId, self.firstName, self.lastName, self.country, self.lastLogin, self.experience, self.deviceNames))

    def findExperience(self, devices):
        ''' Look up how many bugs this tester has filed for the given devices'''
        with open('bugs.csv') as bugsCSV:
            bugs = csv.reader(bugsCSV, delimiter=',')
            sortedBugs = sorted(bugs, key=operator.itemgetter(2))
            # bug[2] represents testerId, bug[1] represents deviceId
            filteredBugs = [bug for bug in sortedBugs if bug[2] == self.testerId and bug[1] in self.deviceIds]
            self.experience = len(filteredBugs)

    def findOwnedDevices(self):
        ''' Look up which devices this tester owns '''
        with open('tester_device.csv') as testerDeviceCSV:
            testerDevices = csv.reader(testerDeviceCSV, delimiter=',')
            sortedTesterDevices = sorted(testerDevices, key=operator.itemgetter(0))
            # device[1] represents device Id, device[0] represents the tester ID for the owner
            filteredDeviceIds = [device[1] for device in sortedTesterDevices if device[0] == self.testerId]
            self.deviceIds = filteredDeviceIds
            for deviceId in filteredDeviceIds:
                self.deviceNames.append(devicesMap[deviceId])

    def doesOwnAnyOf(self, devices):
        ''' Find out if this tester owns any of the devices in a list of device names '''
        for device in devices:
            if device in self.deviceNames:
                return True
        return False

# Look up table for device ID to device name
devicesMap = {}
with open('devices.csv') as devicesCSV:
            devices = csv.reader(devicesCSV, delimiter=',')
            devicesMap = dict(devices)

# Prompt user for search criteria
countriesSplit = input("Input one or more countries (comma separated): ").split(',')
countries = [country.strip() for country in countriesSplit]
devicesSplit = input("Input one or more devices (comma separated): ").split(',')
devices = [device.strip() for device in devicesSplit]

print('Searching for candidates in {} with {} devices...'.format(countries, devices))
testersCandidates = []

# Read in testers in the appropriate countries
with open('testers.csv') as testers:
    testersReader = csv.reader(testers, delimiter=',')
    for row in testersReader:
        if countries[0] == "ALL" or row[3] in countries:
            testersCandidates.append(Tester(row[0],row[1],row[2],
                                            row[3],row[4]))

# Filter down to testers with the appropriate devices and sort by experience
testersWithDevices = [candidate for candidate in testersCandidates if devices[0] == "ALL" or candidate.doesOwnAnyOf(devices)]
for tester in testersWithDevices:
    tester.findExperience(devices)
testersWithDevicesSorted = sorted(testersWithDevices, key=operator.attrgetter('experience'), reverse=True)

print('There are {} valid candidates:\n'.format(len(testersWithDevicesSorted)))
for tester in testersWithDevicesSorted:
    tester.prettyPrint()
