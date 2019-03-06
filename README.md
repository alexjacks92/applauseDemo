A Python script for matching testers to testing demands based on country and device criteria.

Requirements:
python 3.x
CSV file data formatted in the same way as the example files

Running:
python3 matcher.py

The program will prompt for country and device criteria. Inputs should be comma separated. It is whitespace tolerant but matches spelling exactly, so make sure to double check. For either criteria, input ALL to ignore it. Multiple arguments are treated as inclusive or – if either option matches, the tester is a valid candidate.

EX:
Input one or more countries (comma separated): JP, US
Input one or more devices (comma separated): iPhone 4
Searching for candidates in ['JP', 'US'] with ['iPhone 4'] devices...
There are 4 valid candidates:

testerId: 4, firstName: Taybin, lastName: Rutkin, country: US, lastLogin: 2013-01-01 10:57:38, experience: 125, devices: ['iPhone 4', 'iPhone 4S']
testerId: 8, firstName: Sean, lastName: Wellington, country: JP, lastLogin: 2013-08-05 13:27:38, experience: 116, devices: ['iPhone 4', 'iPhone 5', 'Nexus 4', 'HTC One', 'iPhone 3']
testerId: 1, firstName: Miguel, lastName: Bautista, country: US, lastLogin: 2013-08-04 23:57:38, experience: 114, devices: ['iPhone 4', 'iPhone 4S', 'iPhone 5', 'iPhone 3']
testerId: 5, firstName: Mingquan, lastName: Zheng, country: JP, lastLogin: 2013-08-04 22:07:38, experience: 109, devices: ['Galaxy S4', 'Nexus 4', 'Droid Razor', 'iPhone 4', 'iPhone 3']


$ python3 matcher.py
Input one or more countries (comma separated): ALL
Input one or more devices (comma separated): Nexus 4, Droid Razor
Searching for candidates in ['ALL'] with ['Nexus 4', 'Droid Razor'] devices...
There are 6 valid candidates:

testerId: 7, firstName: Lucas, lastName: Lowry, country: JP, lastLogin: 2013-07-12 23:57:38, experience: 117, devices: ['Galaxy S3', 'Galaxy S4', 'Nexus 4', 'Droid Razor', 'Droid DNA']
testerId: 8, firstName: Sean, lastName: Wellington, country: JP, lastLogin: 2013-08-05 13:27:38, experience: 116, devices: ['iPhone 4', 'iPhone 5', 'Nexus 4', 'HTC One', 'iPhone 3']
testerId: 5, firstName: Mingquan, lastName: Zheng, country: JP, lastLogin: 2013-08-04 22:07:38, experience: 109, devices: ['Galaxy S4', 'Nexus 4', 'Droid Razor', 'iPhone 4', 'iPhone 3']
testerId: 3, firstName: Leonard, lastName: Sutton, country: GB, lastLogin: 2013-07-16 21:17:28, experience: 106, devices: ['iPhone 5', 'Galaxy S3', 'Galaxy S4', 'Nexus 4']
testerId: 9, firstName: Darshini, lastName: Thiagarajan, country: GB, lastLogin: 2013-08-05 15:00:38, experience: 104, devices: ['Galaxy S4', 'Nexus 4', 'Droid DNA', 'HTC One']
testerId: 2, firstName: Michael, lastName: Lubavin, country: US, lastLogin: 2013-07-12 13:27:18, experience: 99, devices: ['Galaxy S3', 'Galaxy S4', 'Nexus 4', 'Droid Razor', 'Droid DNA', 'HTC One']

