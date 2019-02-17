# Appraisal Letter

# Taking the Credentials
First_Name = input("Plz enter your first name: ")
Last_Name = input("Plz enter your last name: ")
Current_Salary = float(input("Plz enter your current salary: "))

# Printing the Appraisal Letter
print('''
 _____________________________________________________________________________
|Mr. {} {}                                                        |
|Senior Team Lead                                                             |
|Oberoi Industries Pvt. Ltd.                                                  |
|                                                                             |
|Date: 17th February,2019                                                     |
|                                                                             |
|From,                                                                        |
|Nakul Goenka                                                                 |
|HR Manager                                                                   |
|Oberoi Industries Pvt. Ltd.                                                  |
|                                                                             |
|Sub: Performance Appraisal                                                   |
|                                                                             |
|It is a great privilege for me to write this appraisal letter to you. Your   |
|performance has been really commendable and with sheer dedication you have   |
|become an asset to the organization.                                         |
|                                                                             |
|I proudly mention that company has decided to reward you with a raise in     |
|your salary by 15%. I have gone through your performance card and was        |
|surprised to see that you have always achieved your target well on time and  |
|sometimes even exceeded the same also. Your increment will be effective from |
|1st of next month.                                                           |
|                                                                             |
|We wish you all the best and hope you will continue to work with the same    |
|dedication in future also.                                                   |
|All The Best!                                                                |
|                                                                             |
|Yours Truly                                                                  |
|                                                                             |
|------------                                                                 |
|Nakul Goenka                                                                 |
|_____________________________________________________________________________|
'''.format(First_Name,Last_Name))